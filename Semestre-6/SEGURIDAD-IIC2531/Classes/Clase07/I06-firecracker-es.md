---
marp: true
theme: default
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
style: |
  section {
    font-size: 28px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 50px;
  }

  img[alt~="align-right"] {
    margin-left: 400px;
  }

  img[alt~="align-center"] {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
  }
  
  /* Right-align terminal commands */
  .terminal-commands {
    text-align: right;
    margin-left: 400px;
  }
  
  /* Make sub-bullets lighter and smaller */
  ul ul li, ol ol li {
    color: #666666;
    font-size: 0.9em;
  }
  
  /* Make nested sub-bullets even lighter, italic, and smaller */
  ul ul ul li, ol ol ol li {
    color: #666666;
    font-style: italic;
    font-size: 0.8em;
  }
  
  /* Alternative: Use opacity for a more subtle effect */
  ul ul, ol ol {
    opacity: 0.8;
  }

---

# Aislamiento de SO y VM

---

# Caso de estudio: Paper de Firecracker de Amazon
  * Servicio Lambda: ejecutar aplicación Linux suministrada por el cliente, escalando según la carga
  * Desafío de seguridad: código arbitrario, necesita aislarlo de otros clientes
  * Desafío de rendimiento: la carga puede variar ampliamente
    * Podría ser mucho menos que una máquina (muchos clientes por máquina)
    * Podría crecer rápidamente y necesitar ejecutar código de cliente en nueva máquina
  * Objetivo: dominios de aislamiento de bajo overhead pero fuertes

---

# Enfoques de aislamiento
  * Procesos Linux (como en OKWS)
  * Contenedores, usando namespaces de Linux + cgroups
  * VMs
  * Runtimes de lenguaje

---

# Procesos Linux
  * IDs de usuario
  * Permisos por archivo
  * Diseñado para compartir granular entre usuarios, no aislamiento grueso
    * Básicamente tenemos demasiados recursos compartidos
  * Usamos permisos, chroot, etc. pero no es suficiente

---

# Los contenedores Linux sirven dos propósitos
  * Empaquetar software junto con todas las dependencias (bibliotecas, paquetes, archivos, etc)
  * Aislamiento de seguridad y rendimiento para ejecutar ese software
  * Ambos dependen de namespaces de Linux: abstracción de ejecutar en una máquina Linux separada
  * El aislamiento de rendimiento usa cgroups de Linux para controlar el uso de recursos

---

# ¿Por qué es desafiante el aislamiento en Linux?
  * Mucho estado compartido ("recursos") en el kernel
  * Las llamadas al sistema acceden al estado compartido nombrándolo
    * PIDs
    * Nombres de archivo
    * Direcciones IP / puertos
    * (Incluso IDs de usuario, en alguna forma)
  * El control de acceso típico gira en torno a IDs de usuario (ej., permisos de archivo)
    * Difícil usar eso para hacer cumplir aislamiento entre dos aplicaciones
    * Muchos archivos con permisos
    * Las aplicaciones crean archivos compartidos por accidente o a propósito (ej., world-writable)

---

# Mecanismo Linux: chroot
  * Vimos esto en OKWS
  * Beneficio: limita los archivos que una aplicación puede nombrar
    * No importa si la aplicación crea accidentalmente archivos world-writable
  * Algunas limitaciones técnicas, pero un buen punto de partida para mejor aislamiento

---

