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

# Seguridad de dispositivos móviles

---

# ¿Qué ataques intenta abordar este diseño?
  * Alguien roba tu iPhone
  * Y quiere extraer datos de él

---

# Este diseño representa un gran esfuerzo: ¿por qué podría importarle a Apple?
  * Clientes que deben mantener secretos (médicos, gubernamentales, reporteros, etc)
  * Clientes ordinarios nerviosos sobre ej. contraseña bancaria
  * Ventaja competitiva vs ej. Android
  * Intentando hacer lo correcto

---

# El diseño asume:
  * El dispositivo está protegido con código de acceso
  * El dispositivo está bloqueado en el momento del robo

---

# ¿Cuáles son los ataques potenciales en un dispositivo robado?
  * Búsqueda exhaustiva de código de acceso -- a menudo solo cuatro dígitos
  * Suplantar la huella digital o rostro del usuario
  * Desarmar el teléfono y remover los chips de almacenamiento flash
    * O leer de la RAM encendida
  * Explotar un error en el kernel del SO
    * Teléfono bloqueado -- pero USB, WiFi, y radio pueden estar activos
  * Instalar una versión hackeada del SO sin verificaciones de seguridad
    * ¿Redirigir tráfico de red al servidor de actualización del adversario?
    * ¿Desarmar el teléfono y escribir SO diferente en chips flash?
  * Degradar a una versión antigua del SO que tiene un error conocido

---

# Diseño razonablemente exitoso para teléfonos robados
  * Mucho más difícil extraer datos de iPhone robado que hace 10 años
  * Incluso el FBI se queja
  * Aunque la historia sugiere que esto no es el final de la historia

---

# Arquitectura de hardware iOS:
  * CPU principal
  * RAM
  * Almacenamiento de archivos Flash
  * Motor de cifrado AES entre CPU principal / DRAM y almacenamiento flash
  * CPU de enclave seguro
  * Clave criptográfica "UID" en hardware del enclave
    * El enclave puede cifrar / descifrar pero no puede obtener el UID
  * Sensores de autenticación: lector de huellas digitales, cámara Face ID

---

# Arquitectura de hardware iOS (cont.)


                     
![width:450px align-center](arch.png)


---

# Aspectos interesantes del diseño, para esta clase:
  * Arranque seguro
  * Enclave
    * Ocultación de todas las claves y operaciones cripto de la CPU principal
    * Cifrado de datos controlado por código de acceso
    * Defensas contra búsqueda exhaustiva de código de acceso
    * Cripto entre unidades
  * Cifrado de datos
    * Ejecutar apps en segundo plano (cuando el teléfono está bloqueado)
  * Próxima clase: aislamiento y compartir de apps (enfocándose en Android)

---

# Arranque seguro
  * Objetivo: asegurar que el adversario no pueda ejecutar SO / apps / enclave modificados
  * Al encender, la CPU comienza a ejecutar desde Boot ROM
    * Solo lectura
    * Especificado en la fabricación del chip
  * Secuencia de arranque:
    * Boot ROM -> iBoot -> kernel del SO -> apps
  * Boot ROM verifica que el código iBoot esté firmado por Apple
  * iBoot verifica que el código del kernel del SO esté firmado por Apple
  * El kernel del SO verifica que las apps estén firmadas por desarrollador aprobado por Apple

---

# Ataques de degradación
  * Ataque: reemplazar kernel del SO con uno más antiguo con un error conocido
    * ¡Un kernel de SO antiguo firmado por Apple!
  * Ahora el adversario puede explotar un error antiguo en el kernel de SO antiguo
  * Solución strawman: registrar versiones
    * Ej., iBoot verifica que el kernel del SO sea al menos cierta versión
    * ¿Dónde se almacenaría el número de versión?
    * ¿Qué previene al adversario de modificar el número de versión almacenado?

---

# Prevención de degradación con ECID
  * Cada dispositivo tiene un ID único llamado ECID
    * Exclusive Chip ID
    * Solo lectura, establecido en el momento de fabricación del chip
  * Los servidores de Apple firman actualizaciones para un ECID específico
  * La secuencia de arranque verifica que la firma sea para el ECID de este teléfono
  * ¿Por qué esto ayuda?
    * Es poco probable que el adversario tenga el software antiguo con el ECID de la víctima
    * Los servidores de actualización de Apple no firmarán un kernel desactualizado

---

# Enclave seguro
  * El punto:
    * Prevenir que la CPU principal vea claves cripto
      * A cargo de toda la encriptación
    * Defender contra adivinación de código de acceso
      * Autenticar usuarios
  * La CPU pide al enclave hacer cosas, ej. ayudarla a descifrar
  * Implementado usando una CPU separada
    * Secuencia de arranque seguro, como la CPU principal
  * Comparte DRAM con la CPU principal
    * Se comunica con la CPU principal a través de DRAM
    * Cifra su propio contenido de memoria
    * Autentica memoria para integridad / frescura
    * Estado de autenticación de memoria almacenado en SRAM en chip

<!--
---

