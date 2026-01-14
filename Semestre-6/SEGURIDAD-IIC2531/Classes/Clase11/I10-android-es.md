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

# Seguridad de Android

---

# El tema de hoy es control de acceso app-vs-app
  * ¿Qué apps deberían poder usar tus contactos, ubicación, SMS, etc?
  * ¿Qué apps de terceros deberían poder interactuar?
  * Daremos por sentado:
    * Aislamiento de aplicaciones
    * Corrección del kernel y software del sistema
    * Defensa contra robo del dispositivo
  * Por supuesto es simplista ver estos como independientes:
    * Errores en un área pueden socavar otras áreas (ej. si aislamiento débil)
    * Fortaleza en un área puede ayudar a otros (ej. privilegio mínimo vs errores)

---

# Android tiene propiedades interesantes respecto a seguridad de aplicaciones
  * Cualquiera puede escribir una aplicación (no necesita permiso de Google)
  * Los usuarios pueden ejecutar cualquier app que les guste
  * ¡Seguro incluso si las apps son maliciosas! (Probablemente)
  * iOS es similar
    * ¡Pero sistemas de consumidor anteriores no lo eran!
    * iPhone/Android exploraron nuevo terreno para seguridad de aplicaciones de consumidor

---

# Desafío que Android aborda: aislamiento y compartir

---

# Las aplicaciones de escritorio proporcionan compartir fácil
  * (+) Las aplicaciones pueden interactuar fácilmente entre sí, compartir archivos
  * (+) El usuario puede elegir app para cada tarea (app de email, visor de imágenes, etc)
  * (-) Cada app tiene los privilegios completos del usuario
    * Así que, gran problema si una app es maliciosa o comprometida: ej., ransomware
  * (-) Poca noción de control app vs app para el mismo usuario
  * (-) El enfoque es acceso a archivos; no mucho control de acceso para IPC a servicios

---

