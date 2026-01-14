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

# Seguridad TCP/IP

---

# Próximas clases: seguridad de red
  * Una gran red abierta (Internet) invita a muchos ataques
    * Decentralizada, nadie está a cargo
  * Desafíos:
    * Autenticación/confidencialidad
    * Liveness (responsividad)
    * Privacidad
  * Hoy: ataques a protocolos de red centrales
    * Más adelante: soluciones criptográficas host/host

---

# Modelo de Amenaza

* El adversario puede mirar tus datos
* Pueden mandar paquetes arbitrarios
* Pueden modificar paquetes en transito

---

# Núcleo de Internet
  * Red abierta que consiste en muchos ISPs
    * VTR, Movistar, GTD, AT&T, Comcast, etc.
    * Acuerdos de peering entre ISPs para proporcionar conectividad
  * Muchos protocolos:
    * TCP, BGP, DHCP
    * UDP, telnet, FTP, IMAP, etc.
  * Protocolos definidos por organismo estándar (IETF) a través de RFCs
    * Muchas implementaciones de protocolos
    * Cambiar protocolo mucho más difícil que cambiar implementación
        * Ej., IPv4 -> IPv6
        * Un problema si tenemos una vulnerabilidad

---

# Internet hoy 
  * Mucho progreso en capas superiores seguras: kerberos, ssh, ssl
    * Habilitado por criptografía (que no estaba disponible en 1980)
  * Pero la red central no proporciona seguridad
    * Red abierta
    * IPsec difícil de desplegar globalmente y de uso limitado
  * Buen diseño
    * La red central principalmente preocupada por liveness
    * Seguridad extremo a extremo en los hosts
    * El diseño es exitoso
      * Ej., soporta comercio electrónico hoy
      * Ej., evolucionó con cambios tecnológicos importantes (ethernet, WIFI, etc.)
  * Sin embargo, los ataques antiguos (y nuevas versiones de ataques antiguos) son relevantes

---

# Aplicación de ejemplo: inicio de sesión remoto ca. 1980
  * telnet -- simplemente abre una conexión TCP al programa de login
    * No hay encriptación
    * ¿Qué puede hacer un atacante?
        * Robar la contraseña, etc. espiando en la red
        * Modificar los datos en tránsito
        * Inyectar datos falsos
        * Redirigir toda la conversación vía enrutamiento
    * Todo habría sido difícil en ARPANET
        * Pero el advenimiento de Ethernet hizo que el sniffing de contraseñas fuera un peligro real
  * rlogin -- no envía contraseña
    * El host de destino tiene una lista de nombres de hosts confiables (archivo .rhosts)
    * Permite que el usuario inicie sesión sin contraseña si el host fuente está en la lista confiable

---

# ¿Por qué rlogin parecía estar bien?
  * Los autores no habrían afirmado "seguro" -- pero quizás "bastante bueno"
  * Gran problema potencial: el atacante podría poner la IP del cliente confiable en el campo de dirección fuente
  * Pero la comunicación TCP involucra *ambas* direcciones
    * Si el atacante miente sobre la fuente, entonces las respuestas del servidor no volverán al atacante, por lo que el atacante no podrá ejecutar TCP correctamente.

---

# Veamos los detalles de la configuración de conexión TCP:
  * Handshake estándar:
    * C: SRC=C, DST=S, SYN(SNc)
    * S: SRC=S, DST=C, SYN(SNs), ACK(SNc+1)
    * C: SRC=C, DST=S, ACK(SNs+1)
    * C: SRC=C, DST=S, data(SNc), ACK(SNs)
  * El punto principal: establecer números de secuencia iniciales para paquetes de datos.
  * ¿Por qué uno podría pensar que el servidor puede saber que está hablando con C?
    * Solo C debería haber sido capaz de recibir el segundo mensaje.
    * Por lo tanto, solo C debería saber SNs.
    * El servidor solo acepta el tercer mensaje si tiene el SNs esperado.

---

# Ataque de número de secuencia TCP.
  * Supongamos que el adversario A quiere simular una conexión a S desde C.
    * (Asume que A conoce la dirección IP de C -- generalmente no es gran cosa en la práctica.)
    * A: SRC=C, DST=S, SYN(SNc)
    * S: SRC=S, DST=C, SYN(SNs), ACK(SNc+1)
    * A: SRC=C, DST=S, ACK(SNs+1) -- pero ¿cómo adivinar SNs?
    * A: SRC=C, DST=S, data(SNc)
  * ¿Cómo podría el adversario adivinar SNs?
    * Muchos hosts mantenían variable ISN, para usar en la próxima conexión.
      * (ISN es "número de secuencia inicial".)
      * Incrementar en 128 cada segundo, 64 después de cada nueva conexión.
      * Ayuda a evitar que paquetes antiguos interfieran con nueva conexión.
    * El adversario puede hacer una conexión ordinaria para averiguar el ISN actual,
      * luego adivinar el siguiente sumando 64.

