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

# Asegurando interfaces: sandboxing de bibliotecas

---

# Objetivo: sandboxing de bibliotecas en aplicaciones grandes (ej., Firefox)
  * Las bibliotecas podrían tener errores de seguridad
  * Queremos asegurar que los errores de biblioteca no se traduzcan en vulnerabilidades de aplicación
  * Podríamos no obtener datos significativos de la biblioteca pero queremos evitar ataques
  * Necesitamos aislamiento + compartir controlado con la biblioteca
  * Solución: RLBox

---

# Nuevo problema: securitizar la interfaz
  * Ya sabemos cómo aislar código bastante bien
    * Procesos, VMs, WebAssembly
    * El paper usa WebAssembly, Native Client (predecesor de WebAssembly), y procesos
  * Un gran enfoque en este paper es diseñar la interfaz entre cajas aisladas

---

# Aparte: vemos algunas de las ideas de separación de privilegios en contexto del lado del cliente
  * Hasta ahora hemos hablado de código del lado del servidor (Google, OKWS, Firecracker)
  * RLBox muestra ideas similares siendo usadas en código del lado del cliente, en un navegador web
  * Aunque las ideas centrales son aplicables en general
    * Podríamos imaginar usar RLbox en contexto del lado del servidor también
    * Ej., sandboxing codecs de video en servidores de Youtube

---

# Antecedentes: aislamiento de navegador web
  * Hablaremos más sobre seguridad web después, pero podemos discutir lo básico
  * Diseño típico: proceso renderer para cada ventana / pestaña
    * El objetivo es prevenir que vulnerabilidades del navegador comprometan el SO subyacente
    * Solía ser relativamente más importante cuando el navegador era solo una de muchas apps
    * Hoy en día la mayoría de las cosas corren en el navegador, no tantas apps no-navegador que importen
    * Los compromisos podrían quizás acceder a todas las cookies del usuario
    * Cualquier sitio web podría estar en cualquier pestaña como imagen, frame, etc

---

