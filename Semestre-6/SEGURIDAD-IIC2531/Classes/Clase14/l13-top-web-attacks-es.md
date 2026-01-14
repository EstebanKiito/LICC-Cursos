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

# Tema de hoy: vulnerabilidades más comunes
  * Veremos el top 10 de OWASP
    * Open Web Application Security Project
  * Llevan registro de las CWE
    * Common Weakness Enumerations

---

# Control de Acceso Roto
  * Violación del principio de privilegios mínimos o denegar por defecto, donde el acceso solo debería otorgarse para capacidades, roles o usuarios particulares, pero está disponible para cualquiera.

  * Evadir las verificaciones de control de acceso modificando la URL (manipulación de parámetros o navegación forzada), el estado interno de la aplicación, o la página HTML, o usando una herramienta de ataque que modifique las solicitudes de API.

  * Permitir ver o editar la cuenta de otra persona, proporcionando su identificador único (referencias inseguras a objetos directos)

  * Acceder a API sin controles de acceso para POST, PUT y DELETE.

---

# Control de Acceso Roto - Ejemplos

```
 https://example.com/app/accountInfo?acct=notmyacct

 pstmt.setString(1, request.getParameter("acct"));
 ResultSet results = pstmt.executeQuery( );

```

```
https://example.com/app/getappInfo
https://example.com/app/admin_getappInfo

```


---

# Control de Acceso Roto - Prevención
  * Excepto para recursos públicos, denegar por defecto.
  * Implementar mecanismos de control de acceso una vez y reutilizarlos en toda la aplicación.
  * Los controles de acceso del modelo deben hacer cumplir la propiedad de los registros en lugar de aceptar que el usuario pueda crear, leer, actualizar o eliminar cualquier registro.
  * Los requisitos únicos de límites comerciales de la aplicación deben ser aplicados por los modelos de dominio.
  * Registrar los fallos de control de acceso, alertar a los administradores 
  * Limitar la tasa de acceso a API y controladores para minimizar el daño de herramientas de ataque automatizadas.

---

# Fallo Criptográfico
  * ¿Se transmite algún dato en texto plano? Verificar todo el tráfico interno, ej., entre balanceadores de carga, servidores web o sistemas back-end.

  * ¿Se utilizan algoritmos o protocolos criptográficos antiguos o débiles por defecto o en código antiguo?

  * ¿Se están usando claves criptográficas por defecto, se generan o reutilizan claves criptográficas débiles, o falta la gestión o rotación adecuada de claves? ¿Se han incluido claves criptográficas en repositorios de código fuente?

  * ¿Se valida adecuadamente el certificado del servidor recibido y la cadena de confianza?

  * ¿Se ignoran, reutilizan o no se generan vectores de inicialización suficientemente seguros para el modo de operación criptográfico?

---

# Fallo Criptográfico - Ejemplos

  * Una aplicación encripta números de tarjetas de crédito en una base de datos usando encriptación automática de base de datos. Sin embargo, estos datos se desencriptan automáticamente cuando se recuperan, permitiendo que una vulnerabilidad de inyección SQL recupere números de tarjetas de crédito en texto plano.

  * La base de datos de contraseñas usa hashes sin sal o simples para almacenar las contraseñas de todos. Una vulnerabilidad de carga de archivos permite a un atacante recuperar la base de datos de contraseñas. Todos los hashes sin sal pueden ser expuestos con una tabla arcoíris de hashes pre-calculados. Los hashes generados por funciones hash simples o rápidas pueden ser descifrados por GPUs, incluso si estaban con sal.

---

# Fallo Criptográfico - Prevención

  * Clasificar los datos procesados, almacenados o transmitidos por una aplicación. Identificar qué datos son sensibles según las leyes de privacidad, requisitos regulatorios o necesidades comerciales.

  * No almacenar datos sensibles innecesariamente. Los datos que no se retienen no pueden ser robados.

  * Asegurarse de encriptar todos los datos sensibles en reposo.
    * Deshabilitar el caché para respuestas que contengan datos sensibles.

  * Asegurar que estén en uso algoritmos, protocolos y claves estándar actualizados y fuertes; usar gestión adecuada de claves.

  * Encriptar todos los datos en tránsito con protocolos seguros 
    * No usar protocolos heredados como FTP y SMTP para transportar datos sensibles.

  * Almacenar contraseñas usando funciones hash adaptativas y con sal fuertes con un factor de trabajo (factor de retraso), como Argon2, scrypt, bcrypt o PBKDF2.