---

# Ataque de número de secuencia TCP (cont.)
  * ¿Qué pasa con el paquete real que S envía a C (segundo pkt)?
    * C asumiría que el paquete es de una conexión antigua, enviaría RST en respuesta.
    * Incluso si ese RST se envió, el adversario podría intentar competir antes de que llegue el RST.
    * Resulta que el atacante puede suprimir C; llegaremos a eso más adelante.
  * Pero ¿por qué los ataques de número de secuencia se convierten en un problema de seguridad?

---

# 1. Forjar dirección IP fuente a servicios que autenticaban basándose en dirección IP.
  * El atacante puede pretender ser un host en la lista confiable de rlogin, enviar comandos
    * Sin necesidad de conocer una contraseña.
  * rlogin hizo una mala suposición sobre lo que proporcionaba la capa TCP.
    * Asumió que una conexión TCP desde una dirección IP significaba que realmente venía de ese host.
  * En realidad, la autenticación de rlogin era aún peor:
    * El servidor rlogin usaba búsqueda DNS inversa para obtener el nombre del host de la fuente de conexión.
    * ¡El dueño del dominio inverso puede establecer *cualquier* nombre de host para una dirección IP!
    * Puede hacer una ligera mejora: verificar si el host se resuelve a la misma dirección.

---

# 2. Ataque de denegación de servicio: reset de conexión.
  * Si podemos adivinar SNc, podemos enviar un paquete RST.
  * Peor aún: el servidor aceptará un paquete RST para cualquier valor SNc dentro de la ventana.
  * ¿Qué tan malo es un reset de conexión?
    * Un objetivo de tales ataques eran las conexiones TCP entre enrutadores BGP.
    * Causa que los enrutadores asuman falla de enlace, podría afectar el tráfico por minutos.


---

# 3. Secuestrar conexiones existentes.
  * Si puedes adivinar números de secuencia, puedes inyectar datos en una conexión existente.
  * Es decir, esperar a que alguien inicie sesión, luego tomar el control de la conexión.
  * [ Ref: Blind TCP/IP hijacking is still alive, por lkm@phrack.org (2007) ]
  * [ Ref: https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/cao (2016) ]

---

# ¿Cómo mitigar ataques que forjan direcciones IP fuente?
  * **NO USAR AUTENTICACIÓN POR IP.**
  * Algunas aplicaciones ahora tienen autenticación criptográfica extremo a extremo.
    * Ej. ssh, ssl, Kerberos.
    * Próxima clase: ssl.
  * Los ISPs pueden filtrar paquetes con direcciones IP fuente obviamente forjadas.
  * El core de internet no es autenticar.

---

# ¿Cómo fortalecer TCP contra direcciones IP fuente forjadas?
  * Hacer más difícil para el atacante adivinar el siguiente ISN.
  * No se puede elegir ISN's de manera completamente aleatoria, sin violar la especificación TCP.
    * Necesita evitar números de secuencia recientemente usados para el mismo par host/puerto.
  * ¿Incrementos aleatorios?
    * No se puede incrementar demasiado rápido; no queremos envolver muy a menudo.
    * Entonces no hay una gran cantidad de aleatoriedad (digamos, 8 bits bajos por incremento).


---

# ¿Cómo fortalecer TCP contra direcciones IP fuente forjadas? (cont.)

  * Sin embargo, ¡los valores SN para diferentes pares src/dst nunca interactúan!
  * Entonces, podemos elegir el ISN usando un offset aleatorio para cada par src/dst.
    * ISN = ISN_oldstyle + SHA1(srcip, srcport, dstip, dstport, secret)
  * No requiere estado extra para rastrear ISNs por conexión.
  * El punto: el atacante ya no puede hacer una conexión ordinaria para adivinar el ISN actual para un cliente diferente.

---

