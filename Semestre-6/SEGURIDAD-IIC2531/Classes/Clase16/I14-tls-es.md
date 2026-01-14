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

# Canal Seguro

---

# Canal Seguro
  * TCP/IP no proporciona autenticidad y confidencialidad
  * Usando criptografía, superponemos un canal seguro sobre TCP/IP
    * Caso de estudio: TLS/SSL
  * Los canales seguros son una base sólida para la seguridad
    * Ejecutar HTTP sobre SSL y la Web es "segura"
      * Convirtiéndose en el predeterminado
    * Ejecutar SMTP sobre SSL y la entrega de correo es "segura"
    * Ejecutar IMAP/POP sobre SSL y la recogida de correo es "segura"
    * Etc.
  * Área de seguridad bien entendida/desarrollada

---

# La criptografía es un mecanismo de seguridad poderoso

  * Cifrado: confidencialidad
  * Firmas: integridad
  * Dos tipos de llaves
    * Clave pública vs clave privada
    * Llave Simétrica

---

# Operaciones de clave pública:
  * KeyGen() -> clave pública PK, clave secreta SK
  * Encriptación
    * Encrypt(PK, mensaje m) -> texto cifrado c
    * Decrypt(SK, c) -> m
  * Firma
    * Sign(SK, m) -> firma sig
    * Verify(PK, m, sig) -> ¿ok?

---

# Operaciones de clave simétrica:
  * KeyGen() -> clave privada K
    * Hay que hacerla llegar a ambos participantes
  * Encriptación
    * Encrypt(K, m) -> c
    * Decrypt(K, c) -> m
  * Firma
    * MAC(K, m) -> etiqueta t
  * Las claves para MAC y cifrado deben ser diferentes. 
    * Si necesitas tanto cifrado como MAC, necesitas dos claves.

---

# Establecer un canal seguro
  * Objetivo: establecer una clave compartida para criptografía simétrica
  * Strawman:
    * C --> S: conectar
    * C <-- S: mi clave pública es PK_S
    * C --> S: Encrypt(PK_S, freshKey)
    * C <-> S: Encrypt(freshKey, m...)

---

# Problema 1: autenticar el servidor
  * ¿Qué pasa si un adversario intercepta mensajes al servidor?
    * La vista del cliente es exactamente la misma
    * El cliente tendrá una clave compartida con el adversario
    * El adversario puede conectarse al servidor real y reenviar mensajes
    * Los mensajes subsecuentes parecen estar bien
    * "Ataque de hombre en el medio"
  * Necesitamos vincular PK_S a la identidad del servidor

---

# Solución: certificados
  * Servidor de autoridad confiable
  * Mantiene tabla de pares (nombre principal, clave pública)
    * El nombre principal es típicamente el nombre DNS del servidor
  * Otros participantes confían en que el servidor de autoridad tenga el mapeo correcto
    * Necesitan conocer la clave pública del servidor de autoridad para arrancar todo esto
  * Más sobre certificados en la próxima clase

---

# Solución: certificados (cont.)
  * Podría consultar el servidor, pero eso es malo para disponibilidad, rendimiento
  * En cambio, el servidor de autoridad puede firmar un mensaje:
    * Sign(SK_CA, {servidor, PK_server})
  * Este es el "certificado" del servidor
  * El servidor puede enviar este certificado al cliente
  * El cliente puede verificar que está correctamente firmado por PK_CA
  * El adversario no podría proporcionar tal certificado para PK_S del adversario

---

# Protocolo strawman revisado:
  * C --> S: conectar
  * C <-- S: PK_S, Sign(SK_CA, {servidor: PK_S})
  * C --> S: Encrypt(PK_S, freshKey)
  * C <-> S: Encrypt(freshKey, m...)

---

# Solución alternativa: confianza en el primer uso (TOFU), como en SSH
  * Asumir que la primera conexión está bien
  * Recordar el vínculo entre PK_S y el nombre principal del servidor para uso futuro
  * Más fácil de desplegar, menos propiedades de seguridad

---

