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
    position: absolute;
    margin-top:0px
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

# Autenticación de Usuarios

  * Un problema importante
    * Base de muchas políticas de seguridad
    * Problemas técnicos interesantes
    * Fácil de hacer mal
  * Continúa siendo un desafío, porque la seguridad no es solo un problema técnico
    * Los usuarios eligen contraseñas malas
    * Pero, las contraseñas tienen otras propiedades redentoras (fáciles de usar, implementables)

---

# Recordatorio: ¿Dónde encaja la autenticación?

  * Modelo de guardia de seguridad del sistema informático
    * cliente -> solicitud -> servidor
  * El servidor contiene algún recurso nombrado por la solicitud
  * El servidor contiene un guardia que verifica cada solicitud
    * Ej., función invocada en el código del servidor cuando se maneja cada solicitud
  * Mediación completa: todas las solicitudes verificadas por un guardia
    * 1. Aislamiento del servidor: no hay forma de evitar la interfaz y acceder al recurso directamente
    * 2. Guardia invocado en todas las solicitudes
  * Desafío: ¿cómo autentica el guardia una solicitud?
    * ¿qué principal originó la solicitud?

---

# Las tres partes de la autenticación de usuarios

  * Registro
    * ej., establecer secreto entre usuario y guardia
  * Verificación de autenticación
    * ej., usuario envía (usuario, secreto) junto con la solicitud
    * guardia verifica que el secreto coincida con su copia
  * Recuperación
    * ej., usuario pierde el secreto
    * a menudo pasado por alto; puede ser un talón de Aquiles
  * Muchos desafíos para hacerlo bien

---

# Desafío: principales intermedios

  * Los usuarios rara vez emiten solicitudes directamente
    * Desde el punto de vista del recurso final, solo recibió un paquete TCP..
  * La solicitud típicamente emitida vía máquina cliente, balanceador de carga, servidor de aplicaciones, ..
    * Típicamente decimos que estos principales intermedios "hablan por" el usuario
  * Importante considerar estas entidades intermedias como principales
    * Fuerza a considerar la posibilidad de que la solicitud no sea realmente del usuario
  * Necesitamos estar seguros de que cada principal intermedio sea realmente confiable

---

# Ejemplo: inicio de sesión en un sitio web

  * La solicitud viene del dispositivo del usuario (ej., teléfono/portátil)
    * El dispositivo es el principal intermedio
  * El usuario escribe contraseña/código en el dispositivo
  * ¿Qué pasa si el atacante controla el dispositivo?
    * Malware/keylogger
  * El atacante puede lanzar un ataque de hombre en el medio
    * ej., atacante graba la contraseña y luego la usa más tarde
  * Gran problema en la práctica (más abajo)

---

# Desafío: ¿cuál es la identidad del usuario?

  * El usuario registra algún secreto --- ¿quién es el usuario realmente?
    * A la escala de la universidad, podríamos verificar la identidad del usuario al registrarse
  * Típicamente nos conformamos con una garantía más débil
    * Establecer que el usuario que inicia sesión tiene el secreto al registrarse
    * Si es así, entonces asumimos que es el mismo usuario
    * Pero, no hay garantía de que conozcamos la verdadera identidad del usuario
    * Para muchos usos eso está bien
      * Ej., a Amazon no le importa realmente quién eres mientras pagues

---

# Enfoques de registro

  * Primero en llegar, primero en ser servido
    * Ej., registrarse para una cuenta en gmail.com
  * Arrancar desde otro mecanismo
    * Ej., verificar vía email
  * Creado por administrador
    * Ej., nuevo empleado en una empresa

---

# Enfoques de recuperación

  * "Preguntas de seguridad": política OR
  * Verificar vía email
  * Probar conocimiento del número de tarjeta de crédito, etc.
  * Crear una nueva cuenta (si no es importante retener el mismo principal/nombre)
  * Llamar al servicio al cliente: puede ser una salida de emergencia sin una política precisa
    * A menudo susceptible a ataques de ingeniería social

---

# Secreto común: contraseñas

  * Principal y guardia comparten un conjunto secreto de bits
    * llamar a este conjunto de bits una "contraseña"
  * El usuario escribe nombre de usuario y contraseña.
  * El guardia verifica si la contraseña es correcta para ese nombre de usuario.
  * Ventaja: 
    * Fácil de usar e implementar
  * Desventajas: 
    * Las contraseñas son a menudo muy valiosas 
    * Factor humano -> secretos débiles y muchas veces compartidos