# Enclave seguro (cont.)
  * ¿Comparado con SGX?
    * Comparte objetivo de SGX de ocultar secretos de un kernel no muy confiable
    * CPU separada (no un modo)
    * Ejecuta solo software fijo de Apple (no aplicaciones)
-->

---

# Autenticación de usuario usando el enclave
  * Plan general:
    * Todos los datos de usuario están cifrados
    * Permitir descifrado cuando el teléfono está desbloqueado
    * Prohibir descifrado cuando el teléfono está bloqueado
  * ¿Por qué delegar autenticación al enclave seguro?
    * Prevenir que kernel del SO comprometido:
      * Obtenga claves de descifrado, datos de huella digital/rostro
      * Evite límites de reintentos de código de acceso
    * Permitir ocultación de claves, etc. con cifrado / auth de memoria
      * Así que lectura directa de RAM no produce secretos cripto
      * Muy costoso para CPU principal, pero aceptable para el enclave seguro

---

# Autenticación de usuario usando el enclave (cont.)
  * Mecanismo de autenticación primario: código de acceso
    * Claves de descifrado calculadas basadas en código de acceso (discutiremos después)
  * Mecanismos adicionales: huella digital, reconocimiento facial
    * El enclave seguro cachea claves de descifrado una vez que el usuario ingresa código de acceso
    * Usa estas claves si se presenta con huella digital o coincidencia de rostro correcta

---

# Protegiendo comunicación sensor-a-enclave
  * Ataque: SO comprometido repite lectura de huella digital al enclave seguro
  * Ataque: adversario sustituye sensor de huella digital falso
  * Diseño: autenticación criptográfica entre sensores y enclave seguro
    * El sensor tiene una clave AES secreta
    * El enclave conoce la misma clave secreta (compartida en el momento de fabricación del teléfono)
    * El sensor cifra y autentica todos los datos con la clave AES
    * Probablemente algún nonce o ID de sesión para prevenir repetición de datos antiguos

---

# Reconocimiento facial (una especie de aparte, pero sorprendentemente sofisticado)
  * La cámara de rostro incluye proyector de puntos IR, cámara IR
  * Muchos puntos IR, en un patrón aleatorio, se proyectan en el rostro del usuario
  * La cámara IR lee los puntos, los reporta al enclave seguro
  * Puede ayudar a distinguir rostro 3d de imagen 2d de rostro

---

# Cifrado de datos
  * Datos = archivos almacenados en flash
  * Ataque: el adversario desarma el teléfono, lee datos de chips flash
  * Plan: cifrar datos almacenados en chips flash

---

# ¿Por qué generan claves de cifrado de datos desde el código de acceso?
  * (versus almacenar la clave en algún lugar permanentemente)
  * Para que las claves no existan en ningún lugar del dispositivo después del reinicio
  * Para que las claves puedan olvidarse cuando el dispositivo se bloquea

---

# ¿Cómo generan claves de cifrado de datos desde el código de acceso?
  * Peligro: solo 9999 códigos de acceso, fácil probarlos todos
  * Peligro: el atacante extrae chips flash, prueba todos los códigos de acceso
    * en la máquina del atacante
  
---

# ¿Cómo generan claves de cifrado de datos desde el código de acceso? 
  * Esquema iOS:
    * El hardware del enclave contiene UID único y motor AES
    * El software del enclave no puede acceder al UID, solo puede cifrar/descifrar
    * La clave de cifrado de datos es aproximadamente E_UID(E_UID(...(passcode)))
      * es decir, cifrar con UID muchas veces
    * ¿Por qué?
      * Dependiente del código de acceso, así que la clave no existe en ningún lugar del dispositivo después del reinicio
      * En el enclave, que limita el número de intentos
      * Lento, para limitar velocidad de búsqueda exhaustiva
      * Dependiente del UID, para prevenir fuerza bruta fuera del dispositivo

---

# Desafío: apps en segundo plano
  * Cuando el teléfono está bloqueado, algunas apps deben poder ejecutarse y leer/escribir archivos
    * Ej., descargar adjuntos de email
    * Pero las claves se olvidan después de que el dispositivo se bloquea
  * Idea: "envoltorio de claves"
    * E_k1(k2)
  * Cualquiera que conozca k1 puede obtener k2, descifrando
  * Usado para delegar: de módulo que conoce k2 a módulo que conoce k1

---

# Cifrado de archivos
  * Metadatos del sistema de archivos (directorios, inodos, ...)
    * Cifrados con una sola clave, Kfs
  * Protegido por UID: el enclave seguro almacena E_UID(Kfs)
  * El enclave seguro da E_Ke(Kfs) al kernel del SO en el momento del arranque
  * ¿Por qué molestarse con Kfs en absoluto?
    * Hace posible borrar datos rápidamente, eliminando Kfs
    * O, realmente, eliminando E_UID(Kfs)
    * También, no puede tomar chips flash y conectar a otro teléfono
      * Kfs está envuelto con UID

---

# Cifrado de archivos (cont.)
  * El contenido de cada archivo está cifrado por una clave diferente, Kf
  * Esta clave está envuelta con un Kdf, E_Kdp(Kf)
  * Almacenar con los metadatos del archivo, cifrado con Kfs
  * Diferentes Kdf's para diferentes niveles de protección

