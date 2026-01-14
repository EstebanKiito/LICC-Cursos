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

# Seguridad Web

---

# Tema de hoy: aislamiento entre sitios en un navegador web
  * El plan general se llama la "política del mismo origen" (SOP)
  * Un caso de estudio de políticas de seguridad del mundo real
  * Una mezcla:
    * Principios
    * Compromisos con compatibilidad, conveniencia

---

# ¿Por qué hay un problema?
  * ¡Tu navegador sigue instrucciones proporcionadas por atacantes!
  * La mayoría de nosotros seguimos enlaces a sitios web que no conocemos mucho
    * Y así probablemente vemos sitios web maliciosos
  * Nuestros navegadores ejecutan HTML, JavaScript de sitios web maliciosos
  * Buenas noticias: el navegador no permite que JavaScript lea tus archivos locales, etc
    * Es decir, el navegador ejecuta JavaScript en un sandbox
    * Así que las páginas web solo pueden pedir al navegador hacer cosas relacionadas con web
  * Malas noticias: algunas cosas relacionadas con web pueden ser bastante dañinas

---

# ¿Qué podría salir mal si los navegadores web no fueran cuidadosos?
  * (Estos generalmente no funcionan ahora, pero a menudo solían hacerlo)
  * ¿Leer mis datos privados de sitios web, ej. email?
  * ¿Publicar cosas como yo?
  * ¿Actuar como yo en el sitio web de mi banco?
  * ¿Mirar sitios web dentro del firewall de la universidad?
  * ¿Mirar datos en otras ventanas del navegador?
  * ¿Cambiar información mostrada en otras ventanas del navegador?

---

# ¿Qué ha hecho que asegurar navegadores sea una historia larga y compleja?
  * ¡Inicialmente no parecía haber ningún problema de seguridad en absoluto!
    * La web era texto estático e imágenes, nada sensible
    * JavaScript fue un gran cambio
    * Sitios web sensibles (comercio, bancos, email, etc) fue un gran cambio
  * Evolución rápida en usos y características:
    * Los riesgos de seguridad a menudo no son aparentes hasta mucho después
    * Los diseños iniciales a menudo difíciles de asegurar, y difíciles de cambiar
    * Así que la seguridad a menudo retrofitada
  * La compatibilidad con sitios web antiguos y navegadores antiguos es importante
    * Los usuarios se preocupan más por la conveniencia que por la seguridad

---

# ¿Qué ha hecho que asegurar navegadores sea una historia larga y compleja? (cont.)
  * Compatibilidad y llegada tardía de seguridad ->
    * A menudo implementado al lado
    * Explícito en JS y código de servidor habría sido mejor
  * Muchos navegadores, mecanismos de estándares débiles
    * Lento para obtener consenso sobre cómo debería funcionar la seguridad
  * Mucho compartir entre sitios web, así que el aislamiento estricto no es realista
    * Mash-ups, APIs, anuncios, botones "Like", etc

---

# Modelo de amenaza / suposiciones
  * (-) El atacante controla un sitio web, attacker.com
  * (-) Visitas el sitio web del atacante
    * Ej. attacker.com == dog-photos.com
  * (-) Estás usando el navegador para otras cosas (email, banco, etc)
  * (+) El navegador es confiable, así que podemos diseñarlo para contener ataques
  * (+) El navegador no tiene errores de implementación (ej., buffer overflows)
  * (?) Para esta clase, asumir que la red es segura (hablaremos de HTTPS después)

---

# Solución: la Política del Mismo Origen (SOP)
  * SOP es impuesta por el navegador en las páginas web
  * El navegador etiqueta cada script (HTML, JS) con un origen
    * Origen = el servidor web del que vino la página (o frame)
    * protocolo + nombre de host + puerto
    * Ej. el origen de https://foo.com/x/y/z es https://foo.com:443
      * Todas las páginas en un servidor dado comparten un origen
  * El navegador etiqueta cada recurso con un origen también
    * Recurso = servidor de red, página mostrada, variable JS, etc
  * La regla SOP:
    * Un script solo puede acceder a un recurso si tienen el mismo origen
    * El script se ejecuta en nombre de algún origen
    * Unidad de aislamiento: iframe (ya sea ventana/pestaña de nivel superior, o iframe embebido)