---

# Desafío: las contraseñas son valiosas, pero a menudo débiles

  * Defensa: usarlas lo menos posible
    * Solo para autenticación de usuario
  * Una vez autenticado, usar claves cripto entre servidor/clientes
    * Certificados de cliente, cookies, etc.
  * Incluso para autenticación de usuario, acorralar el secreto componiéndolas con otras ideas
    * Gestor de contraseñas, inicio de sesión único, autenticación de dos factores, etc.
    * 2FA: Biométrico (ej., botón de huella dactilar de apple/android)
  * Rate limiting

---

# Contraseñas: difíciles por factores humanos

  * 1. Los usuarios eligen contraseñas adivinables
    * 20% de las cuentas usan el mismo conjunto de 5,000 contraseñas más populares
    * No se puede permitir que un adversario haga 5,000 intentos de adivinar la contraseña de un usuario
    * No se puede permitir que un adversario adivine "123456" como la contraseña de cada usuario
  * 2. Las contraseñas comunes contienen dígitos, mayúsculas y minúsculas, etc.
    * ¿Es "1Password!" una buena contraseña?
    * Lo que importa es la entropía: ¿qué tan común es esa contraseña?
      * Los requisitos de caracteres no son especialmente útiles

---

# Contraseñas: difíciles por factores humanos (cont.)

  * La entropía de la contraseña generalmente se expresa en términos de bits:
    * Una contraseña que ya se conoce tiene cero bits de entropía
    * Una que se adivinaría en el primer intento la mitad del tiempo tiene 1 bit de entropía
    * Una contraseña de 16 bits de entropía requiere 2^16 intentos para probar todas las posibilidades
  * 3. Las contraseñas a menudo se comparten entre sitios/aplicaciones/sistemas
    * Importante cuando hablamos de cómo usar y almacenar contraseñas
  * 4. Queremos animar a los usuarios a elegir contraseñas de alta entropía

---

# ¿Es una buena idea cambiar las contraseñas frecuentemente?

  * Depende de las amenazas
  * Beneficios de nuevas contraseñas:
    * Incluso si el adversario obtuvo la contraseña antigua, ya no es útil
    * Tal vez esto fuerza al usuario a no reutilizar la contraseña entre sitios
  * Desventajas de nuevas contraseñas:
    * El usuario podría tener dificultades para recordarla
    * El usuario podría elegir una contraseña más débil, o escribirla en algún lugar
  * No hay una política clara ganadora

---

# Defensa: Gestores de contraseñas

  * Los usuarios están tentados a usar contraseñas simples
    * Pueden recordarlas
    * Pero baja entropía
  * Los usuarios están tentados a usar la misma contraseña para diferentes sitios
    * ¡Mala idea!
  * Gestores de contraseñas: contraseñas convenientes, fuertes y diferentes
    * El gestor de contraseñas elige contraseña con alta entropía
    * El gestor de contraseñas almacena diferentes contraseñas para diferentes sitios
    * Opcionalmente: el gestor de contraseñas llena el campo de contraseña (ej., en un navegador PM)
  * El usuario debe autenticarse al gestor de contraseñas
    * El usuario debe recordar una contraseña fuerte
  * ¡El gestor de contraseñas es confiable!

---

# Defender contra adivinación

  * Los ataques de adivinación son un problema debido al pequeño espacio de claves
    * El adversario tiene acceso a mucha información sobre distribuciones de contraseñas
    * Contraseñas comunes (ej., vía filtraciones de bases de datos de contraseñas)
    * Frases populares de sitios web
    * Sesgos comunes del usuario en la selección de caracteres
  * Datos encriptados con contraseña vulnerables a adivinación offline
    * No hay servidor involucrado en verificar un intento

---

# Limitar intentos de autenticación

  * No queremos permitir que un adversario adivine contraseñas
  * Importante limitar la tasa de intentos de inicio de sesión
    * Implementar períodos de tiempo de espera después de demasiados intentos incorrectos
  * Limitar por usuario podría no ser suficiente
    * El adversario puede adivinar "123456" para cada nombre de usuario
  * ¿CAPTCHAs?
    * El costo económico de resolver CAPTCHAs es bastante bajo
  * La mayoría de los sistemas tienen varias heurísticas para limitar la tasa de adivinación de contraseñas

---