# Problema 2: autenticar los mensajes
  * C <-> S: Encrypt(freshKey, m...)
  * Supongamos que el cliente envía la solicitud "Transferir $1 a la cuenta de Bob"
  * El cifrado garantiza confidencialidad pero no integridad
    * Una forma de pensarlo: Decrypt() siempre tiene éxito
    * El adversario manipula el texto cifrado -> Decrypt devolverá otra cosa
    * A veces efectos predecibles: voltear bit de texto cifrado -> voltear bit de mensaje
    * Nota que esto no rompe la confidencialidad
    * En nuestro ejemplo: voltear un bit para enviar $129 a Bob

---

# Solución: usar MAC() para calcular una etiqueta de autenticación
  * C <-> S: c=Encrypt(freshKey1, m...), t=MAC(freshKey2, c)
    * [ Nota: importante usar claves diferentes para Encrypt y MAC ]
  * Esto se llama "Cifrado autenticado"
  * La etiqueta será incorrecta: mensaje rechazado después de manipulación

---

# ¿Qué pasa si el adversario retransmite los mensajes?
  * No manipula el mensaje pero solo lo envía 129 veces
  * Desde la perspectiva del servidor: 129 mensajes válidos
  * Necesitamos defender contra ataques de replay

---

# Solución: mantener registro de mensajes previamente vistos
  * Descartar mensajes que ya han sido procesados
  * Dos enfoques comunes:
    * Número de secuencia en el mensaje
      * El receptor rastrea el último número de secuencia visto
      * Descartar mensajes con números de secuencia más antiguos
      * Bueno para protocolos orientados a flujo
    * Expiración / ID de sesión en el mensaje
      * El receptor rastrea TODOS los mensajes pasados dentro del tiempo de expiración o dentro de la sesión
      * Descartar mensajes previamente recibidos
      * Bueno para protocolos orientados a mensajes (no flujo)

---

# Problema 3: compromiso futuro del servidor
  * ¿Qué pasa si un malo compromete el servidor más tarde?
  * Puede usar SK_S para descifrar paquetes de red antiguos
  * Esto a su vez revela el valor freshKey para tráfico antiguo
  * ¡Puede descifrar el contenido del tráfico antiguo!

---

# Solución: secreto hacia adelante (forward secrecy)
  * No usar claves de largo plazo para cifrado
    * Susceptible al descifrado por un adversario futuro
  * En cambio, usar claves de corta duración para cifrado, y claves de largo plazo para firmar
    * Un adversario futuro puede falsificar firmas en el futuro, pero es demasiado tarde
  * Strawman de secreto hacia adelante para nuestro protocolo:
    * C --> S: conectar
    * C <-- S: PK_conn, Sign(SK_CA, {servidor: PK_S}), Sign(SK_S, PK_conn)
    * C --> S: Encrypt(PK_conn, freshKey)
    * C <-> S: Encrypt(freshKey, m...)

---

# SSL/TLS
  * El protocolo de canal seguro para la Web
    * SSL originalmente definido por Netscape
    * TLS es la versión estándar internacional
  * Mejoras a lo largo de los años
    * SSL 2.0, SSL 3.0 (1996), TLS 1.0 (1999), TLS 1.1 (2006), TLS 1.2 (2008), TLS 1.3 (2018)
    * SSL 2: https://www-archive.mozilla.org/projects/security/pki/nss/ssl/draft02.html
    * SSL 3: https://paulkocher.com/doc/SSLv3.pdf
    * https://en.wikipedia.org/wiki/Transport_Layer_Security
    * SSL 3.0 ahora está "prohibido"
      * El protocolo usa cifrados de bloque incorrectamente (CBC)
      * O usa cifrado de flujo débil (RC4)

---

# SSL/TLS (cont.)
  * Partes principales:
    * Protocolo de registro (enviar/recibir mensajes)
    * Protocolo de handshake (configurar claves para autenticar/cifrar mensajes)

---

# Análisis: modelos de amenaza
  * Atacantes activos
    * Manipulan y falsifican mensajes
  * Atacantes pasivos
    * Solo escuchando
        * ej., análisis de tráfico
    * SSL (especialmente con cifrado de flujo)
      * La longitud del texto cifrado revela la longitud del texto plano
      * Permite al atacante aprender qué página web fue accedida
    * Puede aprender qué computadoras se están comunicando