---

# Inyección
  * Los datos proporcionados por el usuario no son validados, filtrados o sanitizados por la aplicación.

  * Se utilizan consultas dinámicas o llamadas no parametrizadas sin escape consciente del contexto directamente en el intérprete.

  * Se utilizan datos hostiles dentro de los parámetros de búsqueda de mapeo objeto-relacional (ORM) para extraer registros adicionales y sensibles.

  * Los datos hostiles se usan directamente o se concatenan. El SQL o comando contiene la estructura y datos maliciosos en consultas dinámicas, comandos o procedimientos almacenados.

---

# Inyección - Ejemplos

```
String query = "SELECT \* FROM accounts WHERE custID='" + request.getParameter("id") + "'";

http://example.com/app/accountView?id=' UNION SELECT SLEEP(10);--

```

---

# Inyección - Prevención

  * La opción preferida es usar una API segura, que evita usar el intérprete por completo, proporciona una interfaz parametrizada, o migra a herramientas de mapeo objeto-relacional (ORMs).

  * Usar validación positiva de entrada del lado del servidor. Esto no es una defensa completa ya que muchas aplicaciones requieren caracteres especiales, como áreas de texto o APIs para aplicaciones móviles.

  * Para cualquier consulta dinámica residual, escapar caracteres especiales usando la sintaxis de escape específica para ese intérprete.

---
# Diseño Inseguro
  * El diseño inseguro es una categoría amplia que representa diferentes debilidades, expresadas como "diseño de control faltante o ineficaz".
  
  * El diseño inseguro no es la fuente de todas las demás categorías de riesgo Top 10.
    * Hay una diferencia entre diseño inseguro e implementación insegura.
  * Diferenciamos entre fallas de diseño y defectos de implementación por una razón, tienen diferentes causas raíz y remediación.
    * Un diseño seguro aún puede tener defectos de implementación que conduzcan a vulnerabilidades que pueden ser explotadas.

---
# Diseño Inseguro - Ejemplos

  * Una cadena de cines permite descuentos para reservas grupales y tiene un máximo de quince asistentes antes de requerir un depósito. Los atacantes podrían modelar esta amenaza y probar si podían reservar seiscientos asientos y todos los cines a la vez en pocas solicitudes, causando una pérdida masiva de ingresos.

  * El sitio web de comercio electrónico de una cadena minorista no tiene protección contra bots dirigidos por revendedores que compran tarjetas gráficas de gama alta para revender en sitios web de subastas.

---
# Diseño Inseguro - Prevención

  * Requisitos y Gestión de Recursos. Recopilar y negociar los requisitos comerciales de una aplicación con el negocio, incluyendo los requisitos de protección relacionados con confidencialidad, integridad, disponibilidad y autenticidad.
  * El diseño seguro es una cultura y metodología que evalúa constantemente las amenazas y asegura que el código esté diseñado y probado de manera robusta para prevenir métodos de ataque conocidos.
    * El modelado de amenazas debe integrarse en las sesiones de refinamiento.
  * El software seguro requiere un ciclo de vida de desarrollo seguro, alguna forma de patrón de diseño seguro, metodología de camino pavimentado, biblioteca de componentes seguros, herramientas y modelado de amenazas.
---

# Configuración Insegura
  * Falta de endurecimiento de seguridad apropiado en cualquier parte de la pila de aplicaciones o permisos mal configurados. 

  * Se habilitan o instalan características innecesarias (ej., puertos, servicios, páginas, cuentas o privilegios innecesarios).

  * Las cuentas predeterminadas y sus contraseñas siguen habilitadas y sin cambios.

  * El manejo de errores revela rastreos de pila u otros mensajes de error demasiado informativos a los usuarios.

  * Para sistemas actualizados, las características de seguridad más recientes están deshabilitadas o no configuradas de forma segura.

  * La configuración de seguridad en los servidores de aplicaciones, marcos de aplicaciones, bibliotecas, bases de datos, etc., no están configuradas con valores seguros.
  

