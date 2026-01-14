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

# Seguridad en Mensajería

---

# ¿Por qué estudiamos este tema?
  * La seguridad de mensajería importa en la práctica
  * Conocemos muchas técnicas por el problema acotado
  * Aún hay ideas nuevas y desafíos pendientes
  * No está resuelto: ver análisis de Zoom (Citizen Lab, 2020)

---

# Propiedades principales
  * Escenario: Alice envía mensaje M a Bob
  * Confidencialidad: solo Alice y Bob leen M
  * Autenticidad: Bob confirma que Alice lo envió
  * Hay más propiedades posibles (integridad, repudio, etc.)

---

# ¿Qué pasa con el correo electrónico?
  * Es antiguo e importante, esperaríamos alta seguridad
  * Camino típico incluye muchos actores confiables
    * Usuario, proveedor, listas, redirecciones, filtros, archivos
  * Cada salto involucra DNS y múltiples servidores
  * Un correo puede pasar por 10 o 20 hops

---

# Historia del e-mail
  * Originalmente sin seguridad criptográfica
  * Se han ido agregando opciones de seguridad gradualmente
  * Evolución lenta por la gran base instalada de software
    * Implementación hacia atrás

---

# Seguridad hop-by-hop desplegada
  * Protege enlaces individuales usuario-servidor y servidor-servidor
    * Start TLS, pero es oportunista
  * POP/IMAP sobre TLS evita espionaje y robo de buzones
  * DKIM firma mensajes por organización origen
    * Ayuda a detectar suplantaciones, se usa en decisiones de spam
  * BIMI/VMC autentican logos corporativos (certificados de marca)

---

# Limitaciones del enfoque hop-by-hop
  * No compone en seguridad de extremo a extremo
  * Es difícil garantizar TLS en todos los saltos
  * Cada servidor ve el mensaje en texto claro y puede modificarlo
  * Confidencialidad y autenticidad dependen de muchos operadores
  * Requiere configuraciones correctas y personal confiable

---

# Seguridad extremo a extremo
  * Depende solo de los usuarios y sus dispositivos finales
  * El remitente firma, el destinatario verifica; intermediarios son irrelevantes
  * Difícil lograr seguridad “a prueba de balas”
  * Muchos servicios nuevos optan por este modelo
    * WhatsApp, iMessage, Keybase, Signal, etc.

---

# Marco
  * Tres ejes técnicos principales:
    * Establecimiento de confianza (intercambio de claves)
    * Protocolo de conversación (cifrado de mensajes)
    * Privacidad de transporte (metadatos)
  * Revisaremos ideas criptográficas básicas antes de cada eje

---

# Primitivas criptográficas
  * m = mensaje en texto plano
  * h = Hash(m)
  * tag = MAC(clave, m)
  * c = E(clave, m)  
  * m = D(clave, c)
  * Cifrado asimétrico: E(PK_Bob, m), D(SK_Bob, c)
  * Firma: Sign(SK_Alice, m), Verify(PK_Alice, m, sig)

---

# Mensaje único seguro (tipo PGP)
  * Objetivo: confidencialidad + autenticidad
  * Supongamos que conocen PK_Bob y PK_Alice
  * Alice calcula c = E(PK_Bob, m)
  * Calcula s = Sign(SK_Alice, c)
  * Envía c y s a Bob
  * Bob verifica Verify(PK_Alice, c, s) y descifra D(SK_Bob, c)

---

# Mensaje único: preguntas abiertas
  * ¿Es mejor firmar c o m?
  * El adversario podría reinyectar c y s (replay)
  * Siempre hay que intentar firmar lo más cercano al mensaje original que se pueda
  * Tenemos confidencialidad, pero no autenticación
  * También tenemos potenciales replay attacks

---

# Canal seguro simplificado
  * Objetivo: confidencialidad + autenticidad bidireccional
  * Similar a TLS con claves públicas y secretas
  * A -> B: E(PK_B, “A” -> “B” || randomA), Sign(SK_A, …)
  * B -> A: E(PK_A, “A” <- “B” || randomB), Sign(SK_B, …)
  * Comparten secreto randomA || randomB
  * Derivan claves Kx = Hash(randomA || randomB || x)
  * A -> B: E(K1, M), MAC(K2, M)