---

# Diferentes niveles de "protección de datos"
  * Completo: puede descifrar si el teléfono está actualmente desbloqueado
    * Kdf se deriva del código de acceso al desbloquear, se descarta cuando se bloquea
  * Completo a menos que esté abierto: el archivo puede escribirse en cualquier momento (pero no leerse)
    * Caso especial Kdf para descarga en segundo plano de adjuntos
  * Hasta primera autenticación: .. si el teléfono fue desbloqueado desde el reinicio
    * Kdf se deriva del código de acceso en el primer desbloqueo, se descarta al apagar
    * Por defecto para datos de apps de terceros
  * Sin protección: puede descifrar en cualquier momento
    * Kdf se deriva solo del UID (no código de acceso), así que disponible desde el arranque
    * Pero permite borrado rápido, eliminación segura (ver abajo)
  * Los Kdfs se almacenan solo en el enclave seguro

---

# Usando claves de archivo envueltas
  * El código FS en la CPU principal ve solo claves envueltas
    * Pide al enclave seguro desenvolver claves necesarias
    * El enclave seguro desenvolverá, si tiene clave DP
  * ¡Pero el kernel del SO nunca obtiene las claves crudas!
    * Los datos son cifrados/descifrados por motor AES de hardware
    * Secreto compartido entre el motor AES y el enclave seguro: Ke
    * El enclave seguro envuelve la clave de archivo con la clave del motor AES
      * E_Ke(Kf)
    * Envía esta clave envuelta al kernel del SO
    * El kernel del SO puede programar el motor AES según sea necesario

---

# ¿Cómo obtener claves de protección de datos con Touch ID o Face ID?
  * No se puede usar Touch ID / Face ID inmediatamente después del reinicio;
    * primero debe ingresar código de acceso
  * Cuando se ingresa el código de acceso, el enclave calcula las claves Kdp
  * El enclave aparta copias (cifradas) para uso posterior con * ID
  * Cuando el usuario bloquea el teléfono, el enclave elimina Kdp
  * Pero puede volver a obtener claves con Touch ID / Face ID

---

# Eliminación segura de datos
  * Objetivo: permitir al usuario borrar rápidamente datos en el teléfono
  * Objetivo: borrar teléfono después de 10 intentos fallidos de desbloqueo
  * Desafío: ¡difícil eliminar datos!
    * Toma tiempo
    * Flash hace copias para nivelación de desgaste
  * "Almacenamiento borrable"
    * Acceso directo especial de NAND flash para enclave seguro
    * Puede emitir operaciones de flash NAND de bajo nivel para eliminar datos
    * Usado para almacenar E_UID(Kfs)

---

# ¿Lugares para buscar debilidades?
  * El kernel en la CPU principal ve mucho material sensible
    * Código de acceso, datos descifrados, contraseñas web, etc
    * Pero el kernel iOS ha tenido errores que las apps pueden explotar
      * Estos dan a una app privilegios root / kernel en la CPU principal
    * Por suerte no puedes instalar nuevas apps maliciosas en un teléfono bloqueado
  * El código de arranque puede tener errores; arrancar un kernel que permite adivinación de código de acceso
  
---

# ¿Lugares para buscar debilidades? (cont.) 
  * El software USB, WiFi, y radio probablemente tiene errores,
    * y puede estar activo incluso cuando el teléfono está bloqueado
  * Las claves privadas de Apple deben mantenerse seguras, pero también deben usarse para
    * firmar actualizaciones "personalizadas"
    * (probable que haya varias/muchas claves privadas)
  * ¿Puede extraerse el UID del hardware si tienes suficiente dinero?

---

# ¿Hay un costo para esta seguridad iOS?
  * El hardware especializado cuesta dinero (enclave, lector de huellas digitales, AES DMA)
  * Irritante tener que escribir código de acceso
  * Necesitas código de acceso en muchas situaciones, ej. respaldando
  * Las actividades en segundo plano son incómodas, cuando el dispositivo está bloqueado
  * Código de acceso olvidado -> datos permanentemente perdidos (a menos que estén respaldados)

---

# Varias ideas / técnicas interesantes
  * Arranque seguro: firma de código, prevención de degradación
  * Enclave seguro: comunicación cifrada/autenticada con sensores
  * Protección de datos: claves de archivo, envoltorio de claves, clave de dispositivo, almacenamiento borrable

---

# Referencias
  * Arranque seguro: https://queue.acm.org/detail.cfm?id=3382016
  * Seguridad de plataforma Apple (otoño 2019): https://support.apple.com/guide/security/welcome/web
  * Códigos de Autenticación de Punteros:
    * https://lwn.net/Articles/718888/
    * https://googleprojectzero.blogspot.com/2019/02/examining-pointer-authentication-on.html
  * Consideraciones similares en Android: https://www.usenix.org/conference/enigma2019/presentation/mayrhofer
  * http://blog.ptsecurity.com/2020/03/intelx86-root-of-trust-loss-of-trust.html
  * Fallo de seguridad:
    * https://arstechnica.com/information-technology/2020/10/apples-t2-security-chip-has-an-unfixable-flaw/