# Los namespaces proporcionan una forma de delimitar los recursos que se pueden nombrar
  * [[ Ref: https://blog.quarkslab.com/digging-into-linux-namespaces-part-1.html ]]
  * El proceso pertenece a un namespace particular (para cada tipo de namespace)
    * Los nuevos procesos heredan el namespace del proceso padre
  * Ej., el namespace PID limita los PIDs que un proceso puede nombrar
  * Aislamiento de grano grueso, no sujeto a lo que la aplicación podría hacer
  * Un chroot mejor diseñado para diferentes tipos de recursos (no solo sistema de archivos)

---

# Cgroups de Linux
  * Limitar / programar para uso de recursos
  * Memoria, CPU, I/O de disco, I/O de red, etc
  * Se aplica a procesos, similar a namespaces
    * Los nuevos procesos heredan el cgroup del proceso padre
  * No es un límite de seguridad, pero importante para prevenir ataques DoS
    * Ej., un proceso o VM trata de monopolizar toda la CPU o memoria

---

# Contenedores usando namespaces + cgroups
  * Desempaquetar archivos del contenedor en algún lugar del sistema de archivos
  * Asignar nuevo namespace para ejecutar contenedor
  * Apuntar el directorio raíz del namespace del contenedor al árbol de archivos del contenedor
  * Configurar cgroup para el contenedor basado en cualquier política de programación
  * Configurar una interfaz de red virtual para el contenedor
  * Ejecutar procesos en este contenedor
    * Parece ejecutarse en un sistema Linux separado
    * Su propio sistema de archivos, su propia interfaz de red, sus propios procesos (PIDs), etc

---

# ¿Por qué los namespaces no son suficientes para Lambda?
  * Kernel Linux compartido
  * Superficie de ataque amplia: 300+ llamadas al sistema, muchas funciones especializadas bajo ioctl...
  * Gran cantidad de código, escrito en C
    * Los errores (buffer overflows, use-after-free, ...) continúan siendo descubiertos
    * No hay aislamiento dentro del kernel Linux mismo
  * Los errores del kernel permiten al adversario escapar del aislamiento ("escalación de privilegios local" o LPE)
    * Relativamente común: nuevos errores LPE cada año

---

# Mecanismo de seguridad adicional: seccomp-bpf
  * Idea: filtrar qué llamadas al sistema puede invocar un proceso
  * Podría ayudarnos a abordar la amplia superficie de ataque del kernel Linux
  * Patrón común señalado en el paper de Lambda:
    * Los syscalls o características raramente usados son más propensos a tener errores
  * Cada proceso está (opcionalmente) asociado con un filtro de llamadas al sistema
    * Filtro escrito como un pequeño programa en el lenguaje bytecode BPF
    * El kernel Linux ejecuta este filtro en cada invocación de syscall, antes de ejecutar el syscall
    * El programa filtro puede decidir si el syscall debe ser permitido o no
    * Puede mirar syscall#, argumentos, etc
    * Los nuevos procesos heredan el filtro de syscall del proceso padre: "pegajoso"

---

# Mecanismo de seguridad adicional: seccomp-bpf (cont.)
  * Se puede usar seccomp-bpf para prevenir acceso a syscalls sospechosos
  * Usado por algunas implementaciones de contenedores
    * Configurar filtro bpf para deshabilitar llamadas al sistema sospechosas
  * ¿Por qué esto no es suficiente para Lambda?
    * Mal trade-off
    * Comenzando a romper código de cliente que usa syscalls poco comunes
    * Pero aún podría no ser suficiente para seguridad (mucho código/errores en syscalls comunes)

---
<!--
# Mecanismos de seguridad adicionales: control de acceso obligatorio
  * Ej., Linux tiene LSM (https://en.wikipedia.org/wiki/Linux_Security_Modules)
    * Muchas variantes: AppArmor, SELinux, etc
  * El administrador especifica política sobre qué operaciones están permitidas
    * Típicamente basado en qué usuario está ejecutando el proceso, o qué binario se está ejecutando
    * Puede especificar reglas amplias (ej., sin acceso de escritura a ningún archivo)

---

# ¿Por qué no runtimes de lenguaje para Lambda?
  * Queremos soportar binarios Linux arbitrarios
  * Veremos en más detalle los runtimes de lenguaje la próxima semana
  * Los runtimes de lenguaje son atractivos para cargas de trabajo tipo Lambda: overheads bajos
    * [[ Ref: https://developers.cloudflare.com/workers/learning/security-model ]]

---
-->

# Enfoque más pesado: VMs
  * Ejecutar Linux en una VM guest
    * Muy similar a la VM usada para ejecutar código de laboratorio para 6.858
  * ¿Por qué esto es mejor que Linux?
    * Superficie de ataque más pequeña: no hay syscalls complejos, solo x86 + dispositivos virtuales
    * Menos errores / vulnerabilidades: errores de escape de VM descubiertos menos de una vez al año
  * ¿Por qué estos tampoco son suficientes para Lambda?
    * Alto costo de inicio: toma mucho tiempo arrancar la VM
    * Alto overhead: gran costo de memoria para cada VM en ejecución
    * Errores potenciales en el VMM mismo (qemu): 1.4M líneas de código C
  * Plan del paper: escribir un nuevo VMM, pero seguir usando KVM

---

# ¿Qué implica implementar soporte para VMs?
  * Virtualizar la CPU y memoria
    * Soporte de hardware en procesadores modernos
    * Tablas de páginas anidadas
    * Virtualizar registros privilegiados que normalmente solo son accesibles al kernel
  * Virtualizar dispositivos
    * Controlador de disco
    * Tarjeta de red
    * PCI
    * Tarjeta gráfica
    * Teclado, puertos serie, ...
  * Virtualizar el proceso de arranque
    * BIOS, boot loader

---

# Linux KVM
  * [[ Ref: https://www.kernel.org/doc/html/latest/virt/kvm/api.html ]]
  * Abstracción para usar soporte de hardware para virtualización
  * Gestiona CPUs virtuales, memoria virtual
  <!-- * Soporte de hardware correspondiente: tablas de páginas anidadas -->

---

# QEMU
  * Implementa dispositivos virtuales, similar a lo que tendría el hardware real
  * También implementa dispositivos puramente virtuales (virtio)
    * Interfaz bien definida a través de regiones de memoria compartida
  * También implementa emulación de instrucciones de CPU
    * Principalmente no necesario cuando se usa soporte de hardware
    * Pero aún usado para instrucciones que el hardware no soporta nativamente
    * Ej., CPUID, INVD, ..
    * [[ Ref: https://revers.engineering/day-5-vmexits-interrupts-cpuid-emulation/ ]]
  * También proporciona alguna implementación de BIOS para comenzar a ejecutar la VM

---

# Diseño de Firecracker
  * Usar KVM para CPU virtual y memoria
  * Re-implementar QEMU
  * Soportar conjunto mínimo de dispositivos
    * virtio network, virtio block (disco), teclado, serie
  * Dispositivos de bloque en lugar de sistema de archivos: límite de aislamiento más fuerte
    * El sistema de archivos tiene estado complejo
      * Directorios, archivos de longitud variable, symlinks / hardlinks
    * El sistema de archivos tiene operaciones complejas
      * Crear/eliminar/renombrar archivos, mover directorios completos, r/w range, append, ...
    * El dispositivo de bloque es mucho más simple:
      * Bloques de 4 KByte
      * Los bloques están numerados del 0 al N, que es el tamaño del disco
      * Leer y escribir un bloque completo (Y tal vez flush / barrier)

---

# Diseño de Firecracker (cont.)
  * No soportar emulación de instrucciones
    * (Excepto instrucciones necesarias como CPUID, VMCALL/VMEXIT, ..)
  * No soportar BIOS en absoluto
    * Solo cargar el kernel en la VM en la inicialización y comenzar a ejecutarlo

---

# Implementación de Firecracker: Rust
  * Lenguaje memory-safe (módulo código "unsafe")
  * 50K líneas de código: mucho más pequeño que QEMU
  * Hace improbable que la implementación VMM tenga errores como buffer overflows
  * [[ Ref: https://github.com/firecracker-microvm/firecracker ]]

---

# El VMM de Firecracker se ejecuta en un proceso "encarcelado"
  * chroot para limitar archivos que el VMM puede acceder
  * namespaces para limitar el VMM de acceder a otros procesos y red
  * ejecutándose como un ID de usuario separado
  * seccomp-bpf para limitar qué llamadas al sistema puede invocar el VMM
  * Todo para asegurar que, si se explotan errores en el VMM, es difícil escalar el ataque

---

# Arquitectura Lambda alrededor del mecanismo central de Firecracker
  * Muchos workers (máquinas físicas ejecutando MicroVMs basados en Firecracker)
  * Cada worker tiene un número fijo de "slots" de MicroVM disponibles para ejecutar cosas
  * El código del cliente se carga en un "slot" iniciando una VM, cargando código del cliente
  * El manager de workers se encarga de decidir dónde se enrutan las solicitudes
  * El frontend busca worker del manager de workers, envía solicitud directamente allí

---

# ¿Qué tan bien logra Firecracker sus objetivos?
  * El overhead parece bastante bajo
    * 3MB overhead de memoria por VM inactiva
    * 125msec tiempo de arranque
  * El rendimiento parece OK
    * El rendimiento de CPU es básicamente KVM (así que, sin cambios)
    * El rendimiento de I/O de dispositivos no es tan bueno
      * Disco virtual lento: necesita concurrencia
      * Red virtual lenta: necesita PCI pass-through

---

# ¿Qué tan bien logra Firecracker sus objetivos? (cont.)
  * Seguridad probablemente bastante buena
    * Implementación Rust: menos propenso a errores
    * Mucho menos código en el VMM
    * Proceso VMM encarcelado
    * Linux KVM aún parte del TCB, pero mucho más pequeño que QEMU
    * Aún así, los errores de KVM socavarían el aislamiento de Firecracker
      * [[ Ref: https://googleprojectzero.blogspot.com/2021/06/an-epyc-escape-case-study-of-kvm.html ]]

---

# Algunos errores encontrados en Firecracker
  * [[ Ref: https://github.com/firecracker-microvm/firecracker/issues/1462 ]]
    * Problema de verificación de límites de memoria, a pesar de estar escrito en Rust
  * [[ Ref: https://github.com/firecracker-microvm/firecracker/issues/2057 ]]
    * Error DoS en interfaz de red
  * [[ Ref: https://github.com/firecracker-microvm/firecracker/issues/2177 ]]
    * El buffer de consola serie creció sin límite
    * Podría causar que una VM use mucha memoria a través del proceso Firecracker

---

# Firecracker usado fuera de Lambda
  * [[ Ref: https://fly.io/blog/sandboxing-and-workload-isolation/ ]]

---

# Plan alternativo: redirigir llamadas al sistema a una implementación diferente
  * En lugar de bloquear llamadas al sistema, interceptarlas e implementarlas en otro lugar
  * gVisor: implementación en espacio de usuario de muchas llamadas al sistema de Linux, en Go
  * Beneficio: menos probable tener errores de gestión de memoria en código Go
  * Beneficio: los errores no están en código del kernel, probablemente contenidos por proceso Linux
    * Usar seccomp-bpf para limitar qué syscalls puede invocar el emulador gVisor
  * Desventaja: los overheads de rendimiento podrían ser significativos
    * Cada llamada al sistema debe ser redirigida al proceso gVisor
    * Overhead de cambio de contexto, overhead de copia de datos, etc
  * Posible desventaja: compatibilidad (Linux real vs gVisor)
    * ¡gVisor hace un trabajo creíble implementando fielmente los syscalls de Linux!

---

# Resumen
  * El aislamiento es un bloque de construcción clave para la seguridad (una vez más)
  * Desafiante lograr aislamiento junto con otros objetivos:
    * Alto rendimiento
    * Overheads bajos (memoria, cambio de contexto, etc)
    * Compatibilidad con sistemas existentes (ej., Linux)
  * Caso de estudio del mundo real de ingeniería de un mecanismo de aislamiento