---

# Canal seguro simplificado
  * Objetivo: confidencialidad + autenticidad bidireccional
  * Similar a TLS con claves públicas y secretas
  * A -> B: E(PK_B, “A” || “B” || randomA), Sign(SK_A, …)
  * B -> A: E(PK_A, “A” || “B” || randomB), Sign(SK_B, …)
  * Comparten secreto randomA || randomB
  * Derivan claves Kx = Hash(randomA || randomB || x)
  * A -> B: E(K1, M), MAC(K2, M)

---

# Establecimiento de confianza
  * Necesitamos vincular identidades con claves públicas
  * Varios enfoques:
    * Cifrado oportunista
    * Trust on First Use (TOFU)
    * Intercambio fuera de banda
    * Servidor central de claves
    * Key Transparency, Keybase, etc.

---

# Cifrado oportunista
  * Cada parte envía su clave pública en claro al comenzar
  * Útil contra escuchas pasivos en redes honestas
  * Ineficaz ante un atacante activo que modifica las claves
  * Puede servir como mejora incremental en contextos riesgosos
  * Muy conveniente en términos de implementación

---

# Trust on First Use (TOFU)
  * Asume que la primera conexión es honesta
    * SSH -> known_hosts
  * El cliente “adhiere” la clave pública del contacto
  * Conveniente: sin acciones del usuario
  * Resiste atacantes pasivos y ataques nuevos
  * Débil ante adversarios persistentes o cambios de clave legítimos
  * Cambio legítimo aparece como advertencia “¿usar nueva clave?”

---

# Intercambio fuera de banda
  * Intercambiar claves en persona o por canal seguro externo
  * Verificar manualmente la clave fijada por TOFU
  * Muy seguro si se hace presencialmente
  * Poco práctico: la gente rara vez lo hace
  * Necesario repetir tras pérdida o renovación de dispositivos
  * Muchos sistemas ofrecen esta opción

---

# Interludio: Conveniencia vs seguridad
  * La usabilidad es crítica en mensajería
  * Si el sistema ultra seguro es impráctico, nadie lo usa
  * Recuperación de claves y dispositivos perdidos es difícil
  * Soluciones efectivas combinan criptografía y arquitectura

---

# Servidor central de claves
  * Objetivo: mejorar usabilidad evitando intercambios manuales
  * El servidor devuelve la clave pública del contacto
  * Riesgo: un servidor deshonesto puede entregar la clave del atacante
  * Necesitamos controles para reducir esa confianza

---

# Ejemplo: Apple iMessage (registro)
  * Dispositivo genera par de claves público/privado
  * Usuario se autentica con iCloud y registra PK en Apple
  * Solo el dispositivo conoce la clave privada
  * TLS protege el canal hacia los servidores de Apple

---

# iMessage: envío y amenazas
  * Alice pide la clave pública de Bob al servidor
  * Cifra y firma el mensaje, lo sube para que Bob lo reciba
  * Apple no posee la clave privada, no puede leer ni falsificar
  * Conveniente y maneja bien dispositivos nuevos o perdidos
  * Riesgos: 
    * Ataques basados en contraseña 
    * Servidor que devuelva PK de Eve

---

# Key Transparency
  * Meta: combinar servidor de claves con verificabilidad pública
  * El servidor mantiene un log público de actualizaciones de claves
    * Append only y en otra "ubicación"
  * Los dueños revisan que su clave registrada sea correcta
  * Los solicitantes verifican que la respuesta coincida con el log

---

# Key Transparency: detalles
  * Log registra eventos: “Bob añadió PK_x”, “Bob quitó PK_z”
  * Si el servidor devuelve PK_Eve:
    * Debe publicarlo en el log: Bob detecta y alerta
    * Si no, Alice verá que PK_Eve no está en el log
  * Desafíos técnicos: eficiencia, privacidad, evitar bifurcaciones (equivocación)