---

# Solución: la Política del Mismo Origen (SOP) (cont.)
  * Dos vistas de SOP:
    * Impone aislamiento
    * Autoriza algo de compartir

---

# Ejemplo: XMLHttpRequest()
  * XMLHttpRequest(url) es una llamada JavaScript
  * Obtiene URL y permite a JavaScript ver el resultado
  * A menudo usado para acceder a "web APIs", para obtener datos para JS
  * ¿Podría attacker.com usarlo para robar datos de gmail?
    * No: el navegador impone SOP, así que solo puede obtener del mismo servidor del que vino el JavaScript

---

# ¿El SOP hace lo que queremos?
  * Es mayormente impuesto automáticamente, sin elección 
    * Así que es importante que corte ordenadamente el límite entre
    * "siempre OK" y "nunca OK"
  * Previene que JS de attacker.com hable con gmail o mi banco,
    * o sitios web internos de mi red
    * Es decir, con XMLHttpRequest()
  * Previene que JS del atacante mire mis otras ventanas, o las cambie
  * El atacante probablemente puede engañarme para hacer clic en gmail.com
    * Pero entonces el navegador está ejecutando HTML/JS de gmail, no del atacante

---

# ¿Cómo preservar el aislamiento del SOP sobre Internet?
  * ¿Cómo sabe la página que los datos de red son realmente de gmail.com?
    * ¿Y no del servidor del atacante?
    * Respuesta: TLS + certificado con nombre DNS
    * Profundizaremos en estos temas en próximas clases 
  * ¿Cómo sabe gmail.com que el comando es realmente de tu navegador?
    * ¿Y no de la máquina del atacante con navegador hackeado?
    * Respuesta: cookies

---

# Cookies
  * Permiten a los servidores mantener estado en el navegador
    * Para carrito de compras, rastreo de anuncios, autenticación de usuario, etc
  * Los sitios web pueden decir al navegador que establezca cookies
    * Set-Cookie: key=value
  * El navegador envía las cookies de un servidor de vuelta en cada solicitud
  * El sitio web puede especificar un dominio, ej. uc.cl
    * El dominio tiene que ser un sufijo (tal vez completo) del nombre DNS del sitio
    * El navegador envía cookies coincidentes en todas las solicitudes
    * Ej. una cookie con domain=google.com coincide con servidor mail.google.com

---

# Cookies (cont.)
  * Una configuración típica:
    * Cuando te logueas con contraseña, el servidor envía una cookie de ID de sesión
    * Set-Cookie: session=<sessionID> (un string hex largo)
    * Cuando el servidor ve solicitudes, busca sessionID en BD para encontrar usuario
    * ¡sessionID debe mantenerse secreto!
      * Aleatorio y largo para que sea difícil de adivinar
  * Javascript no puede ver cookies excepto como lo permite SOP

---