# ¿Siguen siendo relevantes los ataques de dirección IP fuente forjada?
  * La mayoría de los sistemas operativos implementan el esquema ISN por conexión anterior.
    * [ Ref: Linux secure_tcp_sequence_number en net/core/secure_seq.c ]
        * Usar siphash en lugar de SHA1 (https://en.wikipedia.org/wiki/SipHash)
  * Pero otros protocolos sufren de problemas similares -- ej., DNS.
    * DNS corre sobre UDP, sin números de secuencia, solo puertos, y puerto dst fijo (53).
    * El cliente hace verificaciones básicas de cordura en el paquete de respuesta.
    * Si el adversario sabe que el cliente está haciendo una consulta, puede falsificar una respuesta.
      * Solo necesita adivinar el puerto del cliente, a menudo predecible.
    * Ataque popular comenzando en 2008.
      * [ Ref: http://cr.yp.to/djbdns/forgery.html ]
      * [ Ref: http://unixwiz.net/techtips/iguide-kaminsky-dns-vuln.html ]

---

# ¿Siguen siendo relevantes los ataques de dirección IP fuente forjada? (cont.)
  * Solución: ¡aprovechar cuidadosamente toda la aleatoriedad posible!
    * Las consultas DNS contienen ID de consulta de 16 bits, y pueden aleatorizar ~16 bits de puerto src.
  * Solución: DNSSEC (registros DNS firmados, incluyendo registros faltantes).
    * Problema: distribución de claves (¿quién tiene permitido firmar cada dominio?)
    * Problema: enumeración de nombres (para firmar respuestas "no existe tal nombre").
      * Parcialmente mitigado por NSEC3: http://tools.ietf.org/html/rfc5155
    * Adopción lenta, no mucho incentivo para actualizar, costos no triviales.
    * Los costos incluyen tanto rendimiento como administrativos (gestión de claves/certificados).

---

# Liveness es otra gran área problemática para la capa de red.
  * Incluso cuando no hay problemas de autenticación,
    * ¡aún dependemos de los protocolos de red para realmente entregar los datos!
  * "Denegación de Servicio" (DoS) puede ser molesto, o parte de extorsión.
    * o un ingrediente en un ataque más grande.

---

# SYN flooding -- el primer ataque DoS de alto perfil.
  * El servidor debe ser capaz de verificar ACK(SNs) del cliente en el 3er paquete.
    * La implementación original mantenía estado para cada conexión "medio abierta".
    * Lo mantuvo por minutos en caso de que el cliente sea lento, o la red con pérdidas.
    * Solo dispuesto a recordar ej. 50 conexiones medio abiertas, para evitar quedarse sin memoria.
    * Ignoraba silenciosamente nuevas conexiones si ya tenía 50 esperando.
  * El ataque:
    * El atacante envía paquete SYN con direcciones IP aleatorias forjadas.
      * La mayoría de las direcciones forjadas no responden...
      * Por lo que el servidor nunca obtiene el 3er paquete.
    * Llena las 50 ranuras medio abiertas del servidor.
    * ¡Ahora el servidor ignora solicitudes de conexión legítimas!

---

# SYN flooding (cont.)
  * Difícil de rastrear:
    * Direcciones fuente aleatorias forjadas.
    * Tasa baja -- el atacante solo necesitaba enviar unos pocos paquetes SYN por
      * segundo, ya que los servidores mantenían conexiones medio abiertas por minutos.
  * Estos ataques aparecieron en 1996 y fueron un gran problema por un tiempo.

---

# Defensa contra SYN flooding: SYN cookies.
  * Idea: hacer el servidor sin estado, hasta que reciba ese tercer paquete (ACK).
    * Entonces el servidor no tendrá conexiones medio abiertas, y por lo tanto no se quedará sin.
  * ¿Por qué esto es complicado?
    * El estado medio abierto ayudaba a asegurar que la dirección IP fuente no estaba forjada, verificando que el 3er paquete tenía el ACK correcto.
  * Usar un poco de criptografía para que el servidor no tenga que mantener estado.
  * Codificar el estado del lado del servidor en el número de secuencia.
    * ISNs = SNc + (timestamp || SHA1(src/dst addr+port, secret, timestamp))
    * El timestamp no es fino (ej., minutos).
    * ISNs se envuelve lentamente asumiendo elección legítima de SNc del cliente.

---

# Defensa contra SYN flooding: SYN cookies (cont.)
  * ISNs por cliente, por lo que el atacante no puede adivinar para una dirección IP forjada.
    * La parte hash de ISNs cambia, por lo que no es útil por mucho tiempo si se roba uno.
    * [ Ref detallada: http://cr.yp.to/syncookies.html ]
  * El servidor calcula seq como arriba al enviar respuesta SYN-ACK.
  * El servidor puede verificar que el estado está intacto verificando el hash en el seq del ACK.
  * Las SYN cookies han detenido exitosamente ataques DoS de SYN flooding de baja tasa.

---

# Otro tipo de ataque DoS: amplificación de ancho de banda.
  * El objetivo del atacante es abrumar el servidor o enlace para que el tráfico legítimo sea descartado.
  * Enviar paquetes de solicitud ICMP echo (ping) a la dirección de broadcast de una red.
    * Ej., 18.26.7.255.
    * Solía ser que obtendrías una respuesta ICMP echo de todas las máquinas en la red.
    * ¿Qué pasa si falsificas un paquete desde la dirección de la víctima? La víctima obtiene todas las respuestas.
    * ¡Encuentra una subred con 100 máquinas en una red rápida: amplificación de 100x!
      * [ Ref: http://en.wikipedia.org/wiki/Smurf_attack ]

---

# Amplificación de ancho de banda (cont.)
  * ¿Podemos arreglar esto?
    * Los enrutadores ahora bloquean "broadcast dirigido" (paquetes enviados a dirección de broadcast).
 
---

<!--
  * Variante moderna: amplificación DNS.
    * DNS también es un servicio de solicitud-respuesta.
    * Con una consulta pequeña, el servidor podría enviar una respuesta grande.
    * Con DNSSEC, las respuestas contienen muchas firmas, ¡así que son aún más grandes!
    * Como DNS corre sobre UDP, la dirección fuente está completamente sin verificar.
      * [ http://blog.cloudflare.com/deep-inside-a-dns-amplification-ddos-attack ]

---

# Amplificación de ancho de banda (cont.)
  * ¿Podemos arreglar el ataque DNS?
    * Quizás arreglando servidores DNS para que solo respondan a clientes legítimos.
    * Difícil: muchos servidores de nombres deben responder a un conjunto abierto de clientes.
  * Versión moderna usando Memcached:
    * https://blogs.akamai.com/2018/02/memcached-udp-reflection-attacks.html
  * Versión moderna usando "middleboxes" de red:
    * https://www.akamai.com/blog/security/tcp-middlebox-reflection

---

# Protocolos de enrutamiento: demasiado confiados en los participantes.
  * ARP: dentro de una sola red Ethernet.
    * Para enviar paquete IP, necesitas la dirección MAC Ethernet del enrutador / próximo salto.
    * Protocolo de Resolución de Direcciones (ARP): difundir una solicitud para la MAC del objetivo.
    * Cualquiera puede escuchar la difusión, enviar una respuesta; sin autenticación.
    * El adversario puede hacerse pasar por enrutador, interceptar paquetes, incluso en red conmutada.

---

-->

# Protocolos de enrutamiento (cont.)
  * DHCP: nuevamente, dentro de una sola red Ethernet.
    * El cliente pide una dirección IP enviando una solicitud de difusión.
    * El servidor responde, sin autenticación (algunas especificaciones existen pero no se usan ampliamente).
      * Si acabas de conectarte a una red, podría no saber qué esperar.
    * Muchos campos: dirección IP, dirección de enrutador, servidor DNS, lista de dominio DNS, ...
    * El adversario puede hacerse pasar por servidor DHCP para nuevos clientes en la red.
      * Puede elegir sus servidores DNS, dominios DNS, enrutador, etc.

---

# Protocolos de enrutamiento (cont.)
  * BGP: Internet-wide.
    * El sistema de enrutamiento BGP es enorme; los atacantes controlan ISPs y enrutadores BGP.
      * Ref: http://web.mit.edu/6.033/www/papers/InterdomainRouting.pdf
      * Contratos entre ISPs
      * Ref: https://www.xfinity.com/peering
    * Cualquier enrutador participante BGP puede anunciar ruta a cualquier dirección IP.
    * Ataque: anunciar que tienes una ruta a un dominio, la gente enruta a través de ti (BGP leak)
      * puedes inspeccionar/modificar tráfico, y luego reenviar al dominio.
      * https://blog.cloudflare.com/bgp-leaks-and-crypto-currencies/

---

# El Internet abierto hace fácil para los atacantes recopilar información útil.
  * ¿Qué hosts están ejecutando software/protocolos vulnerables?
    * Sondeo:
      * Verificar si un sistema está escuchando en un puerto bien conocido.
      * Los protocolos/sistemas a menudo envían un mensaje de banner inicial.
    * nmap puede adivinar el OS midiendo varios detalles específicos de implementación.
      * [ Ref: http://nmap.org/book/man-os-detection.html ]
    * Usar DNS para buscar el hostname para una dirección IP; puede dar pistas.
  * ¿Qué hosts existen, ej. para explorar ataques indirectos o para recopilar botnets?
    * traceroute para encontrar enrutadores en el camino, para ataques BGP.

---

# ¿Cómo mejorar la seguridad en el núcleo?
  * Correcciones compatibles con protocolo a implementaciones TCP (y otros protocolos)
  * Firewalls.
    * Corrección parcial, pero ampliamente usada.
    * Problema: el adversario puede estar dentro de la red con firewall.
    * Problema: difícil determinar si un paquete es "malicioso" o no.
    * Problema: incluso para campos que están presentes (src/dst), difícil de autenticar.
  * Seguridad criptográfica sobre TCP/IP: SSL/TLS, Kerberos, SSH, etc.
    * Un problema difícil: diseño de protocolo, distribución de claves, confianza, etc.
    * Hablaremos más sobre esto en la próxima clase sobre SSL.