# Los mecanismos de aislamiento proporcionan poco soporte para compartir
  * Ej., VMs como en AWS Lambda; WebAssembly
  * Aislamiento fuerte pero no muy adecuado para un dispositivo de usuario final
  * A veces el aislamiento fuerte se usa en sistemas de usuario final críticos para seguridad
    * Poner aplicaciones en VMs separadas
    * [[ Ref: https://www.qubes-os.org/ ]]
  * Pero difícil de usar en el caso común

---

# Los mecanismos de aislamiento proporcionan poco soporte para compartir (cont.)
  * Ej., manejar archivos de video:
    * Fotos/videos descargados en una VM
    * ¿Cómo editarlos en la VM de photoshop?
    * ¿Cómo subirlos a youtube después de eso?
  * Ej., manejar adjuntos de correo:
    * La VM de correo quiere ver un adjunto PDF; ¿cómo compartir con VM de PDF?
    * Llenó un formulario PDF en esa VM; ¿cómo enviarlo por email de vuelta a alguien?
  * Hemos visto algunas ideas de compartir pero nada que funcione para un usuario final
    * Compartir en OKWS a través de proxy de bd
    * Compartir en RLbox a través de API de biblioteca anotada

---

# Aplicaciones basadas en web/navegador (hablaremos más de ellas después):
  * (+) No necesita instalar aplicaciones o preocuparse por estado local
  * (+) El navegador aísla diferentes sitios web; bueno para seguridad
  * (-) El navegador aísla diferentes sitios web; no mucho compartir
  * (-) Requiere un servidor; difícil de usar offline

---

# ¿Cómo se ve una aplicación Android?
  * Proceso regular en Linux
  * Cada aplicación tiene almacenamiento de archivos privado
    * /data/data/appname
  * Manifiesto declarando sus permisos
  * La aplicación completa está firmada por el desarrollador

---

# ¿Cómo aísla Android las apps entre sí?
  * Objetivo: interacción *solo* vía mensajería Android
    * ej. sin compartir archivos
  * Aislamiento implementado con facilidades del kernel Linux
    * Originalmente solo UID de UNIX por aplicación
    * Ahora SELinux y seccomp para limitar privilegios de llamadas al sistema
    * Ej., SELinux protege archivos de app en tarjeta SD incluso cuando usa FAT sin ACLs

---

# ¿Es suficiente el aislamiento puro?
  * Necesitamos permitir+controlar acceso a contactos, teléfono, SMS, red, etc
  * Y a servicios de apps de terceros

---

# ¿Cómo interactúan y comparten información las aplicaciones?
  * Intent: primitiva de mensajería básica en Android
  * Permite a una app acceder a un servicio proporcionado por otra app, como RPC
  * Nota: sin acceso directo a archivos inter-app; toda interacción vía intents

---

# ¿Cómo se conectan los intents a las aplicaciones?
  * Enlaces Java para enviar / recibir intents
    * Android iniciará proceso de app si recibe un intent pero aún no está ejecutándose
  * Los enlaces Java esperan que la aplicación esté compuesta de "componentes"
  * Cuatro tipos de componentes:
    * Activity: componente UI de app, típicamente una activity por "pantalla"
    * Service: procesamiento en segundo plano, servicio RPC
    * Content provider: una base de datos SQL
    * Broadcast receiver: recibe anuncios broadcast de otros componentes
  * Los componentes aparecen en el manifiesto de la app

---

# Campos de Intent:
  * Component: nombre del componente objetivo (solo un string)
    * Ej., com.google.someapp/ComponentName
  * Action: el opcode para este mensaje (solo un string)
    * Ej., android.intent.action.MAIN, android.intent.action.DIAL, ..
  * Data: URI de datos para la acción (solo un string)
    * Ej., tel:16172536005, content://contacts/people/1 (para DIAL)

---

# Todos los intents son enrutados vía un único "monitor de referencia" confiable

---

# El intent puede ser implícito: sin nombre de componente especificado
  * El emisor no sabe qué app recibirá
  * El monitor de referencia determina el objetivo basándose en la acción
  * Así que puede ocurrir comunicación entre apps que no saben nada una de la otra
  * Genial para flexibilidad, sustitución de aplicaciones

---

# ¿Cómo decide el monitor de referencia si permitir un intent?
  * "Etiquetas de permiso" denotan privilegios individuales
    * Cada etiqueta es un string de forma libre
    * Comúnmente escrito como nombres de paquete estilo Java, por unicidad
    * Ej., com.android.phone.DIALPERM
  * Una aplicación tiene un conjunto de etiquetas que está autorizada a usar
    * Ej., si app puede marcar el teléfono, ...DIALPERM está en su conjunto de etiquetas
  * Cada componente tiene una sola etiqueta que lo protege
    * Cualquier intent a ese componente debe ser enviado por app que tenga esa etiqueta
    * Ej., servicio marcador de teléfono está etiquetado con ...DIALPERM
    * Para content providers, dos etiquetas: una para lectura, una para escritura

---

# Privilegios de ejemplo (todos estos son "peligrosos")
  * Calendario
  * Cámara
  * Contactos
  * Ubicación
  * Teléfono
  * SMS
  * Almacenamiento externo

---

# ¿Cómo obtiene una aplicación permisos?
  * El manifiesto de la app lista el conjunto de etiquetas de permiso que quiere
    * El manifiesto es escrito por el desarrollador
    * ¡El manifiesto puede pedir cualquier permiso (!)
  * El manifiesto también declara una etiqueta para proteger cada componente
  * Plan original: pedir permisos en tiempo de instalación
    * Android muestra permisos que solicita el manifiesto de la aplicación
    * El usuario puede decir "sí" o "no"
    * El paper dice que esto no funcionó bien: usuarios no equipados (sección 4.3.1)
  * Plan más nuevo: confirmar permisos cuando la app intenta usarlos
  * La app no puede cambiar su manifiesto (sin re-instalar, re-pedir)
  * El monitor de referencia conoce el manifiesto de cada app instalada

---

# Tres tipos de permiso de Android:
  * Normal:
    * El uso es poco probable que sea un problema de seguridad; a lo sumo molesto
      * Ej., cambiar wallpaper, cambiar volumen de audio, instalar un atajo
    * El sistema no pregunta al usuario sobre permisos "normales"
    * ¿Por qué molestarse en absoluto?
      * El usuario puede revisar si está realmente interesado
      * Privilegio mínimo, si la aplicación es comprometida después
  * Peligroso:
    * Podría permitir a una app hacer algo peligroso
    * Ej., enviar SMS, acceder a información de contacto
    * El sistema pregunta al usuario sobre permisos peligrosos
  * Firma:
    * Solo puede ser usado por apps firmadas por el mismo desarrollador
    * Ej., app de configuración de red es especial, otras apps no pueden pedir permiso

---

# ¿Por qué el manifiesto / monitor de referencia?
  * Alternativa: ¿componente decidiendo en tiempo de ejecución si aceptar cada intent?
  * ¡Los programadores tienden a olvidar verificaciones de seguridad!
    * Manifiesto + monitor de referencia hacen la aplicación por defecto
  * Ayuda al usuario a entender algunas implicaciones de seguridad de instalar una app
    * Elegir app que no pida permisos extraños
  * Ayuda a Google Play (tienda) a analizar aplicaciones

---

# Este es un ejemplo de Control de Acceso Obligatorio (MAC)
  * Permisos especificados separadamente del código
  * Los esquemas MAC aparecen mucho, tienen propiedades buenas:
    * Pueden ser analizados sin entender código de app
    * Proporcionan algo de seguridad a pesar de código de app descuidado
    * Usualmente fácil configurar políticas "por defecto nada"
  * Contraste: control de acceso discrecional (DAC) en Unix
    * Cada app UNIX establece sus propios permisos en archivos
    * Los permisos pueden ser cambiados por la app a lo largo del tiempo
    * Difícil decir qué pasará solo mirando permisos de archivo actuales

---

# Los componentes de app Android pueden realizar sus propias verificaciones en intents entrantes
  * Necesario cuando una aplicación proporciona un servicio RPC
    * Muchas funciones RPC diferentes
    * Diferente nivel de protección para cada función RPC
    * El monitor de referencia solo verifica si el cliente puede acceder al servicio completo
  * No es un modelo MAC puro: no se puede solo mirar el manifiesto

---

# La historia hasta ahora es relativamente simple:
  * Los permisos protegen acceso a componentes sensibles
  * Usualmente correspondencia uno a uno entre nombre de permiso y componente
  * Matriz: apps vs componentes
           SMS Camera Tweet
    App1    X           X
    App2         X      X
  * Jerga:
    * La app emisora es el "sujeto"
    * El componente receptor es el "objeto"
  * Los permisos protegen objetos contra uso por sujetos
    * Los permisos pueden proteger privacidad de datos en componentes
    * Los permisos no protegen la privacidad de intents enviados

---

# Los permisos de Android son bastante flexibles
  * Cualquier app puede inventar un nuevo permiso (no requiere privilegios especiales)
  * Las apps no tienen que saber quién usará los permisos
    * A diferencia de una ACL convencional, que lista usuarios específicos
    * Si un usuario cambia a un nuevo gestor de contactos compatible,
      * las apps que usan contactos continuarán funcionando
  * Las apps pueden pedir muchos privilegios si quieren
    * Pero es transparente -- el usuario ve y debe aprobar

---

# ¿Es bueno depender del usuario para decidir si los permisos están bien?
  * Funciona bien si la app no quiere nada peligroso
    * El usuario puede estar confiado de que la app no puede hacer mucho mal cuando se ejecuta
  * Si la app quiere permisos peligrosos:
    * Los usuarios no son buenos decidiendo sobre riesgos de seguridad
    * El usuario esencialmente tiene que decidir si el desarrollador es confiable
      * ¡Eso es difícil!
      * Pero mucho mejor que no preguntar
  * "Quién decide, y cómo" ha sido una pregunta desconcertante durante mucho tiempo

---

# Tristemente, el sistema de permisos requirió más complejidad para ser útil

---

# Problema: ¿cómo controlar distribución de intents broadcast privados?
  * Ej., intent SMS_RECEIVED enviado para un mensaje SMS entrante
  * La app de escucha puede declarar receptor broadcast "abierto"
    * Ya que las etiquetas defienden receptores, no emisores
  * Solución: el emisor puede especificar etiqueta de permiso extra para intent bcast
    * El monitor de referencia verifica que la app receptora tenga el permiso
    * Como si msg enviado fuera objeto, y receptor fuera sujeto
    * Así que receptor tendría que pedir al usuario permiso ej. RECEIVE_SMS
    * Nota: rompe modelo MAC ligeramente
      * Mirar el manifiesto no es suficiente para razonar sobre seguridad

---

# ¿Qué pasa si dos apps definen el mismo nombre de permiso?
  * La primera gana
  * Una app maliciosa podría registrar algún nombre de permiso importante como "normal"
  * Cualquier app puede entonces obtener este permiso sin preguntar al usuario
  * Otras apps pueden definir este permiso como "peligroso"
    * Pero el "peligroso" es ignorado si el permiso ya está definido

---

# Aparte: ¿por qué las aplicaciones deben estar firmadas por el desarrollador?
  * Permitir actualización solo si está firmada por el mismo desarrollador
  * Permitir permisos de firma si está firmada por el mismo desarrollador

---
<!--
# ¿Cómo dar a otra app permisos temporales?
  * Delegación de URI
    * Ej. App1 puede leer contenido, envía URI a App2 con flag
      * diciendo que App2 debería poder leer contenido URI también
    * El monitor de referencia mantiene registro de delegaciones
    * ¡Debe recordar revocar acceso delegado!
      * Ej., URI puede significar otro registro en un momento posterior..
  * Intents pendientes
    * App1 da intent pendiente a App2
      * App2 puede enviar después, ¡pero con permisos de App1!
      * El monitor de referencia mantiene registro
    * Caso de uso: callbacks a tu aplicación, para notificación de eventos
      * El intent puede apuntar a un componente privado en App1
      * Previene falsificación de notificación de evento ya que otras apps no pueden acceder
  * No es un modelo MAC puro: el manifiesto no tiene la historia de seguridad completa

---
-->

# Otro ejemplo de política MAC: Seguridad empresarial
  * El usuario puede definir múltiples perfiles en el mismo teléfono
  * La política SELinux proporciona aislamiento fuerte entre perfiles de usuario
  * Quizás otras políticas también pueden ser especificadas / aplicadas

---

# Mecanismos de seguridad de app fuera del dispositivo
  * Google Play Protect
  * Auditoría / escaneo del lado del servidor de aplicaciones
  * El dispositivo puede elegir instalar apps solo de la tienda Google Play
  * Similar a política iOS, pero no obligatorio

---

# ¿Qué tan segura es la "plataforma" Android?
  * Los errores de kernel y setuid-root sí ocurren
    * Y sí subvierten los controles de acceso
    * Pero son difíciles/caros de encontrar
  * Los usuarios instalan malware con permisos peligrosos
    * Malware común real: enviar mensajes SMS a números premium
    * Los atacantes obtienen dinero directamente desplegando tal malware
    * ¿Por qué los usuarios cometen tales errores?
      * Algunos permisos necesarios tanto para tareas mundanas + sensibles
        * Ej. ID único de dispositivo mismo permiso que acceder estado del teléfono
        * Muchas solicitudes de permisos peligrosos, desensibiliza al usuario
      * Otra causa: las apps piden permisos "por si acaso"
        * Una actualización posterior podría necesitarlos
      * Otra causa: no puede decir "no" a subconjunto de permisos
      * Otra causa: copias de apps Android existentes conteniendo malware

---

# ¿Cómo arreglar?
  * Preguntar al usuario cuando el permiso se usa realmente por primera vez
    * Realmente desplegado en Android ahora; uno de los cambios recientes mayores
    * El usuario puede instalar pero después decir "No" a uso de permiso específico
  * Permitir al usuario deshabilitar selectivamente ciertos permisos
  * Análisis estático/runtime y auditoría -- implementado por Google ahora
    * Busca clones casi idénticos de apps populares existentes
    * Ejecuta apps por un poco para determinar qué hacen
  * El mercado de apps de Android (Google Play) puede matar remotamente una app
  * ¿Cómo sabes que has instalado la aplicación bancaria correcta?
    * Tal vez una tienda de apps más coherente tipo iPhone ayudaría
    * Difícil explotar muchos teléfonos y evitar detección

---

# Resumen:
  * Android tiene una noción bien desarrollada de control de acceso app/app
    * Más útil que el control de acceso user/user de UNIX
    * Permisos sofisticados de grano fino a nivel de intents
  * Razonable descargar y ejecutar apps desconocidas, a diferencia de en escritorio
  * Depende del consentimiento del usuario, para bien o para mal
  * Ha sido bastante exitoso

---

# Referencias:
  * https://source.android.com/security/
  * http://developer.android.com/guide/topics/security/security.html
  * http://research.microsoft.com/pubs/149596/AppFence.pdf
  * http://seasonofcode.com/posts/internal-input-event-handling-in-the-linux-kernel-and-the-android-userspace.html
  * https://dzone.com/articles/depth-android-package-manager
  * https://en.wikipedia.org/wiki/Stagefright_(bug)
  * https://source.android.com/compatibility/cdd