---

# Configuración Insegura - Ejemplos
  * El servidor de aplicaciones viene con aplicaciones de ejemplo que no se eliminaron del servidor de producción las cuales tienen fallas de seguridad conocidas que los atacantes usan para comprometer el servidor. 
    * Supongamos que una de estas aplicaciones es la consola de administración y las cuentas predeterminadas no fueron cambiadas. 

  * El listado de directorios no está deshabilitado en el servidor. El atacante encuentra y descarga las clases Java compiladas, que descompilan e invierten para ver el código. El atacante luego encuentra una falla severa de control de acceso en la aplicación.

  * La configuración del servidor de aplicaciones permite que se devuelvan mensajes de error detallados a los usuarios, ej., stack traces. 

---

# Configuración Insegura - Prevención
  * Los entornos de desarrollo, QA y producción deben configurarse de manera idéntica, con diferentes credenciales utilizadas en cada entorno. Este proceso debe automatizarse para minimizar el esfuerzo requerido para configurar un nuevo entorno seguro.

  * Una plataforma mínima sin características, componentes, documentación y ejemplos innecesarios. Eliminar o no instalar características y marcos no utilizados.

  * Una tarea para revisar y actualizar las configuraciones apropiadas para todas las notas de seguridad, actualizaciones y parches como parte del proceso de gestión de parches.

  * Una arquitectura de aplicación segmentada proporciona separación efectiva y segura entre componentes o inquilinos, con segmentación, containerización o grupos de seguridad en la nube (ACLs).

---

# Componentes Vulnerables y Desactualizados
  * Si no conoces las versiones de todos los componentes que usas (tanto del lado del cliente como del servidor).
    * Esto incluye componentes que usas directamente así como dependencias anidadas.

  * Si el software es vulnerable, no tiene soporte o está desactualizado. Esto incluye el OS, servidor web/aplicación, sistema de gestión de bases de datos (DBMS), etc.

  * Si no escaneas vulnerabilidades regularmente y no te suscribes a boletines de seguridad relacionados con los componentes que usas.

  * Si no corriges o actualizas la plataforma subyacente, frameworks y dependencias de manera oportuna basada en riesgo. 

  * Si los desarrolladores de software no prueban la compatibilidad de bibliotecas actualizadas, mejoradas o parcheadas.
  
---

# Componentes Vulnerables y Desactualizados - Ejemplos
  * Los componentes típicamente se ejecutan con los mismos privilegios que la aplicación misma, por lo que las fallas en cualquier componente pueden resultar en un impacto serio.
    * Tales fallas pueden ser accidentales (ej., error de codificación) o intencionales (ej., una puerta trasera en un componente). 

    * CVE-2017-5638, una vulnerabilidad de ejecución remota de código de Struts 2 que habilita la ejecución de código arbitrario en el servidor, ha sido culpada por brechas significativas.

  * Hay herramientas automatizadas para ayudar a los atacantes a encontrar sistemas sin parches o mal configurados. 
    * Por ejemplo, el motor de búsqueda Shodan IoT puede ayudarte a encontrar dispositivos que aún sufren de la vulnerabilidad Heartbleed parcheada en abril de 2014.

---

# Componentes Vulnerables y Desactualizados - Prevención
  * Debe haber un proceso de gestión de parches para:

    * Eliminar dependencias no utilizadas, características, componentes, archivos y documentación innecesarios.

    * Inventariar continuamente las versiones de componentes tanto del lado del cliente como del servidor y sus dependencias usando herramientas como versions, OWASP Dependency Check, retire.js, etc.
      * Monitorear fuentes como Common Vulnerability and Exposures (CVE) y National Vulnerability Database  

    * Solo obtener componentes de fuentes oficiales sobre enlaces seguros. Preferir paquetes firmados.

    * Monitorear bibliotecas y componentes que no se mantienen o no crean parches de seguridad para versiones antiguas. 

