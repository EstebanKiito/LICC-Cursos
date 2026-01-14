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

# Certificados

---

# Hoy: certificados web
  * Plan básico
  * Problemas que aparecieron
  * Evolución para arreglar fallas de seguridad

---

# Contexto original
  * Mediados de los 90: la web comercial recién comenzaba
  * Pocas personas creían que el comercio en línea sería importante
  * ¿La gente confiaría sus tarjetas de crédito a Internet?
  * Plan: cifrado SSL y certificados para generar confianza

---

# Punto de partida: una URL https
  * Quieres comprar en https://amazon.com
  * Debes enviar tu número de tarjeta de crédito
  * "https" indica al navegador usar HTTP dentro de TLS

---

# Recordemos SSL (simplificado)
  * C es el navegador, S es el servidor web
  * C --> S: conectar
  * C <-- S: PK_S
  * C --> S: Encrypt(PK_S, freshKey)
  * C <-> S: Encrypt(freshKey, datos)
  * Luego, HTTP/HTML normal dentro de SSL

---

# ¿Qué logra SSL sin certificado?
  * Conexión privada autenticada, pero ¿con quién?
  * ¿Qué pasa si el remitente de PK_S es el atacante?
  * TLS sobre TCP/IP inseguro permite interceptar tarjetas
  * El cifrado vale poco si no sabes con quién hablas
  * El cliente debe autenticar al servidor

---

# Necesitamos distribución de claves
  * El cliente debe verificar que PK_S sea realmente de amazon.com
  * Distribuir claves confiablemente es difícil
  * Hay varios enfoques
    * Certificados 
    * En persona (o equivalente)
  * SSL incluye el certificado del servidor para probar su clave pública

---

# ¿Qué contiene el certificado?
  * El navegador lo muestra al hacer clic en el candado
  * Nombre del sujeto: DNS del servidor (ej. amazon.com)
  * Clave pública del sujeto
  * Fecha de expiración (uno o dos años)
  * Identificador de la CA emisora
  * Firma de la CA sobre toda la información

---

# ¿Qué es una Autoridad Certificadora?
  * Organización confiable que valida la relación DNS -> clave pública
  * Obtener un certificado:
    * Amazon genera par de claves y protege la privada
    * Envía la clave pública y prueba de propiedad a la CA
    * La CA valida la prueba y puede rechazar si falla
    * Si todo bien, firma el certificado y se lo entrega a Amazon
    * Amazon lo usa hasta que expire (uno o dos años)

---

# ¿Qué hace el navegador con el certificado?
  * Realiza varias verificaciones:
    * Nombre del sujeto coincide con el URL
    * La CA es reconocida y su clave pública está instalada
    * La firma es válida con la clave de la CA
    * El certificado no ha expirado
    * No ha sido revocado
    * El servidor demuestra poseer la clave privada
  * Si todo pasa: muestra la página y un candado gris
  * Si algo falla: muestra error y bloquea la página

---

# ¿Cómo conocen los navegadores a las CAs?
  * Necesitan la clave pública de cada CA confiable
  * Hay docenas de CAs globales
  * El navegador o el sistema operativo incluye una lista de certificados raíz

---

# ¿Por qué no consultar a la CA en línea?
  * Un PKI en línea sería lento y frágil
    * Requiere ida y vuelta extra en Internet
    * El servidor de la CA puede estar caído o lento
    * Carga pesada sobre la CA
    * La CA podría registrar tus actividades
  * Con certificados, el servidor prueba su identidad sin depender de la CA en tiempo real

---

# Usuarios: el eslabón débil
  * Muchos no saben cuándo exigir el candado
  * No miran el candado ni el URL
  * Desconocen el nombre DNS esperado
  * Por eso funciona el phishing (ej. www.g00gle.com)
  * Sus preocupaciones no coinciden con lo que garantiza SSL
    * Preguntas como "¿este comercio es honesto?"
  * Los navegadores solían mostrar diálogos confusos
    * Hoy intentan bloquear más automáticamente

---

# Certificados EV (Extended Validation)
  * Buscan certificar confiabilidad, no solo dominio
  * La CA solo emite EV a representantes legítimos
  * El certificado incluye el nombre de la empresa y una marca EV
  * Los navegadores muestran un recuadro verde con el nombre
  * Poco efectivos: usuarios no distinguen la diferencia
  * Además, son costosos

---