# Almacenar contraseñas

  * Plan ingenuo: almacenar una tabla que contenga pares (nombre de usuario, contraseña)
  * Riesgo: adversario que compromete el servidor aprende todas las contraseñas
  * Problema 1: incluso después de la recuperación del compromiso, debe restablecer todas las contraseñas de usuario
  * Problema 2: el adversario puede usar las mismas contraseñas para iniciar sesión en otros servicios

---

# Hashing

  * Almacenar pares de (nombre de usuario, H(contraseña))
  * Aún se puede verificar si la contraseña suministrada coincide, hasheándola
  * El hash criptográfico es unidireccional, no se puede invertir

---

# Salting

  * Rainbow tables: se puede construir un diccionario de hashes de todas las contraseñas comunes
  * Solución: almacenar (nombre de usuario, salt, H(salt || contraseña))
  * Se puede verificar hasheando la contraseña suministrada con el salt conocido
  * Pero ahora la misma contraseña puede corresponder a muchos hashes diferentes
  * Costoso construir una tabla de todas las combinaciones comunes de salt+contraseña, si el salt es grande

---

# Hacer el hashing costoso

  * Las funciones de hash cripto típicas son rápidas
  * El adversario no está limitado en tasa al adivinar contra una lista comprometida de hashes de contraseñas
  * Solución: usar una función de hash intencionalmente costosa (llamada función de derivación de claves, o KDF)
  * Buscar en Google bcrypt, scrypt, PBKDF2, ..

---

# Aumentar contraseñas: autenticación de dos factores

  * Ayuda a defender contra contraseñas débiles y reutilización de contraseñas
  * Ayuda contra ataques MITM y phishing
    * MITM = hombre en el medio
  * Variantes comunes

---

# Código 2FA enviado vía SMS al teléfono celular del usuario

  * El servidor almacena solo el número de teléfono del usuario (y el código recientemente enviado)
  * Ventajas: 
    * Fácil de empezar a usar
    * Fácil recuperarse de un teléfono perdido, cambiar proveedores, ..
      * Externalizar el problema al proveedor de teléfono celular, portabilidad de números
  * Desventajas: 
    * Confiar en la red de teléfono celular y el proveedor
    * Requerir que el usuario esté en el rango de la red de teléfono celular
    * Ataques de phishing

---

# 2FA con contraseñas de un solo uso basadas en tiempo (TOTP)

  * El servidor y el dispositivo del usuario acuerdan un valor secreto (ej., escanear código QR)
  * El dispositivo del usuario genera código = H(secreto || tiempo actual)
  * El servidor verifica que el código corresponda al tiempo actual
  * Ventajas: 
    * No hay necesidad de que la red de teléfono celular esté disponible
    * No hay necesidad de confiar en el proveedor de teléfono celular
  * Desventaja: la configuración del usuario implica instalar aplicación, cargar valor secreto

---

# 2FA con contraseñas de un solo uso basadas en tiempo (TOTP) (cont.)

  * Desventajas: 
    * Lidiar con el usuario cambiando dispositivos (recargar valor secreto)
    * Aún susceptible a ataques de phishing

---

# 2FA con desafío-respuesta (U2F)

  * El dongle USB del usuario tiene un par de claves pública/secreta
  * El servidor almacena la clave pública del dongle USB
  * Para iniciar sesión, el servidor envía una cadena de desafío aleatoria a la computadora del usuario (ej., navegador)
  * El navegador envía el desafío del servidor y la identidad al dongle USB
  * El dongle USB firma (desafío, identidad del servidor) con la clave privada
  * El servidor verifica que la firma se refiera al desafío correcto y la identidad

---

# Ventajas de U2F

  * Ventajas: 
    * No susceptible a ataques de phishing
    * No hay necesidad de configuración por servidor
    * El compromiso del servidor no permite que el adversario se autentique más tarde
  * Desventajas: 
    * Necesidad de software especial en la computadora del usuario (no solo escribir código)
    * El usuario necesita llevar el dongle

---

# El protocolo U2F se basa en cripto de clave pública; dos operaciones en particular

  * Sign(Kpriv, m) -> firma sig
  * Verify(Kpub, m, sig) -> ok?
  * Estado U2F:
    * Dispositivo (D): (H/Origin, Kpub, Kpriv)
    * Servidor (S): (H/Origin, Kpub)
    * Navegador (B): ejecutando JavaScript de S en el navegador
      * ¡Nunca ve Kpriv de D!
      * Incluso si B está comprometido, B no puede robar Kpriv

---