---

# Handshake SSL 3.0 (simplificado)
1. C -> S: Hello: versión del cliente, randomC, session_id, cifrados
2. S -> C: Hello: versión del servidor, randomS, session_id, cifrados
3. S -> C: ServerCertificate: lista de certificados
4. S -> C: HelloDone
      * [[ el cliente elige pre_master_secret aleatorio ]]
5. C -> S: ClientKeyExchange: cifrar (pre_master_secret, PK_S)
6. C -> S: ChangeCipherSpec
7. C -> S: finished, MAC({master_secret ++ msg 1,2,3,4,5}, C_mac_key) (y cifrado)
8. S -> C: change cipher spec
9. S -> C: finished, MAC({master_secret ++ msg 1,2,3,4,5,7}, S_mac_key) (y cifrado)
10. C -> S: cifrar({data, MAC(data, C_mac_key)}, C_enc_key)
   master_secret <- PRF(pre_master_secret, "master secret", randomC+randomS)
   (C_mac_key, C_enc_key) <- PRF(master_secret, "key expansion", randomS+randomC)

---

# Ataque SSL 2.0
  * El adversario podría editar el mensaje ClientHello sin ser detectado
    * Decirle a S que sustituya cifrados fuertes con cifrados débiles

---

# Riesgo SSL 3.0: ataque de retroceso de versión
  * El adversario modifica ClientHello para ser digamos versión 2
  * Los clientes agregan "marcador" en bytes de relleno autenticados
  * Funciona solo con intercambio de claves RSA

---

# Ataque SSL 3.0: eliminar ChangeCipher
  * MAC no incluye mensaje 6 y 8
  * el atacante elimina 6 y 8
  * ¡El cliente y el servidor no cambiarán a usar cifrados!
  * El atacante puede cambiar datos a S
  * TLS 1.0: Finish debe ser precedido por ChangeCipher

---

# SSL 3.0: POODLE (Oct 2014)
  * MAC no cubre el relleno de cifrado de bloque
  * Puede usarse para adivinar cookie en un pequeño número de intentos
  * Operación normal:
    * cifrado: Ci = E(K, Mi) xor Ci-1
      * Eso es Cipher Block Chaining (CBC), E = AES
      * C0 = un vector de inicialización aleatorio
    * descifrado: Mi = D(K, Ci) xor Ci-1
    * en formato de mensaje SSL: msg || MAC de 20 bytes || relleno
      * el último byte del último bloque registra el número de bytes de relleno
      * otros bytes en el relleno no están especificados, cualquier cosa está bien
      * ¡MAC no cubre el relleno!

---

# SSL 3.0: POODLE (cont.)
  * Receptor: descifrar bloques, eliminar relleno, recalcular MAC, verificar MAC,
    * eliminar MAC
  * Atacante:
    * 1. Hacer que el usuario ejecute javascript que envía post al sitio web que el usuario está usando
      * POST /path Cookie: name=<value>\r\n\r\nbody || MAC de 20 bytes || relleno
      * El javascript del atacante puede acceder a la cookie, pero el navegador la enviará
    * 2. El atacante interpone en el tráfico entre cliente y sitio web
      * a. El atacante ve la versión cifrada del mensaje anterior, pero el atacante puede organizar:
        * - un bloque completo de relleno P
        * - Ci para que el primer byte a adivinar de la cookie esté en el último byte
      * b. copiar Ci en P

---

# SSL 3.0: POODLE (cont.)
  * si el servidor acepta el mensaje, entonces
    * - D(K, Ci)[15] xor Cn-1[15] = 15
      * Sabemos que D(K, Ci)[15] = Mi[15] xor Ci-1[15]
      * => Mi[15] = 15 xor Cn-1[15] xor Ci-1[15]
    * - el atacante pasa al siguiente byte de la cookie
  * si el servidor rechaza el mensaje, la conexión se cierra
    * - reintentar post en una nueva conexión
      * IV/clave diferente
    * - con 256 intentos, deberíamos tener suerte

---