# Certificados DV (Domain Validated)
  * Mucho más comunes
  * La CA verifica la propiedad del dominio con chequeos técnicos
    * Ej. colocar un nonce en un archivo o en registros DNS
  * Proceso automatizado, rápido y barato (Let's Encrypt)
  * Garantía limitada: solo confirma dueño del dominio
  * Protocolos estándar como ACME soportan este flujo

---

# Limitaciones de la validación DV
  * Depende de que DNS y enrutamiento IP funcionen bien
  * Pero los certificados buscaban resistir cuando un atacante controla la red
  * Aun así mitigan ataques locales en WiFi o LAN
  * Buenas CAs DV consultan desde múltiples ubicaciones
  * No existe prueba 100% fiable de identidad o propiedad
  * Si aparecen dos certificados (legítimo y atacante) necesitamos detección

---

# ¿Cómo ayudan los certificados contra ataques?
  * Intentas ir a https://amazon.com
  * El atacante redirige tus paquetes a su servidor
    * Puede interceptar vía WiFi/LAN o manipular DNS/rutas
  * El atacante puede mostrar el certificado real, pero no conoce la clave privada
    * La llave privada no hará match con el certificado.
  * Si usa un certificado para attacker.com, el navegador lo rechaza
  * Si envías el certificado de Amazon junto con la llave de Amazon vas a recibir la información, pero no vas a poder desencriptar.
  * Otros vectores: phishing, forzar HTTP, engañar a una CA descuidada
    * Pero aquí no te protegen los certificados

---

# ¿Qué garantiza realmente el candado?
  * El navegador muestra la URL actual
  * El candado significa que la CA cree que ese servidor posee el nombre del URL
  * Si deseas amazon.com y ves candado + URL correcto, es razonable ingresar tu contraseña
  * Si no revisas candado ni URL, el beneficio cae
  * SSL no dice "esta página es segura"
    * Solo asegura que hablas con el dueño del nombre DNS mostrado
  * Sitios grandes complican el cuadro (CDN, llaves compartidas)
  * Se requiere usuario informado y cuidadoso

---

# Cuando las CAs no son confiables
  * Tu navegador confía en docenas o cientos de CAs
  * Cualquier CA puede emitir un certificado para cualquier nombre
  * Útil cuando un dominio cambia de CA, pero riesgoso
  * Problemas:
    * CAs descuidadas pueden ser engañadas
    * Un atacante puede robar la clave privada de la CA
    * Empleados pueden ser sobornados o coaccionados

---

# ¿Por qué es grave un certificado falso?
  * Si obtengo un cert válido para "gmail.com" con mi propia clave privada
  * Si además intercepto o redirijo tráfico, puedo hacer MitM
  * El navegador mostrará el candado y la sesión parece legítima
  * Puedo reenviar credenciales y contenido al Gmail real
  * El usuario verá su bandeja, mientras yo leo todo en texto plano

---

# Incidentes reales
  * En 1996 estos riesgos parecían lejanos
  * En 2011 dos CAs emitieron certificados maliciosos (ej. google.com)
  * Algunos se usaron para interceptar tráfico de Gmail
  * Los certificados falsos pueden circular antes de ser detectados
  * La naturaleza offline dificulta descubrirlos salvo que se usen ampliamente
  * Estos ataques impulsaron defensas contra certificados falsos


---

# Defensas contra certificados falsos
  * Varias técnicas han sido propuestas y desplegadas
  * Objetivo: detectar cambios inesperados de llave o emisión fraudulenta

---

# Aproximaciones de key pinning
  * Detectan cambios de claves respecto de visitas previas
  * Ejemplo: Chrome incluye lista de CAs autorizadas para google.com
  * Pinning vía historial del navegador (TOFU)
    * Recuerda la clave pública y alerta ante cambios
    * ¿Qué pasa si el sitio cambia legítimamente de clave?
  * Pinning gestionado por el servidor (HPKP) mediante cabecera HTTP
    * Potente pero peligroso si se configura mal


---
<!--
# Registros CAA
  * El dueño del dominio le indica a la CA qué reglas seguir al emitir
  * No ayuda contra CAs corruptas, pero sí evita errores
  * Puede limitar qué CAs pueden emitir para un dominio

---
-->

# Certificate Transparency (CT)
  * Registro público de todos los certificados emitidos
    * Múltiples copias operadas por distintas organizaciones
  * Las CAs deben registrar cada certificado
  * Los navegadores rechazan certificados que no estén en el log
  * Dueños de certificados monitorean para detectar falsos
  * Obliga a CAs maliciosas a dejar rastros visibles
  * Menos propenso a errores que HPKP
  * Chrome exige entrada CT para la mayoría de certificados
---


# ¿Qué hacer si se detecta un certificado fraudulento?
  * Debe revocarse rápidamente

---

# Revocación: un problema difícil
  * ¿Qué pasa si amazon.com cambia de dueño o le roban la clave privada?
  * El certificado antiguo seguirá pareciendo válido
  * Expirar no ayuda: suele durar uno o dos años
  * Listas de Revocación de Certificados (CRL):
    * El sitio pide a la CA revocar
    * La CA publica una lista firmada de certificados revocados
    * El navegador debería descargarla y revisarla


---


# ¿Qué hacer si se detecta un certificado fraudulento?

  * El esquema CRL original es insuficiente
    * Servidores de revocación poco confiables
    * El navegador suele aceptar el cert si no puede contactar la CRL
    * Las listas pueden ser grandes

---

# Esquemas modernos de revocación
  * Navegadores distribuyen listas negras tras incidentes mayores
  * Protocolo de Online de Estado de Certificado (OCSP): el cliente siempre pregunta
    * Sigue siendo lento, poco fiable y filtra privacidad
  * OCSP stapling:
    * La respuesta OCSP firmada se adjunta en el handshake
    * Funciona como certificado de corta duración
    * Certificados modernos incluyen bandera "must staple"

---

# Resumen
  * SSL + certificados reducen el riesgo de espionaje y manipulación DNS
  * Diseñar certificados web seguros es complejo
    * No hay verdad absoluta sobre identidad
    * Difícil involucrar a los usuarios en la seguridad
    * Las CAs solo validan propiedad de dominio
    * No todas las CAs son totalmente confiables
    * La revocación sigue siendo un punto débil

---

# Referencias adicionales
  * http://www.imperialviolet.org/2012/07/19/hope9talk.html