# Algunos problemas de cookies
  * Es un desastre que el navegador las envíe automáticamente
    * Arreglo potencial: cookies SameSite=Strict no enviadas con solicitudes de otro origen
    * Comportamiento sorprendente: hacer clic en enlace a Facebook muestra página de login de facebook
      * Porque las cookies de Facebook no se enviaron, ya que la solicitud se originó desde otro lugar
    * Workaround: cookies SameSite=Lax, enviadas con enlaces de otra página
      * Pero ahora de vuelta a tener una debilidad de seguridad (solo requiere que usuario haga clic en enlace)
    * Chrome ahora por defecto a SameSite=Lax
      * [[ Ref: https://www.chromium.org/updates/same-site/ ]]

---

# Algunos problemas de cookies (cont.)
  * Sobrescribir es un problema potencial:
    * ¿Puede attacker.com cambiar una cookie de google.com?
    * ¿Así que estoy logueado en google.com como atacante, no como yo?
    * ¿Así que el atacante ve mi historial de búsqueda?
    * La regla de sufijo ayuda aquí
    * ¡Pero no podemos permitir que attacker.com establezca una cookie para .com!
      * O cualquier otro dominio de nivel superior, ej. co.uk
      * El navegador debe tener lista de todos los dominios de nivel superior

---

# ¿Por qué la aplicación estricta de SOP no es el final de la historia?
  * Los desarrolladores deberían poder crear sitios "mash-up" que
    * combinen contenido de múltiples lugares
  * Ejemplo: Un sitio que combina datos de Google Map con datos de bienes raíces
  * Ejemplo: Anuncios
  * Ejemplo: Widgets de redes sociales (ej., el botón "like" de Facebook)
  * También compatibilidad con HTML pre-SOP

---

# Excepción SOP: enlaces ordinarios
  * Ej. una página attacker.com puede contener un enlace a gmail.com
    * Y tal clic navegará al usuario a gmail.com
  * ¿Por qué esta excepción?
    * Estos enlaces son una gran parte de cómo la gente encuentra cosas en la web
  * Usualmente los enlaces inter-dominio son inofensivos
  * PERO el navegador enviará cookies (si hay) a gmail.com
    * Así que el enlace se sigue como el usuario de gmail
    * Esto podría ser un problema si visitar el enlace tiene efectos secundarios

---

# Excepción SOP: IMG
  * La página attacker.com puede contener \<IMG SRC="https://foo.com/x.gif">
  * El navegador obtendrá y mostrará la imagen, a pesar de diferentes orígenes
  * ¿Por qué esta excepción?
    * Evitar muchas copias de imágenes comúnmente usadas
    * Permitir incorporación fácil de contenido de imagen
  * ¿Puede una página attacker.com robar contenido de esta manera?
    * Ej. usar fetch IMG e inspeccionar páginas web dentro del firewall de mi red?
    * No: el navegador impone SOP a los píxeles recuperados
    * El usuario ve la imagen, pero no la página attack.com
  * PERO el navegador enviará cookies para foo.com
    * Así que foo.com puede otorgar a la solicitud del atacante mis permisos
    * ¡Esto es un problema!

---

# Falsificación de Solicitud Cross-Site (CSRF)
  * Supongamos que una página de attacker.com contiene
    * \<IMG SRC="https://bank.com/xfer?amount=500&to=attacker">
  * El usuario no ve nada especial, tal vez una pequeña imagen rota
  * ¿Qué pasa si el usuario está logueado en bank.com?
  * ¡bank.com ve una solicitud de transferencia con una cookie de sesión válida!
  * CSRF ha sido una gran fuente de ataques reales
    * Una falla subyacente es la excepción al SOP
    * Otra falla es el envío automático de cookies
  * Término general es "confused deputy"
    * El navegador envía una solicitud a bank.com
    * El navegador *debería* decir que está reenviando una solicitud de attacker.com
    * Pero en realidad envía mi cookie, implicando que la solicitud es en nombre de mí o de una página web del banco

---

# ¿Cómo protegerse contra CSRF?
  * bank.com envía un token aleatorio con cada URL que genera
    * Ej. https://bank.com/xfer..&token=...
  * bank.com registra todos los tokens anti-CSRF legítimos
  * bank.com acepta solo una solicitud con un token legítimo no usado
    * asociado con el usuario solicitante
  * Esperemos que el atacante no pueda predecir o robar tokens

---

# Excepción SOP: SCRIPT
  * <SCRIPT SRC="https://foo.com/lib.js"></SCRIPT>
  * Carga y ejecuta JavaScript de cualquier lugar; SOP no impuesto
  * ¿Por qué esta excepción?
    * Para que la gente pueda usar bibliotecas JavaScript obtenidas de cualquier lugar
  * ¿Como qué origen debería ejecutarse el JS obtenido?
    * ¿Como origen = foo.com?
    * ¿Como origen = página que obtiene?
  * Los navegadores ejecutan con el origen de la página que obtiene
    * Intuición: como ejecutar código de biblioteca como parte de tu app
    * Así que debes ser cuidadoso sobre de dónde obtienes scripts

---

# Excepción SOP: IFRAME
  * Carga y muestra una página web en un rectángulo
    * La página enmarcada puede venir de cualquier lugar: SOP no impuesto en obtención
  * ¿Por qué esta excepción?
    * Usado para anuncios, botones "like" de Facebook, etc
  * Pero SOP *sí* se aplica a las acciones del frame una vez obtenido
    * Si los orígenes de la página principal y del frame son diferentes,
      * entonces SOP les previene interactuar en la mayoría de las formas
    * SOP defiende cada uno contra el otro, haciendo IFRAMEs bastante seguros
    * Y el IFRAME obtiene los derechos SOP de su origen, así que
      * puede ej. obtener datos de su servidor de origen
  * La página principal puede, sin embargo, navegar el frame vía JS

---

# Excepción SOP: Cross Origin Resource Sharing (CORS)
  * Un servidor puede decir al navegador permitir XMLHttpRequest(url) cross-origin
  * Si el navegador ve que la solicitud de una página es cross-origin, pregunta al servidor
    * primero, le dice al servidor el origen solicitante, el servidor puede decir sí o no
  * ¿Por qué esta excepción?
    * Algunos datos de API web son públicos
    * Algunos mash-ups específicos son intencionalmente autorizados
  * ¿Por qué la excepción es segura?
    * El propósito de SOP es defender al servidor
    * Si el servidor explícitamente no quiere ser defendido, eso está bien
    * Por defecto a "no" si el servidor no entiende
  * Este es un buen diseño, ya que es explícito sobre seguridad

---

# Aquí hay algunos ataques que funcionan alrededor del SOP

---

# Ataque Cross-site Scripting (XSS)
  * Considerar sitios que muestran comentarios de usuarios entre sí (ej., Facebook)
  * El atacante publica un comentario como este:
    * <SCRIPT> ... </SCRIPT>
  * Yo veo el comentario
  * Si el sitio no previno esto:
    * Ahora el código JavaScript del atacante está ejecutándose en mi navegador
    * ¿Es eso malo? Después de todo el navegador sandboxea JS
  * El problema real es que el código del atacante está ejecutándose con
    * el origen de la página circundante, ej. facebook.com
  * ¡El JS del atacante puede ver mi cookie de Facebook con ID de sesión!
    * Puede actuar como yo, o enviar mi cookie al atacante
  * Verán esto en el Laboratorio 4

---

# ¿Cómo defenderse contra ataques XSS?
  * Cookies HTTP-Only -- oculta cookie de todo JS
    * No es un arreglo completo, ya que el JS del atacante aún puede hacer otras cosas
      * como origen de la página, ej. enviar solicitudes al servidor como yo
  * El servidor podría quitar todo HTML de comentarios
    * Pero a los usuarios les gusta incluir formato, enlaces, etc
  * El servidor podría parsear cuidadosamente comentarios para prohibir ciertas etiquetas
    * Complicado pero a menudo hecho; ¡use una buena biblioteca!
  * Header HTTP Content-Security-Policy, un nuevo mecanismo
    * El servidor dice al navegador prohibir scripts inline
    * Así que el servidor no tiene que adivinar cómo el navegador parsea
  * ¿Pero qué pasa si el sitio web permite a los usuarios subir fotos?
    * El adversario podría subir código Javascript como su foto
    * Difícil obtener garantías de seguridad precisas con mecanismos retrofitados

---

# Ataque de Clickjacking
  * El navegador trata los clics de usuario como teniendo autoridad completa
  * Así que es vital que el usuario entienda las consecuencias de los clics
    * ¿Comprará algo en Amazon? ¿Enviará email? ¿"Like"?
  * Las pistas principales para la comprensión del usuario son visuales
    * Así que es vital que el layout de página haga claras las consecuencias del clic
  * Tristemente, HTML no siempre es útil asegurando pistas visuales claras

---

# Ataque de Clickjacking
  * Ejemplo:
    * La página attacker.com incluye IFRAME mostrando página amazon.com
      * Con un botón de pedido One-Click
    * attacker.com hace el IFRAME transparente (!)
      * <iframe style="opacity:0;" ...
    * attacker.com puede pintar en cualquier lugar de la página, incluyendo sobre IFRAME
      * Ej. "¡Haz clic aquí para un iPad gratis!"
    * Un clic compra el artículo en amazon; sin iPad gratis
    * El frame de amazon es invisible, así que el usuario no puede ver que algo raro pasó

---

# Ataque de Clickjacking (cont.)
  * Defensa:
    * Header X-Frame-Options: DENY -- prohibe página en IFRAME
    * Content-Security-Policy: frame-ancestors 'none'


---

# ¿Por qué no rediseñar el modelo de seguridad desde cero?
  * R1: ¡Compatibilidad hacia atrás! 
    * Hay una gran cantidad de infraestructura web preexistente en la que la gente confía
  * R2: ¿Cómo sabemos que un nuevo modelo de seguridad sería suficientemente expresivo?
    * Los usuarios no cambiarán mucha conveniencia por seguridad
  * R3: Cualquier modelo de seguridad debe evolucionar

---

# ¿Qué ideas podrían ir en un diseño mejorado?
  * Separar credenciales de usuario de otras cookies
    * Deberían obedecer reglas diferentes
  * Indicación explícita de qué principal usar
    * Sin autoridad ambiente
    * La página debería decir cómo debería ejecutarse JS extranjero
    * Todas las obtenciones deberían indicar explícitamente origen
      * y credenciales de usuario a usar
  * Requerir menos parsing, menos escaping
    * Ej. sin mezcla de JavaScript y HTML
  * Noción explícita de permisos -- política de control de acceso
  * Más claridad visual sobre en qué está a punto de hacer clic el usuario
    * ¿Quién está mostrando el botón? ¿A dónde irá?

---

# ¿La conclusión es "lío sin esperanza" o "complicado pero adecuado"?
  * El SOP previene un gran conjunto de ataques
  * Los mantenedores de navegadores son serios sobre arreglar problemas
    * Y trabajan juntos bastante para semi-estandarización
  * Frameworks como Django son útiles
    * Bibliotecas para cosas complicadas como parsing / quitar / escapar
    * Despliegue automático de mecanismos protectores

---

# Referencias
  * https://lchsk.com/stay-paranoid-and-trust-no-one-overview-of-common-security-vulnerabilities-in-web-applications.html

---

# Mejoras desde The Tangled Web:
  * https://infosec.mozilla.org/guidelines/web_security

  * Ejemplos notables:
    * Cookies Same-Site, ahora por defecto (https://www.chromium.org/updates/same-site/)
    * https://en.wikipedia.org/wiki/Content_Security_Policy
    * https://en.wikipedia.org/wiki/Cross-origin_resource_sharing
    * https://en.wikipedia.org/wiki/Strict_Transport_Security
    * https://www.w3.org/TR/SRI/
    * Atributo sandbox de iframe HTML5
      * https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe

---

# El aislamiento web (SOP) es usado para aislamiento de privilegios por apps web
  * Ej., Facebook (https://ysamm.com/?p=763)
  * Ej., googleusercontent.com de Google