# Aislamiento de sitio
  * Enfoque relativamente más nuevo en Firefox, Chrome
    * [[ Ref: https://www.chromium.org/Home/chromium-security/site-isolation/ ]]
  * Proceso por dominio (como google.com)
  * El atacante aún puede ser bastante dañino
    * Solo necesita inyectar una imagen que se renderice con biblioteca con errores en google.com
    * Ej., enviar imagen como adjunto de email, subir imagen a Google Maps, Google Photos, etc
    * El código de biblioteca comprometido puede acceder a cookie de google.com

---

# Proceso de media sandboxeado, en Firefox

  * Poner codecs de media en un proceso (único) separado
  * Desventaja: todos los codecs de media comparten el mismo proceso, un compromiso puede afectar otros codecs
  * No funciona tan bien para sandboxear bibliotecas relativamente más importantes
  * Ej., ¿qué pasa si esa biblioteca gzip corre en el mismo sandbox que un codec de video comprometido?
    * El adversario puede hacer que la biblioteca gzip descomprima a salida JS arbitraria
    * Causar que el renderer de página web ejecute código Javascript arbitrario en esa página

---

# Objetivo: combinar separación de privilegios existente con sandboxing de bibliotecas
  * Aún otro nivel de separación de privilegios, dentro del proceso renderer
  * La biblioteca debería tomar datos, producir versión renderizada
  * Codecs de imagen, codecs de video, bibliotecas de fuentes, biblioteca de descompresión, etc
  * Buena opción para separación de privilegios: especificación bastante limpia
    * Acepta datos arbitrarios, los decodifica en algún otro formato de datos
    * Casi puramente funcional
    * Sin almacenamiento persistente, sin dependencia entre decodificación de diferentes archivos

---

# ¿Cuántos sandboxes?
  * Crear sandbox aún incurre algún overhead (1-2 msec)
  * Un sandbox para todo el renderer: no es genial porque algo del contenido es importante
    * Ej., la biblioteca gzip podría descomprimir Javascript que corre en una página
  * El paper amortiza el costo agrupando por biblioteca, tipo de contenido, y de dónde vino el contenido
    * <renderer, biblioteca, origen-contenido, tipo-contenido>

---

# ¿Por qué la interfaz es un desafío?
  * Hasta cierto punto siempre va a ser complicado
  * Pero en gran medida este problema surge porque estamos reutilizando límite existente
  * La interfaz aplicación-biblioteca no fue diseñada originalmente para ser no confiable
  * La aplicación necesita preocuparse por qué datos podría estar dando a la biblioteca
  * La aplicación necesita validar datos que vienen de la biblioteca

---

# Ejemplos de errores: sección 3

---

# No sanitizar datos que vienen de la biblioteca (sandbox)
  * Ejemplo: la biblioteca pide saltar N bytes de datos de entrada
  * El código existente probablemente no verifica que N esté en límites (la biblioteca es confiable)
  * La biblioteca comprometida en sandbox puede pedir N mucho más grande que el tamaño del buffer
    * Causar lecturas o escrituras de memoria fuera de límites en código fuera del sandbox
  * Otro ejemplo: la biblioteca retorna un código de error o flag inesperado

---

# Conversiones de punteros
  * El código en la aplicación (renderer) y biblioteca (sandbox) tienen memorias diferentes
  * Los punteros en una memoria son sin sentido en otra memoria
  * Necesitamos copiar explícitamente el contenido de memoria -- no podemos solo pasar punteros existentes
  * ¿Qué sale mal?
    * El código de biblioteca o código de app se rompe (corrompe memoria): el puntero es basura
    * El código de biblioteca puede engañar al código de app para sobrescribir memoria arbitraria
    * La app puede filtrar inadvertidamente información ASLR a biblioteca no confiable en sandbox
      * El puntero podría no ser usado, así que no se captó en pruebas, y todo funciona
      * Pero la biblioteca comprometida puede mirar el puntero y extraer aleatoriedad ASLR

---

# Errores de doble-fetch
  * El código de app accede a los mismos datos compartidos dos veces
  * Ej., struct compartido; verificar si offset está en límites, luego usar ese offset
  * La biblioteca comprometida puede modificar el valor entre las dos verificaciones: condición de carrera

---

# Callbacks
  * La biblioteca podría necesitar hacer callback a la aplicación: ej., obtener más datos de entrada
  * Necesitamos otorgar de forma segura a la biblioteca acceso a funciones callback específicas
  * No es seguro que la biblioteca llame cualquier función en la aplicación
  * Pero la API existente solo pasa un puntero de 64 bits para especificar callback

---

# Argumentos de callback
  * A menudo las interfaces de biblioteca involucran que la biblioteca pase algo de estado de vuelta a función cb
    * Ej., puntero a alguna estructura de datos a nivel de app
  * La biblioteca comprometida puede pasar puntero arbitrario
  * Podríamos incluso necesitar restringir los argumentos a esas funciones callback

---

# Timing de callback
  * La aplicación podría no estar esperando un callback en algún punto de su ejecución
  * Ej., podría esperar que la biblioteca invoque callback de error solo después de que ocurra el error

---

# Callbacks vs hilos
  * Podríamos esperar ciertos callbacks en ciertos hilos
  * Ej., dos hilos llaman biblioteca, biblioteca corre cb de un hilo en otro hilo
    * O mismo cb de un hilo en ambos hilos
  * Podría llevar a corrupción de memoria de aplicación, condiciones de carrera, etc

---

# Mecanismos para ayudar a desarrolladores: sección 4

---

# Valores "tainted" (contaminados)
  * Intuición: valores tainted representan cosas que están en el sandbox, no confiables
    * Valores untainted están fuera del sandbox, confiables
    * No podemos pasar valores untainted al sandbox, o usar valores tainted fuera del sandbox
    * Necesitamos verificaciones explícitas para deshacerse de "taint"
    * En algunos casos necesitamos también convertir explícitamente a valores "tainted"
  * Operadores aritméticos y otros funcionan en valores tainted pero mantienen taint
  * No podemos realizar operaciones en valores tainted que tengan efectos secundarios
    * Ej., if (tainted_bool || foo()) invocará foo() solo si tainted_bool es falso

---

# Valores "tainted" (cont.) - Estructuras

<style scoped>
    pre {
    width: 70%;
    margin: 0 auto;
}
</style>

```
tainted<int> t_width  = sandbox_invoke(jpeg_sbx, get_width);
tainted<int> t_height = sandbox_invoke(jpeg_sbx, get_height);

// You cannot use t_width or t_height as normal ints:
int width = t_width;   // ❌ compile error
int height = t_height; // ❌ compile error

// Instead, you must validate them first:
int safe_width  = t_width.copy_and_verify([](int w) {
    return (w > 0 && w < 10000) ? w : 0;
});
int safe_height = t_height.copy_and_verify([](int h) {
    return (h > 0 && h < 10000) ? h : 0;
});

resize_canvas(safe_width, safe_height); // ✅ safe to use

```


---

# Valores "tainted" (cont.) - Estructuras
  * En principio el recorrido de struct también rastrea taint
    * struct foo { int x; int y; }
    * Podemos tomar un tainted<struct foo> y acceder al campo x
    * El resultado es un tainted<int>
    * Parece que el soporte de struct es débil en RLbox, pero "debería" funcionar así
  * Punteros tainted representan punteros a memoria del sandbox
    * En contraste, punteros regulares son punteros a memoria de aplicación
    * Necesitamos asignar explícitamente memoria en sandbox, obtener tainted<T*> de vuelta
    * Necesitamos copiar explícitamente memoria; no podemos solo convertir entre T* y tainted<T*>

---

# Desenvolver con un validador
  * Específico de aplicación, el desarrollador debe pensar qué es necesario
  * Ej., verificar que el status del decodificador de header JPEG es uno de los valores esperados
  * 
  ```
     tainted<int>.verify(
      [](int val) {
        if (val == ...) { 
          return val; 
        } else { 
          panic; 
        }
     });
  ```

---

# Congelamiento
  * Error de doble-fetch: consistencia entre valores a lo largo del tiempo
  * Mecanismo: declarar que algunos datos sean una unidad "freezable". Probablemente un struct
  * No se permite leer de un tipo freezable a menos que esté congelado
  * Congelarlo copia una instantánea de todo fuera del sandbox
  * Ahora no hay posibilidad de condiciones de carrera de doble-fetch

---

# Callbacks - Implementación técnica
  * Tecnicidad: WebAssembly no permite importar funciones adicionales en tiempo de ejecución
    * Solución: función trampolín
    * Función única importada del renderer al sandbox
    * El trampolín toma como argumento el callback específico que quieres llamar, y puntero args
    * El trampolín verifica si el callback es uno válido, y si es así, lo llama
  * Problema de seguridad: los callbacks podrían ser mal usados por el sandbox de alguna manera

---

# Restricciones en tipos de función callback
  * Aplicadas por register_callback()
  * Deben tomar argumentos tainted
    * (también toma un argumento al objeto sandbox)
  * Deben retornar resultado tainted (o void)
  * Vida del objeto callback: con scope o unregister explícito

---

# ¿Qué tan bien aborda RLbox sus objetivos?
  * Parece relativamente fácil de usar
  * 1-3 días-persona para sandboxear una biblioteca
  * Incremento de pocos cientos de LOCs: no tanto código
  * Suena como que los validadores son la parte más difícil: debe entender app, biblioteca

---

# ¿Cómo es el rendimiento después de sandboxear bibliotecas con RLbox?

  * Overheads de CPU modestos (3% para SFI/NaCl, 13% para sandboxing de procesos)
    * El overhead de sandboxing parece relativamente pequeño comparado con costos generales
    * Tienen algunas optimizaciones para mitigar overhead de cambio de contexto
    * Pin proceso sandbox en otro core, spin-wait para solicitudes
  * Overheads de memoria modestos también
    * El compartir sandbox parece funcionar bien
    * Los sandboxes no son de larga duración, así que los costos de memoria no son a largo plazo

<!--
---

# El overhead crudo parece más significativo
  * 27% reducción de throughput para Apache mod_markdown (NaCl)
  * 27% reducción de throughput para bcrypt en Node.js (NaCl)
  * 85% overhead para libGraphite (wasm)
  * Lo que importa parece ser cruces de límite y código intensivo en CPU
    * Ambos probablemente serán optimizados a medida que las herramientas wasm maduren
    * Paper posterior sobre reducir overhead de cruce de límite, del mismo grupo
    * [[ Ref: https://cseweb.ucsd.edu/~dstefan/pubs/kolosick:2022:isolation.pdf ]]

---

# RLbox usado en producción en Firefox, parece ser una herramienta bien desarrollada
  * [[ Ref: https://github.com/plsyssec/rlbox_sandboxing_api/ ]]
  * [[ Ref: https://plsyssec.github.io/rlbox_sandboxing_api/sphinx/ ]]

---

# El código original para el paper difiere algo de la versión de producción
  * [[ Ref: https://github.com/shravanrn/LibrarySandboxing ]]
  * [[ Ref: https://github.com/shravanrn/rlbox_api ]]
  * Parece que el congelamiento de struct fue descartado en producción
-->
---

# ¿Hasta qué punto surgen problemas de interfaz similares si estamos hablando por la red?
  * Ej., RPCs entre componentes OKWS, servicios de Google, etc
  * Probablemente aún necesitamos ser cuidadosos sobre decodificar respuesta
  * Probablemente aún sería útil saber qué datos validar
    * Ej., código de status o respuesta de RPC debería ser uno válido
    * Tainting sería útil para identificar lugares para validación
  * Algunos desafíos en RLbox surgen de interacciones repetidas e invariantes implícitas
    * Ej., saber que el próximo callback debería avanzar algún puntero, etc
    * Ej., pasar punteros u offsets a datos que fueron enviados antes
    * Menos problema si RPC es solo un viaje de ida y vuelta
    * Pero podría tener problema similar si haciendo RPCs de streaming, llamadas repetidas, etc

---

# Otro contexto donde estos problemas surgen: enclaves / kernels de SO no confiables
  * Línea de trabajo separada sobre poner el kernel en un dominio de aislamiento separado
  * El kernel podría tener errores, pero incluso si el adversario toma control del kernel, no puede comprometer la app
  * El aislamiento está relativamente bien definido, y quizás factible
  * Desafío: ¿cómo usar la interfaz syscall de un SO comprometido?
    * Muchos de los mismos problemas que RLbox está enfrentando, a una escala aún mayor
    * Ej., invocamos open("foo.txt") y obtuvimos file descriptor 5 de vuelta; ¿está bien?
      * Deberíamos verificar que ningún otro archivo que teníamos abierto esté usando fd 5
      * De otra manera podríamos confundirnos
    * Ej., llamamos mmap() para asignar memoria y obtuvimos alguna dirección de vuelta; ¿está bien?
      * Deberíamos asegurar que esta no sea la dirección de alguna estructura de datos existente
      * ¡De otra manera podríamos ser engañados para escribir sobre alguna memoria existente!

---

# Análogo práctico de rlbox: verificación de punteros de usuario de Linux
  * [[ Ref: https://www.usenix.org/legacy/publications/library/proceedings/sec04/tech/full_papers/johnson/johnson_html/cquk.html ]]
  * [[ Ref: https://sparse.docs.kernel.org/en/latest/ ]]

---

# Resumen
  * Caso de estudio interesante de separación de privilegios / sandboxing en navegador
  * Complicado interactuar de forma segura entre componentes aislados
  * Particularmente difícil adaptar interfaces existentes a límites de seguridad
  * RLbox trata de extraer patrones comunes
  * Idea clave: flujo de datos a través de límite de aislamiento; asistencia en tiempo de compilación
    * Necesitamos validación antes de comenzar a usar datos que vinieron a través del límite