# SSL 3.0: POODLE (cont.)
  * Ver https://www.openssl.org/~bodo/ssl-poodle.pdf para detalles completos
  * O, https://www.imperialviolet.org/2014/10/14/poodle.html
  * Observación:
    * error de protocolo; no error de implementación
    * SSL3.0 ahora está prohibido
    * TLS no permite que los bytes de relleno estén sin especificar

---

# Ser explícito/Principio de Horton
  * La cita de Horton es "Quise decir lo que dije y dije lo que quise decir",
    * que los autores adoptaron para el diseño de protocolos
  * Principio de diseño, útil para analizar protocolos
  * Cada mensaje debe ser explícito sobre el contexto del que depende
  * El mensaje Finish en SSL3.0 no es explícito sobre el mensaje 6

---

# La seguridad también depende de la implementación
  * SSL/TLS es complicado, por lo tanto errores de implementación
    * ¡TLS 1.3 más simple que 1.2!
  * Implementación popular: openSSL
    * Error Heartbleed en 2014
      * El adversario puede robar la clave privada
      * Error de desbordamiento de búfer

---

# ¿Quién puede acceder a datos cifrados?
  * Los canales seguros protegen contra un adversario que controla la red
  * Los datos están disponibles como texto plano en cualquiera de los extremos del canal seguro
  * Un servidor comprometido puede obtener acceso a los datos: el servidor tiene la clave de descifrado
  * Alternativa: no darle al servidor la clave de descifrado

---

# Cifrado extremo a extremo / cifrado en reposo
  * Datos cifrados con una clave del destinatario previsto a nivel de aplicación
    * No necesariamente el servidor que transmite o almacena el mensaje
  * Ej., mensajería de texto: cifrar con la clave del otro usuario
    * El servidor almacena y reenvía texto cifrado, no puede mirar dentro
    * El destinatario puede eventualmente descifrar el mensaje
  * Ej., almacenamiento de archivos: cifrar con la clave propia del usuario
    * El servidor almacena datos cifrados, no puede mirar dentro
    * El usuario puede descargar el archivo de vuelta del servidor, descifrarlo
    * Lab 5

---

# Cifrado extremo a extremo (cont.)
  * Poderoso: elimina preocuparse por ataques al servidor (w.r.t. confidencialidad)

---

# Datos cifrados compartidos: ¿cómo dar acceso a múltiples usuarios a un documento compartido?
  * Plan ingenuo: cifrar el mismo documento con la clave de cada usuario.
  * Desventaja: múltiples copias, posiblemente versiones divergentes.
  * Mejor plan: encadenar claves.
    * Generar una nueva clave solo para el documento.
    * Cifrar documento con la clave pública del documento.
    * Cifrar la clave secreta del documento con la clave pública de cada usuario.

---

# Referencias
  * Ataque por Rizzo y Duong puede permitir al adversario aprender algo de texto plano
    * emitiendo muchas solicitudes cuidadosamente elegidas sobre una sola conexión.
    * [ Ref: http://www.educatedguesswork.org/2011/09/security_impact_of_the_rizzodu.html ]
  * Ataque reciente por las mismas personas usando compresión, mencionado en la clase de Paul Youn.
    * [ Ref: http://en.wikipedia.org/wiki/CRIME ]
  * Más recientemente, más ataques de oráculo de relleno.
    * [ Ref: https://www.openssl.org/~bodo/ssl-poodle.pdf ]

---

# Referencias (cont.)
  * Algunos servidores/CAs usan criptografía débil, ej. certificados usando MD5.
  * Algunos clientes eligen criptografía débil (ej., SSL/TLS en Android).
    * [ Ref: http://op-co.de/blog/posts/android_ssl_downgrade/ ]
  * Algunas implementaciones usan mala aleatoriedad para generar claves
    * [ Ref: https://wiki.debian.org/SSLkeys#End_User_Summary ]
  * Pero, la criptografía rara vez es la parte más débil de un sistema.
  * Handshake RSA versus DH
    * https://blog.cloudflare.com/keyless-ssl-the-nitty-gritty-technical-details/
  * Handshake TLS 1.3 ilustrado
    * [ Ref: https://tls13.ulfheim.net/ ]