# Punto de partida simplificado para el protocolo U2F

  * S->B: desafío
  * B->D: desafío
  * D->B: Sign(Kpriv, desafío) -> firma s
  * B->S: s
  * S: Verify(Kpub, desafío, s) -> ok?
  * El desafío es un número aleatorio, a menudo llamado "nonce"
  * ¿Por qué el ataque de replay no funcionará?

---

# Considerar pasos del ataque

  * El atacante graba s cuando la víctima inicia sesión en bank.com
  * Más tarde el atacante visita bank.com, inicia sesión como la víctima
    * S elige un nuevo desafío, y lo envía al atacante
  * Cuando se solicita respuesta U2F, el atacante reenvía s grabado de la víctima
  * S calculará Verif(Kpub, nuevo desafío, s), que fallará
    * porque D firmó el desafío antiguo, no el nuevo

---

# Problema 1 con protocolo simplificado: ataque de phishing

  * El usuario visita el sitio web del adversario (bad.com)
  * El adversario (bad.com) visita un sitio real (bank.com), obtiene desafío para el inicio de sesión del usuario
  * bad.com envía desafío al usuario
  * El dispositivo del usuario firma el desafío
  * bad.com envía el desafío al sitio real (bank.com), el inicio de sesión tiene éxito

---

# U2F protege contra ataques de phishing vinculando el desafío a la identidad del servidor

  * S->B: desafío
  * B->D: CD={desafío, origen}
    * donde origen es realmente H(protocolo || nombre de host || puerto)
  * D->B: Sign(Kpriv, CD) -> firma s
  * B->S: s, CD
  * S: Verify(Kpub, CD, s), y verificar que CD contenga el desafío esperado + origen
  * El adversario causará que el navegador B envíe un CD diferente, así que firma diferente

---

# Problema 2 con protocolo simplificado: puede vincular dispositivos entre sitios

  * Los servidores pueden comparar sus valores Kpub para aprender qué usuarios son los mismos
  * Problema de privacidad; no se podría decir que el usuario es el mismo con contraseñas
  * U2F protege contra vinculación entre sitios con registro de claves por sitio
    * Al momento del registro, el dispositivo genera clave fresca (Kpub, Kpriv)
    * El dispositivo envía Kpub en claro, pero envía Kpriv encriptado con Kwrap

---

# U2F protege contra vinculación entre sitios (cont.)

  * Kwrap almacenado en el dispositivo (la única clave que se almacena a largo plazo)
  * La encriptación de Kpriv está asociada con el origen
  * "Handle" es solo este Kpriv encriptado
  * En desafío posterior, el dispositivo desencripta el handle en Kpriv, verifica el origen

---

# Otros ataques

  * El atacante compromete el cliente
    * Podría robar cookie de sesión después del inicio de sesión
    * Podría engañar al usuario para que presione el botón de clave de seguridad para iniciar sesión en otro sitio
  * El atacante roba el dispositivo
    * Aún necesita la contraseña del usuario, si es fuerte
  * El atacante suministra dispositivo malo al usuario
    * Tal vez la atestación del dispositivo detectará esto y evitará el registro

---

# Resumen

  * La autenticación de usuarios es difícil
  * Las contraseñas una solución duradera
  * Fortalecer contraseñas con gestor de contraseñas y 2FA
  * Primer encuentro con cripto:
    * Función de hash criptográfica
    * Firmar/Verificar con par de claves públicas

---

# Referencias

  * http://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-817.pdf
  * http://www.cl.cam.ac.uk/~jcb82/doc/B12-IEEESP-analyzing_70M_anonymized_passwords.pdf
  * http://arstechnica.com/security/2013/10/how-the-bible-and-youtube-are-fueling-the-next-frontier-of-password-cracking/
  * http://cynosureprime.blogspot.com/2015/09/how-we-cracked-millions-of-ashley.html
  * https://blog.acolyer.org/2017/06/21/the-password-reset-mitm-attack/
  * https://tools.ietf.org/id/draft-balfanz-tls-channelid-01.html
  * https://developers.yubico.com/U2F/Protocol_details/Overview.html
  * https://www.yubico.com/2017/10/infineon-rsa-key-generation-issue/
  * https://www.wired.com/story/chrome-yubikey-phishing-webusb/
  * http://blog.dustinkirkland.com/2013/10/fingerprints-are-user-names-not.html
  * https://www.allthingsauth.com/2018/02/27/sms-the-most-popular-and-lea
  * https://www.dongleauth.info/
  * https://www.yubico.com/products/manufacturing/
  * https://blog.duszynski.eu/phishing-ng-bypassing-2fa-with-modlishka/
