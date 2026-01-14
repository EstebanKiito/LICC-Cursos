# Lab 3: Symbolic execution

Introducción
------------

Muchos exploits de seguridad se deben a bugs de software. Este laboratorio te introducirá a
una técnica poderosa para encontrar bugs en software: *ejecución simbólica*.
Esta puede ser una buena forma de auditar tu aplicación en busca de vulnerabilidades de seguridad para
que luego puedas corregirlas. Al final de este laboratorio, tendrás un sistema de
ejecución simbólica que puede tomar la aplicación web Zoobar y encontrar mecánicamente
entradas que disparan diferentes tipos de bugs en Zoobar que pueden llevar a vulnerabilidades
de seguridad. (Más precisamente, este laboratorio construirá un sistema de
ejecución concolic; explicaremos qué significa esto más adelante.)

El [artículo EXE](https://css.csail.mit.edu/6.858/2022/readings/exe.pdf) describe un sistema de
ejecución simbólica para programas en C. Por simplicidad, este laboratorio se enfocará
en construir un sistema de ejecución simbólica/concolica para programas en Python,
modificando objetos Python y sobrecargando métodos específicos. Mucho
como EXE, usaremos un solucionador SMT para verificar restricciones
satisfacibles y encontrar entradas de ejemplo para el programa que estamos probando.
(Como nota al margen, SMT significa [Satisfiability Modulo Theories](https://en.wikipedia.org/wiki/Satisfiability_Modulo_Theories), lo que significa que el solucionador puede verificar restricciones
que involucran tanto expresiones tradicionales de satisfactibilidad booleana como
restricciones que se refieren a otras "teorías" como enteros, vectores de bits,
cadenas, y así sucesivamente.)

En este laboratorio, primero te familiarizarás con el uso de Z3,
un solucionador SMT popular, usándolo para encontrar una forma correcta de calcular
el promedio sin signo (y con signo) de dos valores de 32 bits. Luego
crearás wrappers para operaciones enteras en Python (similar a como EXE proporciona
reemplazos para operaciones en valores simbólicos), e implementarás la lógica
central de invocar Z3 para explorar diferentes rutas de ejecución posibles.
Finalmente, explorarás cómo aplicar este enfoque a aplicaciones web,
que tienden a manejar cadenas en lugar de valores enteros. Envolverás
operaciones en cadenas Python, implementarás wrappers amigables a simbólicos alrededor
de la interfaz de base de datos SQLalchemy, y usarás el sistema resultante para encontrar
vulnerabilidades de seguridad en Zoobar.


Comenzando
----------

Para obtener el nuevo código fuente, primero usa Git para hacer commit de tus soluciones del laboratorio 2,
luego ejecuta `git pull` para obtener el nuevo código, y luego
haz checkout de la rama `lab3`:

```
student@vm-6858:~$ cd lab
student@vm-6858:~/lab$ git commit -am 'my solution to lab2'
[lab1 f54fd4d] my solution to lab2
 1 files changed, 1 insertions(+), 0 deletions(-)
student@vm-6858:~/lab$ git pull
...
student@vm-6858:~/lab$ git checkout -b lab3 origin/lab3
Branch lab3 set up to track remote branch lab3 from origin.
Switched to a new branch 'lab3'
student@vm-6858:~/lab$

```

**ADVERTENCIA:** ¡*no* hagas merge de tus soluciones del laboratorio 2 en el código fuente del
laboratorio 3! Nuestro sistema básico de ejecución simbólica no puede rastrear restricciones
simbólicas a través de RPC entre múltiples procesos, por lo que nos enfocaremos
en usar ejecución simbólica en un sitio Zoobar sin separación de privilegios.
El sistema de ejecución simbólica también nos ayudará a encontrar bugs que la separación
de privilegios no mitiga completamente.

Luego, asegúrate de que el código fuente del laboratorio 3 esté ejecutándose correctamente en tu
VM, ejecutando `make check`. Como se muestra a continuación,
este comando debería reportar que todas las verificaciones fallan, pero si obtienes otros
mensajes de error, detente y averigua qué salió mal.


```bash
student@vm-6858:~/lab$ make check
./check\_lab3.py
FAIL Exercise 1: unsigned average
FAIL Challenge 1: signed average
FAIL Exercise 2: concolic multiply
FAIL Exercise 2: concolic divide
FAIL Exercise 2: concolic divide+multiply+add
FAIL Exercise 3: concrete input for 1234
FAIL Exercise 4: concolic\_find\_input constr2
PASS Exercise 4: concolic\_find\_input constr3
FAIL Exercise 5: concolic\_force\_branch
FAIL Exercise 6: concolic execution for integers
FAIL Exercise 7: concolic length
FAIL Exercise 7: concolic contains
FAIL Exercise 7: concolic execution for strings
FAIL Exercise 8: concolic database lookup (str)
FAIL Exercise 8: concolic database lookup (int)
FAIL Exercise 9: eval injection not found
FAIL Exercise 9: balance mismatch not found
FAIL Exercise 9: zoobar theft not found
PASS Exercise 10: eval injection not found
PASS Exercise 10: balance mismatch not found
PASS Exercise 10: zoobar theft not found
student@vm-6858:~/lab$
```

Nota que partes del sistema de ejecución concolica son bastante intensivas en CPU.
Si estás ejecutando QEMU sin soporte KVM, podrías observar que la
última verificación (para el ejercicio 6) puede tomar mucho tiempo (más de 5 minutos).
Considera habilitar KVM o usar alguna otra VMM de bajo overhead (como VMware).


Usando un solucionador SMT
--------------------------


Una pieza clave de maquinaria usada por la ejecución simbólica es un solucionador SMT.
Para este laboratorio, usarás el [solucionador Z3](https://github.com/Z3Prover/z3)
de Microsoft Research. Invocaremos Z3 usando su API basada en Python;
puedes encontrar útil consultar el
[tutorial z3py](https://ericpony.github.io/z3py-tutorial/) y la
[documentación de la API de Python de Z3](https://z3prover.github.io/api/html/namespacez3py.html). El laboratorio también hará uso del
[soporte de Z3 para
cadenas](https://rise4fun.com/z3/tutorialcontent/sequences). El laboratorio viene con una versión binaria preconstruida de Z3; fue
construida desde el [repositorio de Z3 en github](https://github.com/Z3Prover/z3).

Como primer paso para aprender sobre Z3, lo usaremos para ayudarnos a implementar
un fragmento de código aparentemente simple pero propenso a errores: *calcular el
promedio de dos enteros de 32 bits*. Esto es sorprendentemente sutil de
hacer correctamente. Un enfoque ingenuo para calcular el promedio de x
e y podría ser usar (x+y)/2. Sin embargo, si tanto
x como y son grandes, su suma x+y podría
desbordarse y envolverse alrededor del módulo 2^32, por lo que (x+y)/2 no será
el valor promedio correcto. De hecho, los errores de desbordamiento de enteros son una
fuente significativa de problemas de seguridad para código de sistemas (revisa el [artículo
KINT](https://people.csail.mit.edu/nickolai/papers/wang-kint-2013-06-24.pdf) si tienes curiosidad por aprender más sobre eso), por lo que es importante
saber cómo escribir este código correctamente.

Z3 puede ayudarnos a obtener una implementación correcta de la función de promedio verificando
si una implementación particular que tenemos en mente es correcta.
En particular, dada una expresión booleana, Z3 puede decirnos si
es posible hacer que esa expresión booleana sea verdadera (es decir, satisfacerla).
Además, si es posible hacer que la expresión sea verdadera, y la expresión
contiene algunas variables, Z3 nos dará una asignación de ejemplo de valores
a estas variables que hace que la expresión sea verdadera.


Para ver cómo podemos usar Z3, mira el código que proporcionamos para
ti en `int-avg.py`. Las primeras líneas construyen dos variables de 32 bits
llamadas `a` y `b`. La siguiente línea intenta
calcular el promedio *sin signo* de a y b
(es decir, tratando tanto a como b como enteros sin signo)
y lo almacena en `u_avg`. Nota que este código *no*
realiza realmente la suma y división. En su lugar, construye una
expresión simbólica que representa estas operaciones, y Z3 razonará
sobre los valores posibles de esta expresión más adelante. Puedes observar
esto simplemente imprimiendo la variable `u_avg`:


```bash
student@vm-6858:~/lab$ python3
Python 3.9.7 (default, Sep 10 2021, 14:59:43) 
[GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import z3
>>> a = z3.BitVec('a', 32)
>>> b = z3.BitVec('b', 32)
>>> u\_avg = z3.UDiv(a + b, 2)
>>> print(u\_avg)
UDiv(a + b, 2)
>>> s\_avg = (a + b) / 2
>>> print(s\_avg)
(a + b)/2
>>>
```

Como dice el comentario en el código fuente, debes tener cuidado con la
diferencia entre operaciones enteras con signo y sin signo. En
Z3, los operadores por defecto de Python para división (/) y
desplazamiento a la derecha (>>) tratan los vectores de bits como valores
con signo. Cuando quieres realizar operaciones sin signo, debes
usar las funciones
[z3.UDiv](https://z3prover.github.io/api/html/namespacez3py.html#a64c02a843a4ac8781dd666a991797906)
y
[z3.LShR](https://z3prover.github.io/api/html/namespacez3py.html#a6bffa9a3debf2b93f9407ee7eced222f)
en su lugar.

El código inicial calcula `u_avg` de la forma ingenua que
discutimos anteriormente, y no siempre es correcto. Veamos ahora cómo Z3 puede
ayudarnos a detectar este error. En el resto de `int-avg.py`, calculamos
un valor de referencia que representa el promedio esperado y correcto
de `a` y `b`. Para calcular este valor de referencia,
"hacemos trampa": en realidad convertimos tanto `a` como `b` en enteros de 33 bits
(un bit más que antes) usando
[z3.ZeroExt](https://z3prover.github.io/api/html/namespacez3py.html#a5193573b414389d308baa47eab707fe2).
Luego calculamos su promedio usando el método ingenuo, pero como estamos
usando aritmética de 33 bits, no hay desbordamiento, y el método ingenuo
funciona correctamente. Finalmente truncamos el valor de 33 bits de vuelta a
32 bits, lo cual también es seguro de hacer (porque el promedio siempre
cabrá en 32 bits), y almacenamos la expresión simbólica resultante en
`real_u_avg`.

Ahora, para verificar si `u_avg` calculó el promedio correctamente, simplemente
preguntamos a Z3 si es posible satisfacer la expresión
`u_avg != real_u_avg`, lo que significa que nuestro valor `u_avg` no es correcto.
En este caso, como nuestro promedio ingenuo de 32 bits está roto, la expresión
es satisfacible, y Z3 nos lo dice (por ahora, puedes ignorar la segunda
parte sobre el promedio con signo):


```bash
student@vm-6858:~/lab$ ./int-avg.py
Checking unsigned avg using Z3 expression:
    UDiv(a + b, 2) !=
    Extract(31, 0, UDiv(ZeroExt(1, a) + ZeroExt(1, b), 2))
  Answer for unsigned avg: sat
  Example: {b: 4292870143, a: 4294967287}
  Your average: 2146435067
  Real average: 4293918715
Checking signed avg using Z3 expression:
    (a + b)/2 !=
    Extract(31, 0, (SignExt(1, a) + SignExt(1, b))/2)
  Answer for signed avg: sat
  Example: {b: -2147483648, a: -2147483648}
  Your average: 0
  Real average: -2147483648
student@vm-6858:~/lab$
```

Como puedes ver, Z3 nos dice que la expresión es satisfacible, y nos da
una asignación de ejemplo de valores tanto para `a` como para `b`
para los cuales la expresión es verdadera. Efectivamente, estos valores de ejemplo parecen
bastante grandes, y su suma claramente excede 2^32, rompiendo nuestro
método ingenuo de promedio.


>**Ejercicio 1.**
>Implementa una función correcta para calcular el promedio sin signo de
`a` y `b` usando solo aritmética de 32 bits, modificando la línea `u_avg = ...`
en `int-avg.py`.
>
>Para los propósitos de este ejercicio, no se te permite cambiar el
ancho de bits de tus operandos. Esto está destinado a representar el mundo real,
donde no puedes simplemente agregar un bit más al ancho del registro de tu CPU.
>
>Puedes encontrar útil buscar en línea formas correctas
de realizar aritmética entera de ancho fijo. El libro [Hacker's Delight](https://web.archive.org/web/20190915025154/http://www.hackersdelight.org/) de Henry
S. Warren es una fuente particularmente buena de tales trucos.
>
>Verifica tu función de promedio ejecutando nuevamente
`./int-avg.py` o
`make check`.
Si tu implementación es correcta, `int-avg.py` debería producir
el mensaje Answer for unsigned avg: `unsat`.

>**¡Desafío! (opcional)**
>Para crédito adicional, descubre cómo calcular el promedio de dos
valores de 32 bits *con signo*. Modifica la línea `s_avg = ...`
en `int-avg.py`, y ejecuta `./int-avg.py` o
`make check` para verificar tu respuesta.
Ten en cuenta la dirección del redondeo: `3/2=1` y `-3/2=-1`, por lo que
el promedio de 1 y 2 debería ser 1, y el promedio de
-2 y -1 debería ser -1.
>
>Mientras exploras la aritmética con signo, puedes encontrar útil saber que Z3
tiene dos operadores diferentes tipo módulo. El primero es módulo con signo,
que obtienes usando `a % b` en la API de Python de Z3. Aquí, el
signo del resultado sigue el signo del divisor (es decir, `b`).
Por ejemplo, `-5 % 2 = 1`. El segundo es resto con signo,
que obtienes usando `z3.SRem(a, b)`. Aquí, el signo del
resultado sigue el signo del dividendo (es decir, a). Con las
mismas entradas de ejemplo, `z3.SRem(-5, 2) = -1`.




Interludio: ¿qué son la ejecución simbólica y concolica?
--------------------------------------------------------

Como probablemente recuerdas del artículo EXE, la ejecución simbólica es un
enfoque para probar un programa observando cómo se comporta el programa con
diferentes entradas posibles. Típicamente, el objetivo de la ejecución simbólica es
lograr una alta [cobertura de código](https://en.wikipedia.org/wiki/Code_coverage) o cobertura de rutas en el programa. En el contexto de seguridad,
esto es útil porque ayuda a explorar rutas de código raras que podrían contener
vulnerabilidades pero que no se están disparando en ejecuciones típicas
del código. A alto nivel, si estamos construyendo un sistema de ejecución simbólica,
tenemos que abordar varios puntos:

1. Mientras el programa construye valores intermedios basados en la entrada
(por ejemplo, tomando dos valores enteros de entrada, calculando su promedio, y
almacenando eso en alguna variable), necesitamos recordar la relación entre
la entrada y estos valores intermedios. Típicamente esto se hace
permitiendo que las variables o ubicaciones de memoria tengan valores
*concretos* o *simbólicos*. Un valor concreto es lo que un programa ordinario
almacenaría en una variable o ubicación de memoria: algún valor específico, como
el entero 42. Un valor simbólico no es un valor específico sino más bien
una expresión simbólica que describe lo que el valor *sería* como
una función de las entradas, como (a+b)/2. Esto es similar
a la expresión simbólica de Z3 que construiste para u\_avg en el
primer ejercicio anterior.

2. Necesitamos determinar qué decisiones de flujo de control (ramas) la
aplicación toma basándose en la entrada. Esto se reduce a construir
una restricción simbólica cada vez que el programa se ramifica, describiendo
la condición booleana (en términos de la entrada original del programa)
bajo la cual el programa toma alguna rama particular (o no).
Ya que estamos rastreando cómo todos los valores intermedios están relacionados
con la entrada original del programa, usando valores simbólicos, típicamente no
necesitamos mirar hacia atrás a la entrada original para hacer estas restricciones.
Estas restricciones son similares a la restricción que usaste arriba para buscar
bugs en la función de promedio entero. Determinar estas restricciones de flujo de control es importante porque si el
programa inicialmente va de una manera particular en alguna rama, nos gustaría
descubrir cómo hacer que vaya por el otro camino, para ver si hay
bugs interesantes en ese otro código. En el caso de EXE, usan
un traductor de C-a-C para insertar su propio código en todas las ramas.

3. Para cada una de las ramas anteriores, necesitamos decidir si hay
una entrada posible que causará que el programa se ejecute de la otra manera
en una rama. (Más generalmente, a menudo pensamos en rutas completas de flujo de control,
en lugar de ramas individuales aisladas.) Esto nos ayuda
a encontrar decisiones de flujo de control en un programa que podemos afectar ajustando
la entrada (a diferencia de decisiones de flujo de control que siempre irán de una
manera cierta en un programa, independientemente de la entrada que estemos considerando).
Todos los sistemas de ejecución simbólica dependen de algún tipo de solucionador SMT para hacer esto.

4. Necesitamos especificar qué estamos buscando en nuestras pruebas.
Típicamente esto se piensa mejor en términos de alguna invariante que te
importa asegurar en tu programa, y la ejecución simbólica busca
entradas que violen esta invariante. Una cosa que podríamos buscar es
crashes (es decir, la invariante es que nuestro programa nunca debería crashearse).
Buscar crashes tiene mucho sentido en el contexto de programas en C,
donde los crashes a menudo indican corrupción de memoria que casi ciertamente es un
bug y a menudo podría ser explotado. En lenguajes de más alto nivel como Python,
los bugs de corrupción de memoria no son un problema por diseño, pero aún podríamos
buscar otros tipos de problemas, como ataques de inyección de código a nivel Python
(alguna parte de la entrada se pasa a eval(), por
ejemplo), o invariantes específicas de la aplicación que importan para la seguridad.

5. Finalmente, dadas todas las rutas de flujo de control a través del programa
que son posibles de ejecutar, necesitamos decidir qué ruta probar realmente.
Esto es importante porque puede haber exponencialmente muchas rutas diferentes
a medida que el tamaño del programa crece, y rápidamente se vuelve
inviable probar todas ellas. Por lo tanto, los sistemas de ejecución simbólica típicamente
incluyen algún tipo de *planificador* o *estrategia de búsqueda* que
decide qué ruta es la más prometedora en términos de encontrar violaciones
de nuestra invariante. Un ejemplo simple de una estrategia de búsqueda es probar
ramas que no hemos probado antes, con la esperanza de que ejecutará nuevo
código que aún no hemos ejecutado; esto conducirá a una mayor cobertura de código,
y quizás este nuevo código contiene un bug en el que aún no nos hemos topado.

Una alternativa a la ejecución simbólica es [fuzzing](https://en.wikipedia.org/wiki/Fuzz_testing) (también
llamado prueba de fuzzing). El fuzzing toma un enfoque aleatorizado: en lugar
de tratar de razonar cuidadosamente sobre qué entradas dispararán diferentes
rutas de código en la aplicación, el fuzzing implica construir entradas
aleatorias concretas para el programa y verificar cómo se comporta el programa.
Esto tiene la ventaja de ser relativamente fácil, pero por otro lado,
puede ser difícil construir entradas precisas que alcancen algún caso
específico en el código de la aplicación.

Un desafío en construir un sistema de ejecución simbólica, como EXE, es
que tu sistema tiene que saber cómo ejecutar todas las operaciones posibles en
valores simbólicos (pasos 1 y 2 anteriores).
En este laboratorio, vamos a interponernos
a nivel de objetos Python (en particular, enteros y cadenas).
Esto es desafiante para la ejecución simbólica porque hay una cantidad muy
grande de operaciones que se pueden hacer en estos objetos Python,
por lo que construir un sistema completo de ejecución simbólica para una interfaz de tan alto nivel
sería un proceso tedioso.

Afortunadamente, hay una opción más fácil, llamada *ejecución concolica*,
que puedes pensar como en algún lugar en el medio entre fuzzing completamente
aleatorio y ejecución simbólica completa. La idea es que, en lugar
de rastrear valores puramente simbólicos (como en EXE), podemos almacenar
tanto un valor concreto *como* simbólico para variables que son
derivadas de la entrada. (El nombre *concolic* es un acrónimo
de *concrete* y *symbolic*.) Ahora que tenemos tanto un
valor concreto como simbólico, casi podemos obtener lo mejor de ambos mundos:

* Si la aplicación realiza alguna operación que nuestro sistema concolico
conoce, ejecutaremos más o menos como ejecución simbólica
(excepto que también propagaremos la parte concreta de cada valor).
Por ejemplo, supongamos que tenemos dos variables enteras concolicas `aa`
y `bb`, cuyos valores concretos son 5 y 6, y cuyas expresiones
simbólicas son `a` y `b`. Si la aplicación almacena
`aa+bb` en la variable `cc`, la variable `cc` ahora
tendrá valor concreto 11 y expresión simbólica `a+b`. Similarmente,
si la aplicación se ramifica en `cc==12`, el programa puede ejecutarse
como si la condición de rama fuera falsa (ya que `11 != 12`) y registrar la
condición de rama simbólica correspondiente (`a+b != 12`).

* Si, por otro lado, la aplicación realiza alguna operación que nuestro
sistema concolico no conoce, la aplicación solo obtendrá el
valor concreto. Por ejemplo, si la aplicación escribe la variable
`cc` en un archivo, o quizás la pasa a alguna biblioteca externa
que no instrumentamos, el código aún puede ejecutarse, usando el valor
concreto 11 como si la aplicación simplemente estuviera ejecutándose normalmente.

El beneficio de la ejecución concolica, para los propósitos de este laboratorio, es
que no necesitamos ser completos en términos de soportar operaciones
en valores simbólicos. Mientras soportemos suficientes operaciones para encontrar
bugs interesantes que nos importan en la aplicación, el sistema será
suficientemente bueno (y en la práctica, la mayoría de los sistemas de búsqueda de bugs son aproximados
de todos modos, ya que generalmente es inviable encontrar todos los bugs). La compensación
es por supuesto que, si la aplicación realiza algunas operaciones que no
soportamos, perderemos el rastro de la parte simbólica, y no podremos
hacer exploración estilo ejecución simbólica de esas rutas.
Si estás interesado, puedes aprender más sobre ejecución concolica
leyendo el [artículo DART](https://css.csail.mit.edu/6.858/2022/readings/dart.pdf)
de Godefroid, Klarlund y Sen.

Ejecución concolica para enteros
---------------------------------

Para comenzar, implementarás un sistema de ejecución concolica para valores
enteros. El código esqueleto que te proporcionamos para ejecución concolica
está en `symex/fuzzy.py` en tu directorio de laboratorio. Hay varias
capas importantes de abstracción que están implementadas en `fuzzy.py`:

* **El AST.** En lugar de usar expresiones Z3 para representar valores
simbólicos, como hiciste en el ejercicio `int-avg.py` anterior, construimos
nuestro propio árbol de sintaxis abstracta (AST) para representar expresiones simbólicas.
Un nodo AST podría ser una variable simple (representada por un objeto `sym_str
o `sym_int`), un valor constante (representado por un objeto
`const_int`, `const_str`, o `const_bool`), o
alguna función u operador que toma otros nodos AST como argumentos (por ejemplo,
`sym_eq(a, b)` para representar la expresión booleana `a==b`
donde `a` y `b` son nodos AST, o `sym_plus(a, b)`
para representar la expresión entera `a+b`).
  * Cada nodo AST n puede convertirse en una expresión Z3
llamando `z3expr(n)`. Esto funciona llamando `n._z3expr()`,
y cada nodo AST implementa el método `_z3expr` que devuelve
la representación Z3 correspondiente.
  * La razón por la que introducimos nuestra propia capa AST, en lugar de usar la representación
simbólica de Z3, es que necesitamos realizar ciertas manipulaciones en el
AST que son difíciles de hacer con la representación de Z3. Además,
necesitamos bifurcar un proceso separado para invocar el solucionador de Z3, de modo que en
caso de que el solucionador Z3 tome mucho tiempo, podamos hacer timeout, matar ese
proceso, y asumir que la restricción simplemente no es resoluble. (En este caso,
podríamos perder esas rutas, pero al menos haremos progreso explorando
otras rutas.) Tener nuestro propio AST nos permite aislar limpiamente el estado de Z3
solo al proceso bifurcado.

* **Los envoltorios concolicos.** Para interceptar operaciones a nivel Python y
realizar ejecución concolica, reemplazamos los objetos regulares de Python `int` y
str con subclases concolicas: `concolic_int`
hereda de int y `concolic_str` hereda de
`str`. Cada uno de estos envoltorios concolicos almacena un valor
concreto (en `self.__v`) y una expresión simbólica (un nodo AST,
en `self.__sym`). Cuando la aplicación calcula alguna expresión
derivada de un valor concolico (por ejemplo, `a+1` donde a es
un `concolic_int`), necesitamos interceptar la operación y devolver
otro valor concolico que contiene tanto el valor de resultado concreto como una
expresión simbólica de cómo se calculó el resultado.
  * Para realizar esta interceptación, sobrecargamos varios métodos en las
clases `concolic_int` y `concolic_str`. Por ejemplo,
`concolic_int.__add__` se invoca cuando la aplicación calcula
`a+1` en el ejemplo anterior, y este método devuelve un nuevo valor
concolico que representa el resultado.
  * En principio, deberíamos tener un `concolic_bool` que sea una subclase
de `bool` también. Desafortunadamente, `bool` no puede ser subclassed
en Python (ver [aquí](https://docs.python.org/3/library/functions.html#bool)
y [aquí](https://mail.python.org/pipermail/python-dev/2002-March/020822.html)).
Entonces, hacemos que `concolic_bool` sea una función que lógicamente simula
que, una vez que construyes un valor booleano concolico, el programa inmediatamente
se ramifica en su valor, por lo que `concolic_bool` también agrega una restricción
a la condición de ruta actual. (La restricción es que la expresión
simbólica del valor booleano es igual al valor concreto.) La
función `concolic_bool` luego devuelve un valor booleano concreto.

* **Las entradas concretas.**
Las entradas al programa que se está probando bajo ejecución concolica están
almacenadas en el diccionario `concrete_values`.
Este diccionario da nombres de cadena a las entradas del programa,
y mapea cada nombre al valor de esa entrada.
El valor es
un entero regular de Python (para variables enteras) o una cadena regular de Python
(para variables de cadena).
  * La razón por la que `concrete_values` es una variable global es que las aplicaciones
crean valores concolicos invocando `fuzzy.mk_str(name)` o
`fuzzy.mk_int(name)` para construir una cadena concolica o un entero concolico,
respectivamente. Esto devuelve un nuevo valor concolico, cuya parte simbólica
es un nodo AST nuevo correspondiente a una variable llamada name,
pero cuyo valor concreto se busca en el diccionario
`concrete_values`. Si no hay un valor específico asignado a esa variable
en `concrete_values`, el sistema usa por defecto algún valor inicial
(0 para enteros y la cadena vacía para cadenas).
  * El marco de ejecución concolica mantiene una cola de diferentes
entradas para probar, en un objeto `InputQueue` (también definido en
`symex/fuzzy.py`). El marco de ejecución concolica primero agrega una
entrada inicial (el diccionario vacío {}), y luego ejecuta el código.
Si la aplicación hace alguna rama, el sistema de ejecución concolica
invocará Z3 para encontrar nuevas entradas para probar otras rutas en el código,
agregará esas entradas a la cola de entradas, y seguirá iterando hasta que no haya
más entradas para probar.

* **El solucionador SMT.**
La función `fork_and_check(c)` verifica si la restricción
`c` (un AST) es una expresión satisfacible, y devuelve un par
de valores: el estado de satisfactibilidad ok y el modelo de ejemplo
(asignación de valores a variables) si la restricción es satisfacible. La
variable ok es `z3.sat` si la restricción es satisfacible,
y `z3.unsat` o `z3.unknown` en caso contrario. Internamente, esta
función bifurca un proceso separado, intenta ejecutar el solucionador Z3, pero si
toma más de unos segundos (controlado por `z3_timeout`),
mata el proceso y devuelve `z3.unknown`.

* **La condición de ruta actual.**
Cuando la aplicación se ejecuta y toma decisiones de flujo de control basándose en
el valor de un valor concolico (ver discusión de `concolic_bool`
arriba), la restricción que representa esa rama se agrega a la
lista `cur_path_constr`. Para generar entradas que
tomen una decisión diferente en un punto a lo largo de la ruta, la restricción
requerida es la unión de las restricciones antes de ese punto en
la ruta, más la negación de la restricción en ese punto.
Para ayudar con depuración y heurísticas de
búsqueda, información sobre la línea de código que disparó cada rama
se agrega a la lista `cur_path_constr_callers`.

Ahora, tu trabajo será terminar la implementación de `concolic_int`,
y luego implementar el núcleo del bucle de ejecución concolica. Proporcionamos
dos programas de prueba para ti, `check-concolic-int.py` y
`check-symex-int.py`. Echa un vistazo a estos programas para tener una idea
de cómo estamos usando ejecución concolica, y qué código estos casos de prueba están
invocando.


>**Ejercicio 2.**
>Termina la implementación de `concolic_int` agregando soporte para
operaciones de multiplicación y división enteras. Necesitarás sobrecargar métodos adicionales
en la clase `concolic_int` (ver la documentación para
[funciones de operador
en Python 3](https://docs.python.org/3/library/operator.html)), agregar nodos AST para operaciones de multiplicación y
división, e implementar `_z3expr` apropiadamente para esos
nodos AST.
>
>Busca los comentarios Ejercicio 2: tu código aquí en
`symex/fuzzy.py` para encontrar lugares donde creemos que podrías necesitar
escribir código para resolver este ejercicio.
>
>Ejecuta `./check-concolic-int.py` o `make check` para verificar que tus cambios a
`concolic_int` funcionen correctamente.


> **Ejercicio 3**. Un componente importante de la ejecución concolica
 es `concolic_exec_input()` en `symex/fuzzy.py`. Te hemos dado
 la implementación. La usarás para construir un sistema completo de ejecución concolica.
 Para entender cómo usar `concolic_exec_input()`, debes
 crear una entrada tal que pases la primera verificación
 en `symex/check-symex-int.py`. No
 modifiques `symex/check-symex-int.py` directamente, sino modifica
 `symex_exercises.py`.
>
> Ejecuta `./check-symex-int.py` o `make check` para verificar tu solución.


>**Ejercicio 4**. Otro componente importante en la ejecución concolica
 es encontrar una entrada concreta para una restricción. Completa la
 implementación de `concolic_find_input` en `symex/fuzzy.py` y
 asegúrate de pasar el segundo caso de prueba de `symex/check-symex-int.py`.
 Para este ejercicio, tendrás que invocar Z3, algo así como
 `(ok, model) = fork_and_check(constr)` (ver los comentarios en el código).
>
> Ejecuta `./check-symex-int.py` o `make check` para verificar tu solución.


>**Ejercicio 5**. Un componente importante final en la ejecución concolica
 es explorar diferentes ramas de ejecución. Completa la
 implementación de `concolic_force_branch` en `symex/fuzzy.py`
 y asegúrate de pasar el caso de prueba final
 de `symex/check-symex-int.py`.
>
> Ejecuta `./check-symex-int.py` o `make check` para verificar tu solución.


>**Ejercicio 6**. Ahora implementa ejecución concolica de una
 función en `concolic\_execs()` en
`symex/fuzzy.py`. El objetivo es eventualmente hacer que cada rama
de la función sea ejecutada. Lee el comentario para un plan de ataque propuesto
para implementar ese bucle. Las funciones en los ejercicios 3-5 deberían ser
bastante útiles.
>
>Ejecuta `./check-symex-int.py`
o `make check` para verificar que
tu `concolic_execs()` funcione correctamente.
>
>Ten cuidado de que nuestra verificación para este ejercicio *no* está completa.
Bien podrías encontrar que más adelante algo no funciona, y tendrás
que revisar tu código para este ejercicio.

Ejecución concolica para cadenas y Zoobar
-----------------------------------------

Antes de poder ejecutar toda la aplicación Zoobar a través de nuestro sistema concolico,
primero tenemos que agregar soporte para cadenas, además del soporte para enteros
que agregamos arriba. Este es ahora tu trabajo.

>**Ejercicio 7**.
>Termina la implementación de ejecución concolica para cadenas y arreglos de bytes en
`symex/fuzzy.py`. Dejamos fuera soporte para dos operaciones en
objetos `concolic_str` y `concolic_bytes`. La primera es calcular la longitud
de una cadena, y la segunda es verificar si una cadena particular
`a` aparece en la cadena `b` (es decir, `a` está contenida
en `b`, la implementación subyacente del constructo de Python
"a in b").
>
>Busca el comentario Ejercicio 7: tu código aquí para encontrar dónde
debes implementar el código para este ejercicio. Ya hemos
implementado los nodos AST `sym_contains` y `sym_length`
para ti, que deberían ser útiles para este ejercicio.
>
>Ejecuta `./check-concolic-str.py` *y*
`./check-symex-str.py` (o simplemente ejecuta
`make check`) para verificar que tu respuesta a
este ejercicio funcione correctamente.


Además de realizar operaciones de cadena, el código de la aplicación Zoobar
hace consultas a la base de datos (por ejemplo, buscar el objeto `Profile`
de un usuario desde la base de datos de perfiles). Nuestro plan es suministrar una solicitud
HTTP concolica a Zoobar, por lo que el nombre de usuario que se está buscando será
un valor concolico también (viniendo a través de la cookie HTTP). Pero ¿cómo podemos
realizar consultas SQL en un valor concolico? Nos gustaría permitir que el
sistema de ejecución concolica de alguna manera explore todos los registros posibles que
podría obtener de la base de datos, pero la consulta SQL va al código de SQLite
que está escrito en C, no en Python, por lo que no podemos interponernos en ese
código.

>**Ejercicio 8**.
>Descubre cómo manejar la base de datos SQL para que el motor concolico
pueda crear restricciones contra los datos devueltos por la base de datos.
Para ayudarte a hacer esto, hemos escrito un wrapper vacío alrededor del método
get de sqlalchemy, en `symex/symsql.py`. Implementa este wrapper
para que la ejecución concolica pueda probar todos los registros posibles en una base de datos.
Examina `./check-symex-sql.py` para ver cómo
estamos pensando realizar búsquedas en la base de datos en valores concolicos.
>
>Probablemente necesitarás consultar la referencia para el
[objeto de consulta de SQLalchemy](https://docs.sqlalchemy.org/en/11/orm/query.html) para entender cuál debería ser el comportamiento de get
y qué debería hacer tu implementación de reemplazo.
>
>Ejecuta `./check-symex-sql.py` (o simplemente ejecuta
`make check`) para verificar que tu respuesta a
este ejercicio funcione correctamente.

Ahora que podemos realizar ejecución concolica para cadenas e incluso consultas de
base de datos, finalmente podemos intentar ejecutar Zoobar bajo ejecución concolica.
Echa un vistazo al programa `check-symex-zoobar.py` para ver cómo
podemos invocar Zoobar con entradas simbólicas. Para asegurar que la ejecución concolica
de Zoobar termine relativamente rápido, sobre-restringimos las
entradas iniciales a Zoobar. En particular, especificamos que el método HTTP
(en `environ['REQUEST_METHOD']`) siempre es `GET`, y que
la URL solicitada (en `environ['PATH\_INFO']`) siempre comienza con
trans. Esto reduce enormemente el número de rutas posibles que
la ejecución concolica debe explorar; hacer estas entradas arbitrarias conduce a
alrededor de 2000 rutas que deben ser exploradas, lo que toma alrededor de 10 minutos.

Intenta ejecutar `check-symex-zoobar.py` para asegurar que todo el
código que has implementado hasta ahora en este laboratorio funcione correctamente. Sugerimos
ejecutarlo dentro de script para que la salida se guarde en el
archivo `typescript` para inspección posterior:


```bash
student@vm-6858:~/lab$ script -c ./check-symex-zoobar.py
Script started, file is typescript
Trying concrete values: {}
startresp 404 NOT FOUND [('Content-Type', 'text/html'), ('Content-Length', '233'), ('X-XSS-Protection', '0')]
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>

Trying concrete values: {'referrer': '', 'cookie': '', 'path': 'fer'}
/home/student/lab/zoobar/debug.py:23 :: \_\_try : caught exception in function transfer:
 Traceback (most recent call last):
  File "/home/student/lab/zoobar/debug.py", line 20, in \_\_try
    return f(*args, **kwargs)
  File "/home/student/lab/zoobar/login.py", line 59, in loginhelper
    if not logged\_in():
  File "/home/student/lab/zoobar/login.py", line 50, in logged\_in
    g.user.checkCookie(request.cookies.get("PyZoobarLogin"))
  File "/usr/lib/python2.7/dist-packages/werkzeug/local.py", line 338, in \_\_getattr\_\_
    return getattr(self.\_get\_current\_object(), name)
  File "/usr/lib/python2.7/dist-packages/werkzeug/utils.py", line 71, in \_\_get\_\_
    value = self.func(obj)
  File "/home/student/lab/symex/symflask.py", line 44, in cookies
    fuzzy.require(hdr == name + '=' + val)
  File "/home/student/lab/symex/fuzzy.py", line 362, in require
    raise RequireMismatch()
RequireMismatch

startresp 500 INTERNAL SERVER ERROR [('Content-Type', 'text/html'), ('Content-Length', '291')]
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>500 Internal Server Error</title>
<h1>Internal Server Error</h1>
<p>The server encountered an internal error and was unable to complete your request.  Either the server is overloaded or there is an error in the application.
</p>

Trying concrete values: {'referrer': '', 'path': 'fer', 'cookie\_name': 'v', 'cookie': 'v=aC', 'cookie\_val': 'aC'}
...
Stopping after 139 iterations
Script done, file is typescript
student@vm-6858:~/lab$
```

Entonces, ¿qué bugs encontramos en estas 139 rutas diferentes? Como Zoobar
está escrito en Python, no hay bugs de corrupción de memoria o crashes,
por lo que no es inmediatamente claro cómo podríamos decir que hay un problema.
Como resultado, tenemos que escribir invariantes explícitas para detectar situaciones malas
indicativas de un problema de seguridad.

Una de esas invariantes que hemos proporcionado para ti es una verificación de inyección eval;
es decir, entrada arbitraria que se pasa a la función `eval()`
en Python. Examina `symex/symeval.py` para ver cómo verificamos
inyección eval. Hacemos una aproximación que parece razonable en
la práctica: si la cadena pasada a `eval()` puede alguna vez contener
`;badstuff();` en algún lugar de la cadena, es una buena apuesta que
tenemos una vulnerabilidad de inyección `eval`. Como la implementación de eval
está escrita en Python, la verificación '`;badstuff();`' en
`expr` invoca tu método sobrecargado en `concolic_str`, y
esto le dice al sistema de ejecución concolica que intente construir una entrada
que contenga esa subcadena.

Puedes ver si Zoobar contiene alguno de estos bugs buscando la
cadena impresa por esa verificación en `symex/symeval.py` en la
salida de `check-symex-zoobar.py`:

```
student@vm-6858:~/lab$ grep "Exception: eval injection" typescript
Exception: eval injection
Exception: eval injection
student@vm-6858:~/lab$
```

Parece que el sistema de ejecución concolica encontró dos entradas diferentes
que conducen a nuestra verificación de "inyección eval". Ahora podrías mirar las
líneas justo antes de ese mensaje para ver qué entrada concreta dispara la inyección eval.
Esto puede ayudar enormemente a un desarrollador en la práctica a encontrar y
corregir tal bug.

Ahora, tu trabajo será implementar dos verificaciones de invariante adicionales para
ver si los balances de Zoobar pueden alguna vez corromperse. En particular, queremos
hacer cumplir dos garantías:

* Si no se registran nuevos usuarios, la suma de los balances de Zoobar en todas las
cuentas debe permanecer igual antes y después de cada solicitud.
(Es decir, los zoobars nunca deberían crearse de la nada.)

* Si un usuario `u` no emite ninguna solicitud a Zoobar, el balance de Zoobar de `u`
no debería reducirse. (Es decir, debería ser imposible
que las solicitudes de un usuario roben los zoobars de otro usuario.)

>**Ejercicio 9**.
>Agrega verificaciones de invariante a check-symex-zoobar.py para implementar las
dos reglas anteriores (preservación del balance total y sin robo de zoobars). Busca
el comentario Ejercicio 9: tu código aquí para ver dónde
debes escribir este código. Cuando detectes un desajuste del balance de zoobars, llama
a la función `report_balance_mismatch()`. Cuando detectes robo de zoobars,
llama a `report_zoobar_theft()`.
>
>Recuerda que nuestra verificación para los ejercicios 3-6, donde implementaste el núcleo
del sistema de ejecución concolica, no estaba completa. Si estás teniendo
problemas con este ejercicio, puede ser que no implementaste los ejercicios
3-6 correctamente, por lo que puede que necesites volver y corregirlos.
>
>Para verificar si tu solución funciona correctamente, necesitas ejecutar nuevamente
`./check-symex-zoobar.py` y ver si
la salida contiene los mensajes `WARNING: Balance mismatch detected`
y `WARNING: Zoobar theft detected`. Alternativamente, puedes
ejecutar `make check`, que hará esto por
ti (ejecuta `check-symex-zoobar.py` y busca estas cadenas mágicas).


Finalmente, tu trabajo es corregir estos dos bugs (desajuste del balance de zoobars
y robo de zoobars), y asegurarte de que tu sistema de ejecución simbólica
reporte correctamente que estos bugs ya no son alcanzables.
Para corregir los bugs, pedimos que *no* modifiques el código fuente original
de Zoobar en el directorio `zoobar`, para que
`make check` pueda seguir funcionando. En su lugar, por favor haz una copia de cualquier
archivo `.py` que quieras corregir del directorio zoobar en
`zoobar-fixed`. Luego usa el script `check-symex-zoobar-fixed.sh`
para ver si tus correcciones funcionan correctamente.

Ya corregimos el bug de inyección eval para ti, en
`zoobar-fixed/transfer.py`. También debes asegurarte de que tu
sistema de ejecución concolica ya no reporte bugs de inyección eval.

>**Ejercicio 10**.
>Corrige los dos bugs que encontraste en el Ejercicio 9, copiando los archivos `.py`
que necesites modificar del directorio `zoobar` a
`zoobar-fixed` y cambiándolos allí.
>
>Recuerda que nuestra verificación para los ejercicios 3-6, donde implementaste el núcleo
del sistema de ejecución concolica, no estaba completa. Si estás teniendo
problemas con este ejercicio, puede ser que no implementaste los ejercicios
3-6 correctamente, por lo que puede que necesites volver y corregirlos.
>
>Para verificar si tu solución funciona correctamente, necesitas ejecutar
`./check-symex-zoobar-fixed.sh` y ver si la
salida todavía contiene los mensajes `Exception: eval injection`,
`WARNING: Balance mismatch detected` y
`WARNING: Zoobar theft detected`. Alternativamente, puedes ejecutar
`make check`, que hará esto por ti.


¡Estás listo!
Envía tus respuestas a la tarea del laboratorio ejecutando
make prepare-submit y sube el archivo resultante
lab3-handin.tar.gz a Canvas.