---

# Keybase: verificación social
  * Reduce la confianza en el servidor usando pruebas externas
  * Para cada usuario “Alice” almacena:
    * PK_Alice (claves privadas solo en dispositivos de Alice)
    * Registros que enlazan identidades en otros servicios
      * Ej. Sign(PK_Alice, “Soy alice177 en twitter”)

---

# Keybase: cómo valida el cliente
  * Bob obtiene de Keybase PK_Alice y pruebas de identidad
    * Llaves posteadas en redes sociales (u otros lugares públicos)
  * El cliente descarga las pruebas (tweets, repos, etc.)
  * Verifica que estén firmadas con PK_Alice
  * Pregunta al usuario “¿es la Alice correcta?”
  * Si Keybase intenta devolver PK_Eve, falla la verificación social

---

# Keybase: ataques y operación
  * Ataque posible: comprometer las cuentas de prueba (twitter, github)
  * Los clientes fijan (pin) la clave la primera vez
  * Actualizaciones seguras: Alice firma la nueva clave con la anterior
  * Bob acepta cambios si están firmados por la clave ya fijada
  * Usabilidad aceptable salvo en configuración inicial y revocaciones

---

# Seguridad de conversación
  * Cómo proteger mensajes una vez establecidas las claves correctas
  * Metas en tensión:
    * Autenticidad vs negabilidad
      * Básicamente que no queden pruebas
    * Confidencialidad vs capacidad de denunciar abusos
      * Porque nadie sabe quien eres!
  * Grupos presentan retos adicionales

---

# Secreto hacia adelante
  * Previene que grabaciones antiguas se descifren tras comprometer claves
  * Proceso simplificado:
    * Alice genera par de claves temporal
    * Envía PK_temp a Bob
    * Bob cifra M con PK_temp
    * Alice descifra y borra SK_temp permanentemente
  * Combinado con TLS u otros canales para autenticidad

---

# Secreto hacia adelante: implicancias
  * El atacante necesita SK_temp para leer mensajes grabados
  * La clave temporal no está en dispositivos comprometidos ni en la red
  * TLS modernos y WhatsApp/Signal usan variantes más robustas

---

# Autenticidad negable
  * Objetivo dual: convencer al destinatario, negar ante terceros
  * No usar firmas públicas: preferir MAC simétricos
  * Protocolo SKEME simplificado:
    * Bob elige clave aleatoria K
    * Envía E(PK_Alice, K)
    * Alice descifra K
    * Envía M y MAC(K, M)
    * Alice publica K al finalizar
  * Cualquiera puede generar los mismos artefactos después

---

# Deniable messaging en la práctica
  * Protocolos como OTR y Signal implementan versiones avanzadas
  * Permiten autenticidad entre pares sin prueba transferible
  * Útiles para proteger la privacidad frente a terceros

---

# Privacidad de transporte
  * Busca ocultar metadatos: quién habla con quién, cuándo
  * Costosa de lograr, muchos sistemas la minimizan
    * No hay buena solución
  * Modelos:
    * Servidor central
    * Onion routing (Tor)
    * Difusión o mixnets

---

# Servidor central
  * Adversario observa tráfico cliente-servidor sobre TLS
  * Cronograma de mensajes revela patrones de comunicación
  * No oculta quién usa el servicio ni la frecuencia

---

# Onion routing y Tor
  * Mensajes pasan por múltiples relays cifrados en capas
  * Mejora frente a un servidor único
  * Adversarios globales aún pueden correlacionar tiempos

---

# Alternativas más costosas
  * Difusión (broadcast) a todos los participantes
  * Mixnets que procesan lotes grandes de mensajes
  * Ambas tienen mayor latencia y complejidad operativa

---

# Resumen
  * La seguridad en mensajería combina criptografía y diseño de sistemas
  * No hay solución única que cumpla todos los objetivos
  * Las decisiones implican trade-offs entre seguridad y usabilidad