---

# Fallos de Identificación y Autenticación
  * Permite ataques automatizados como credential stuffing, donde el atacante tiene una lista de nombres de usuario y contraseñas válidos.

    * Permite ataques de fuerza bruta u otros ataques automatizados.

  * Permite contraseñas predeterminadas, débiles o conocidas, como "Password1" o "admin/admin".

  * Usa procesos de recuperación de credenciales y olvido de contraseña débiles o ineficaces, como "respuestas basadas en conocimiento".

  * Tiene autenticación multifactor faltante o ineficaz.

  * Expone el identificador de sesión en la URL.

  * No invalida correctamente los IDs de sesión durante el cierre de sesión o un período de inactividad.

---

# Fallos de Identificación y Autenticación - Ejemplos
  * Credential stuffing, el uso de listas de contraseñas conocidas, es un ataque común.

  * La mayoría de los ataques de autenticación ocurren debido al uso continuo de contraseñas como único factor. 
    * Una vez consideradas mejores prácticas, la rotación de contraseñas y los requisitos de complejidad alientan a los usuarios a usar y reutilizar contraseñas débiles. 

  * Los timeouts de sesión de la aplicación no están configurados correctamente. Un usuario usa una computadora pública para acceder a una aplicación. En lugar de seleccionar "cerrar sesión", el usuario simplemente cierra la pestaña del navegador y se va. Un atacante usa el mismo navegador una hora después, y el usuario sigue autenticado.

---

# Fallos de Identificación y Autenticación - Prevención
  * Cuando sea posible, implementar autenticación multifactor para prevenir ataques automatizados de credential stuffing, fuerza bruta y reutilización de credenciales robadas.

  * No enviar o desplegar con credenciales predeterminadas, particularmente para usuarios administradores.

  * Implementar verificaciones de contraseñas débiles, como probar contraseñas nuevas o cambiadas contra la lista de las 10,000 peores contraseñas.

  * Asegurar que los caminos de registro, recuperación de credenciales y API estén endurecidos contra ataques de enumeración de cuentas usando los mismos mensajes para todos los resultados.

---

# Fallos de Identificación y Autenticación - Prevención

  * Limitar o retrasar progresivamente los intentos de inicio de sesión fallidos, pero tener cuidado de no crear un escenario de denegación de servicio.
    * Registrar todos los fallos y alertar a los administradores cuando se detecten credential stuffing, fuerza bruta u otros ataques.

  * Usar un gestor de sesiones integrado, seguro y del lado del servidor que genere un nuevo ID de sesión aleatorio con alta entropía después del inicio de sesión. 
    * El identificador de sesión no debe estar en la URL, debe almacenarse de forma segura y invalidarse después de cierre de sesión, inactividad y timeouts absolutos.

---

# Fallos de Integridad de Software y Datos
  * Los fallos de integridad de software y datos se relacionan con código e infraestructura que no protege contra violaciones de integridad.
  * Un ejemplo de esto es cuando una aplicación depende de bibliotecas de fuentes no confiables.
    * Una canalización CI/CD insegura puede introducir el potencial de acceso no autorizado, código malicioso o compromiso del sistema.
  * Muchas aplicaciones ahora incluyen funcionalidad de auto-actualización, donde las actualizaciones se descargan sin verificación de integridad suficiente y se aplican a la aplicación previamente confiable.
  * Otro ejemplo es cuando objetos o datos se codifican o serializan en una estructura que un atacante puede ver y modificar es vulnerable a deserialización insegura.

---

# Fallos de Integridad de Software y Datos - Ejemplos
  * Actualización sin firma: Muchos routers domésticos, firmware de dispositivos y otros no verifican actualizaciones mediante firmware firmado. Este es un objetivo creciente para los atacantes.
    * Muchas veces no hay mecanismo para remediar excepto arreglar en una versión futura y esperar a que las versiones anteriores envejezcan.

  * Actualización maliciosa de SolarWinds: Se sabe que los estados-nación han atacado mecanismos de actualización. La empresa que desarrolla el software tenía procesos seguros de construcción e integridad de actualización.
    * Aún así, estos pudieron ser subvertidos, y durante varios meses, la empresa distribuyó una actualización maliciosa altamente dirigida a más de 18,000 organizaciones, de las cuales alrededor de 100 fueron afectadas.

---

# Fallos de Integridad de Software y Datos - Ejemplos
  * Deserialización Insegura: Una aplicación React llama a un conjunto de microservicios Spring Boot.
    * Siendo programadores funcionales, trataron de asegurar que su código sea inmutable.
    * La solución que idearon es serializar el estado del usuario y pasarlo de un lado a otro con cada solicitud.
    * Un atacante nota la firma del objeto Java "rO0" (en base64) y usa la herramienta Java Serial Killer para obtener ejecución remota de código en el servidor de aplicaciones.

---

# Fallos de Integridad de Software y Datos - Prevención
  * Usar firmas digitales o mecanismos similares para verificar que el software o datos provienen de la fuente esperada y no han sido alterados.

  * Asegurar que las bibliotecas y dependencias, como npm o Maven, consuman repositorios confiables. Si tienes un perfil de riesgo más alto, considera alojar un repositorio interno conocido-bueno que esté verificado.

  * Asegurar que se use una herramienta de seguridad de cadena de suministro de software para verificar que los componentes no contengan vulnerabilidades conocidas.

  * Asegurar que haya un proceso de revisión para cambios de código y configuración.

---

# Fallos de Integridad de Software y Datos - Prevención

  * Asegurar que tu canalización CI/CD tenga segregación, configuración y control de acceso apropiados para asegurar la integridad del código que fluye a través de los procesos de construcción y despliegue.

  * Asegurar que los datos serializados sin firmar o sin encriptar no se envíen a clientes no confiables sin alguna forma de verificación de integridad o firma digital para detectar manipulación o reproducción de los datos serializados.

---

# Fallos de Logs y Monitoreo de Seguridad
  * Los eventos auditables, como inicios de sesión, inicios de sesión fallidos y transacciones de alto valor, no se logean.

  * Los errores generan mensajes de registro nulos, inadecuados o poco claros.

  * Los registros de aplicaciones y APIs no se monitorean para actividad sospechosa.

  * Los registros solo se almacenan localmente.

  * Los procesos de escalación de respuesta no están en su lugar o no son efectivos.

  * La aplicación no puede detectar, escalar o alertar sobre ataques activos en tiempo real o casi tiempo real.

  * Eres vulnerable a inyecciones o ataques en los sistemas de registro o monitoreo si los datos de registro no están codificados correctamente.

---

# Fallos de Logs y Monitoreo de Seguridad - Ejemplos
  * El operador del sitio web de un proveedor de plan de salud infantil no pudo detectar una brecha debido a la falta de monitoreo y logs.
    * Una parte externa informó al proveedor del plan de salud que un atacante había accedido y modificado miles de registros de salud sensibles de más de 3.5 millones de niños.
    * Como no había logs o monitoreo del sistema, la brecha de datos pudo haber estado en progreso desde 2013, un período de más de siete años.

---

# Fallos de Logs y Monitoreo de Seguridad - Prevención
  * Asegurar que todos los fallos de inicio de sesión, control de acceso, etc. puedan logearse con suficiente contexto de usuario para identificar cuentas sospechosas y mantenerse durante suficiente tiempo para permitir análisis forense retrasado.

  * Asegurar que los logs se generen en un formato que las soluciones de gestión de logs puedan consumir fácilmente.

  * Asegurar que los datos de logs estén codificados correctamente para prevenir inyecciones o ataques en los sistemas de registro o monitoreo.

  * Asegurar que las transacciones de alto valor tengan un rastro de auditoría con controles de integridad para prevenir manipulación o eliminación.

  * Establecer o adoptar un plan de respuesta y recuperación de incidentes.  


---

# Los Almost
  * Calidad de Código
  * DDoS
  * Manejo de Memoria



