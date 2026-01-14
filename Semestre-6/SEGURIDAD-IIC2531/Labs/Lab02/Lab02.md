# Lab 2: Separación de privilegios y sandboxing del lado del servidor

Este laboratorio te introducirá a la separación de privilegios y sandboxing
del lado del servidor, en el contexto de una aplicación web simple en Python llamada
zoobar, donde los usuarios transfieren "zoobars" (créditos) entre ellos.
El objetivo principal de la separación de privilegios es asegurar que si un adversario
compromete una parte de una aplicación, el adversario no comprometa las
otras partes también. Para ayudarte a separar privilegios en esta aplicación, el
servidor web `zookws` que ya viste en el laboratorio anterior está
diseñado para ejecutar una aplicación web que consiste en múltiples componentes.
Si tienes curiosidad, este diseño está basado en el servidor web [OKWS](https://okws.org/), descrito en un
[paper de investigación](https://css.csail.mit.edu/6.858/2024/readings/okws.pdf) y usado por [okcupid.com](https://www.okcupid.com/). En un sistema moderno
a gran escala, el diseño probablemente consistiría en muchas más partes móviles, como
usar Kubernetes para ejecutar todos los componentes de tu aplicación,
usar una librería RPC como gRPC para comunicar entre componentes, etc,
pero `zookws` empaqueta todo esto en un sistema relativamente simple.

En este laboratorio, configurarás un servidor web con separación de privilegios,
examinarás posibles vulnerabilidades, y dividirás el código de la aplicación
en componentes con menos privilegios para minimizar los efectos de cualquier
vulnerabilidad individual. El laboratorio usará soporte moderno para separación de
privilegios, [contenedores Linux](https://linuxcontainers.org/).
(El diseño original de OKWS usaba IDs de usuario y chroot, porque los contenedores
Linux y namespaces no existían en ese momento.)

 También extenderás la aplicación web Zoobar para soportar
*perfiles ejecutables*, que permiten a los usuarios usar código Python como
sus perfiles. Para hacer un perfil, un usuario guarda un programa Python
en su perfil en su página principal de Zoobar. (Para indicar que el
perfil contiene código Python, la primera línea debe ser `#!python`.)
Cada vez que otro usuario vea el perfil Python del usuario, el servidor
ejecutará el código Python en el perfil de ese usuario para generar la
salida del perfil resultante. Esto permitirá a los usuarios implementar una variedad de características
en sus perfiles, como:

* Un perfil que saluda a los visitantes por su nombre de usuario.
* Un perfil que lleva registro de los últimos varios visitantes a ese perfil.
* Un perfil que da un `zoobar` a cada visitante (límite 1 por minuto).

Soportar esto de manera segura requiere hacer sandbox del código del perfil en el servidor,
para que no pueda realizar operaciones arbitrarias o acceder a archivos arbitrarios.
Por otro lado, este código puede necesitar llevar registro de datos persistentes en
algunos archivos, o acceder a las bases de datos existentes de zoobar, para funcionar correctamente.
Usarás la librería de llamadas a procedimientos remotos y algo de código shim que proporcionamos para
hacer sandbox de manera segura a los perfiles ejecutables en el servidor usando WebAssembly.

Para obtener el nuevo código fuente, usa Git para hacer commit de tus soluciones del Lab 1,
y luego cambia a la rama lab2.

```
student@6566-v24:~$ cd lab
student@6566-v24:~/lab$ git status
...
student@6566-v24:~/lab$ git add exploit-*.py http.c zookd.c [and any other new files...]
student@6566-v24:~/lab$ git commit -am 'my solution to lab1'
[lab1 c54dd4d] my solution to lab1
 1 files changed, 1 insertions(+), 0 deletions(-)
student@6566-v24:~/lab$ git fetch
...
student@6566-v24:~/lab$ git checkout -b lab2 origin/lab2
Branch lab2 set up to track remote branch lab2 from origin.
Switched to a new branch 'lab2'

```

Una vez que tu código fuente esté en su lugar, asegúrate de que puedes compilar e instalar
el servidor web y la aplicación `zoobar`:

```
student@6566-v24:~/lab$ make
cc zookd.c -c -o zookd.o -m64 -g -std=c99 -Wall -Wno-format-overflow -D\_GNU\_SOURCE -static -fno-stack-protector
cc http.c -c -o http.o -m64 -g -std=c99 -Wall -Wno-format-overflow -D\_GNU\_SOURCE -static -fno-stack-protector
...
cc zookfs.c -c -o zookfs.o -m64 -g -std=c99 -Wall -Wno-format-overflow -D\_GNU\_SOURCE -static -fno-stack-protector
cc -m64  zookfs.o http.o   -o zookfs
cc zookd2.c -c -o zookd2.o -m64 -g -std=c99 -Wall -Wno-format-overflow -D\_GNU\_SOURCE -static -fno-stack-protector
cc -m64  zookd2.o http.o   -o zookd2
student@6566-v24:~/lab$

```

## Preludio: ¿Qué es un zoobar?

Para entender la aplicación `zoobar` en sí, primero examinaremos
el código de la aplicación web zoobar.

Una de las características clave de la aplicación `zoobar` es la capacidad de
transferir créditos entre usuarios. Esta característica está implementada por el 
script `transfer.py`.

Para tener una idea de lo que hace transfer, inicia el sitio web zoobar. Para
el lab 2, iniciamos el servidor web usando el launcher `zookld.py`, que es
similar al daemon launcher `okld` en OKWS:

```
student@6566-v24:~/lab$ ./zookld.py
~base: Creating container
Unpacking the rootfs
~base: Configuring
*... lots of output ...*
main: Creating container
main: Copying files
main: Running zooksvc.py
main: zooksvc.py: dispatcher main, port 8080
main: zooksvc.py: running ['./zookd2', '3', '5']
main: zookd2: Start with 1 service(s)
main: zookd2: Dispatch ^(.*)$ for service 0
main: zookd2: Host 10.1.1.4 (link 1) service 0
main: zookd2: Port 8081 for service 0
zookfs: Creating container
zookfs: Copying files
zookfs: Running zooksvc.py
zookfs: zooksvc.py: running ['./zookfs', '8081']
echo: Creating container
echo: Copying files
echo: Running zooksvc.py
echo: zooksvc.py: running ['.//zoobar/echo-server.py', '8081']
echo: Running on port 8081
student@6566-v24:~/lab$ 

```

La primera vez que ejecutes `zookld.py` correrá por minutos,
porque está construyendo el contenedor base, lo que involucra
construir una imagen Linux e instalar todo el software que `zoobar`
necesita. Luego, construye otros tres
contenedores: `main`, `zookfs`, y `echo`.
Cada uno de estos contenedores tiene el contenido de tu directorio `/home/student/lab`
copiado en ``/app, para que puedas ejecutar tu código dentro
del contenedor.
Los contenedores en sí están almacenados en el directorio `~/.local/share/lxc`,
si tienes curiosidad sobre cómo están implementados los contenedores.
`zookld.py`
usa `zookconf.py` para construir y configurar los contenedores.
Si obtienes errores sobre crear o iniciar contenedores, intenta
resetear el estado del contenedor usando el comando `./zookclean.py`
y/o reiniciar tu VM.

Puedes manipular los contenedores con los siguientes comandos:

* `zookld.py`: inicia contenedores listados en zook.conf
* `zookps.py`: lista el estado de los contenedores listados
 en zook.conf y los procesos ejecutándose en ellos.
* `zookstop.py`: detiene los contenedores listados en zook.conf
* `zookclean.py`: elimina todos los contenedores de `~/.local/share/lxc`, por si quieres empezar desde
 cero de nuevo.

Cada uno de estos comandos también puede tomar el nombre de un contenedor individual (e.g., `main`) 
y aplicar la operación solo a ese contenedor.

Todos estos comandos son wrappers alrededor de
la [API Python de LXC](https://linuxcontainers.org/lxc/documentation/#python). 
También puedes ejecutar muchos de los comandos LXC desde [línea de comandos](https://linuxcontainers.org/lxc/manpages/);
en particular, `lxc-attach -n name` te dará un
shell root en el contenedor name, que podrías encontrar útil para debugging.

Ejecuta `zookps.py` para ver si tus contenedores están ejecutándose. Luego, asegúrate
de que puedes ejecutar el servidor web, y acceder al sitio web desde tu navegador, como
sigue:

```
student@6566-v24:~/lab$ ip addr show dev eth0
2: eth0:  mtu 1500 qdisc fq_codel state UP group default qlen 1000
 link/ether 00:0c:29:b4:55:8e brd ff:ff:ff:ff:ff:ff
 altname enp0s3
 altname ens3
 inet 192.168.24.128/24 brd 192.168.24.255 scope global eth0
 valid_lft forever preferred_lft forever
 inet6 fe80::20c:29ff:feb4:558e/64 scope link
 valid_lft forever preferred_lft forever

```

En este ejemplo particular, querrías
abrir tu navegador e ir a `http://192.168.24.128:8888/zoobar/index.cgi/`,
o, si estás usando KVM, a `http://localhost:8888/zoobar/index.cgi/`.
Deberías ver el sitio web `zoobar`.


Nota el puerto diferente, `8888` en lugar de `8080`, en las URLs de arriba.
Esto es porque en realidad queremos conectarnos al contenedor
`main`, pero está en una red virtual interna que solo es accesible
desde la VM misma. Configuramos el kernel Linux en la VM para reenviar
conexiones del puerto `8888` al puerto `8080` en el contenedor `main`.
Puedes ver las reglas iptables que usamos para lograr esto en
`/etc/rc.local` en tu VM.

Si tienes problemas viendo el sitio web, una posible causa
es que las correcciones que hiciste en el Lab 1 para arreglar los bugs de buffer overflow
pueden ser demasiado estrictas. Si es así, por favor corrígelo antes de continuar.

>**Ejercicio 1.**
En tu navegador, conéctate al sitio web `zoobar`, y crea dos cuentas de
usuario. Inicia sesión como uno de los usuarios, y transfiere zoobars de un usuario a
otro haciendo clic en el enlace de transfer y llenando el formulario. Juega
con las otras características también para tener una idea de lo que permite a los usuarios
hacer. En resumen, un usuario registrado puede actualizar su perfil, transferir
"zoobars" (créditos) a otro usuario, y buscar el balance de zoobar, perfil,
y transacciones de otros usuarios en el sistema.
>
>Lee el código de `zoobar` y ve cómo transfer.py
se invoca cuando un usuario envía una transfer en la página de transfer. Un buen lugar para
empezar para esta parte del laboratorio es `templates/transfer.html`,
`\_\_init__.py`, `transfer.py`, y `bank.py` en el directorio zoobar.
>
>**Nota:** No necesitas entregar nada para este ejercicio, pero asegúrate
de que entiendes la estructura de la aplicación `zoobar`--¡te ahorrará
tiempo en el futuro!

## Separación de privilegios

Habiendo examinado el código de la aplicación `zoobar`, vale la pena empezar a pensar
sobre cómo aplicar separación de privilegios a la infraestructura `zookws` y
zoobar para que los bugs en la infraestructura no permitan a un
adversario, por ejemplo, transferir zoobars a la cuenta del adversario.

El servidor web para este laboratorio usa contenedores para diferentes partes del servidor
web. Los contenedores están definidos en `zook.conf`. 
`zookld.py` usa `zookconf.py` para leer `zook.conf`
(vía `readconf.py`) y configurar los contenedores. Como parte de este laboratorio
definirás nuevos contenedores y modificarás cómo se configuran los contenedores. Para ese
propósito necesitas trabajar con LXC y podrías encontrar útil referirte a la
documentación sobre [LXC](https://linuxcontainers.org/lxc/introduction/).

Dos aspectos hacen que la separación de privilegios sea desafiante en el mundo real y en
este laboratorio. Primero, la separación de privilegios requiere que desarmes la
aplicación y la dividas en piezas separadas. Aunque hemos tratado de
estructurar la aplicación bien para que sea fácil de dividir, hay lugares
donde debes rediseñar ciertas partes para hacer posible la separación de privilegios.
Segundo, debes asegurar que cada pieza se ejecute con privilegios mínimos, lo que
requiere configurar permisos precisamente y configurar las piezas
correctamente. Con suerte, al final de este laboratorio, tendrás una mejor
comprensión de por qué muchas aplicaciones tienen vulnerabilidades de seguridad relacionadas
con la falla de separar privilegios adecuadamente: ¡la separación de privilegios adecuada es
difícil!

Un problema en el que podrías encontrarte es que es complicado hacer debug de una aplicación
compleja que está compuesta de muchas piezas. Para ayudarte, hemos proporcionado
una librería de debug simple en `debug.py`, que es importada por cada
script de Python que te damos. La librería de debug proporciona una sola
función, `log(msg)`, que imprime el mensaje `msg` a
`stderr` (que debería ir a la terminal donde ejecutaste `zookld`),
junto con un stack trace de dónde se llamó la función `log`.

Toda la salida del código ejecutándose en varios contenedores que veas en tu
terminal también debería estar prefijada con el nombre del contenedor.
Por ejemplo, cuando veas `main: zookd2: Forwarding to 10.1.1.4:8081
for /zoobar/media/zoobar.css`, significa que el mensaje viene del
contenedor `main`.

Si algo no parece estar funcionando, intenta averiguar qué salió mal, o
contacta al personal del curso (profesor o ayudantes), antes de proceder más.

## Parte 1: Separar privilegios de la configuración del servidor web usando contenedores

En el lab 1, `zookws` consistía esencialmente de un proceso:
`zookd`. Desde el punto de vista de seguridad, esta estructura no es ideal:
por ejemplo, cualquier buffer overflow que encontraste, puedes usarlo para tomar
control de `zookws`. Por ejemplo, puedes invocar los scripts dinámicos con
argumentos de tu elección (e.g., darte muchos zoobars a ti mismo), o más simple,
solo escribir la base de datos que contiene las cuentas de `zoobar` directamente.

Este laboratorio refactoriza `zookd`
siguiendo el diseño [OKWS](https://okws.org/). Similar a OKWS,
`zookws` consiste de un programa launcher `zookld.py` que
lanza servicios configurados en el archivo `zook.conf`, un
`zookd` que solo enruta solicitudes a servicios correspondientes, así como
varios servicios. Por simplicidad `zookws` no implementa `helper` o
`daemon logger` como lo hace OKWS. Puedes pensar en `zookld.py` como una versión
minimalista de Kubernetes.

Ejecutaremos cada componente en un contenedor Linux separado. Los contenedores Linux
proporcionan la ilusión de una máquina Linux virtual sin usar máquinas virtuales;
están implementados usando procesos Linux. Un proceso en un contenedor está
más aislado que los procesos Linux estándar: un proceso dentro de un contenedor
tiene acceso limitado a los namespaces del kernel, tiene acceso limitado a las system calls,
y no tiene acceso al sistema de archivos. En muchos aspectos, se comportan como máquinas
virtuales: se inician desde una imagen de maquina virtual, tienen su propia dirección IP, su
propio sistema de archivos, etc. Les asignas direcciones IP, copias los archivos correctos
en ellos, y arreglas llamadas a procedimientos remotos entre ellos.

Usaremos contenedores *sin privilegios*, que se ejecutan como un proceso de usuario
sin privilegios (i.e., no root). Incluso si el proceso ejecutándose dentro del
contenedor se ejecuta con privilegios de root, el contenedor mismo se ejecuta como un
usuario sin privilegios.

Con contenedores, incluso si hay un exploit (e.g., otro buffer overflow
en zookd), el contenedor ejecutando `zookd` le dará al atacante
poco control. Por ejemplo, tomar control de `zookd`, no permitirá al
atacante invocar los scripts dinámicos o escribir la base de datos directamente que se ejecuta
dentro de otro contenedor. Además, `zookd` no puede salir de su
contenedor y tomar control del kernel Linux subyacente.

El archivo `zook.conf` es el archivo de configuración que especifica cómo
cada contenedor debería ejecutarse. Por ejemplo, la entrada `main`:

```
[main]
    cmd = zookd2
    dir = /app
    lxcbr = 0
    port = 8080
    http_svcs = zookfs

```

especifica que el comando para ejecutar `main` es `zookd2`, en el directorio
`/app` en un contenedor conectado a la red virtual 0
(`lxcbr`, abreviación de LXC bridge), y
que `cmd` obtiene el puerto `8080` para recibir/enviar solicitudes.

En la VM del laboratorio que estás usando, pre-creamos 10 redes virtuales,
`lxcbr0` a través de `lxcbr9`, que puedes usar, correspondiendo
a las direcciones de red `10.1.0.*` a través de `10.1.9.*`
respectivamente (o `10.1.0.0/24` a través de `10.1.9.0/24` en
notación [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)). Cada contenedor obtiene la dirección IP .4 en la subred de su
red virtual; por ejemplo, si asignas algún servicio a `lxcbr = 7`,
tendrá la dirección IP `10.1.7.4`.

La razón para tener múltiples redes virtuales es proporcionar un fuerte aislamiento de red
entre contenedores. Los contenedores conectados a la misma red virtual
pueden enviarse paquetes directamente entre ellos, y un contenedor comprometido podría falsificar
paquetes de la dirección IP de otro contenedor. Por otro lado, los contenedores
en diferentes redes virtuales deben pasar por el kernel Linux del host para enrutar
paquetes, y el kernel Linux asegura que los paquetes que vienen de una red virtual
no falsifiquen una dirección de origen de una red virtual diferente (habilitado
por la opción del kernel [rp\_filter](https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt)).

Por defecto, cada contenedor permite paquetes entrantes de cualquier otro
contenedor. Restringirás esto más tarde en el laboratorio, y el uso de
redes virtuales separadas asegurará que un contenedor comprometido no pueda
evadir estas restricciones a nivel de red.

El archivo ``zook.conf configura solo un servicio HTTP (a través de
la línea `http_svcs`), `zookfs`, que tanto sirve archivos
estáticos como ejecuta scripts dinámicos. Más adelante en este laboratorio, necesitarás
ejecutar múltiples servicios HTTP, lo que puedes hacer listando todos ellos,
separados por coma, en la línea `http_svcs`; por ejemplo,
`http_svcs = first,second,third`.

El servicio `zookfs` funciona
invocando el ejecutable `zookfs`, que se ejecuta en el directorio
`/app` en el contenedor conectado a `lxcbr = 1`
(y por tanto con dirección IP `10.1.1.4`).

Las líneas `fwrule` que ves comentadas en la descripción del servicio `zookfs`
en `zook.conf`
especifican filtros que controlan la comunicación a ese contenedor:

```
[zookfs]
    cmd = zookfs
    url = .*
    dir = /app
    lxcbr = 1
    port = 8081
    ## Filter rules are inserted in the order they appear in this file.
    ## Thus, in the below example (commented out initially) the first
    ## filters applied are the ACCEPT ones, and then the REJECT one.
    ## Use `iptables -nvL INPUT' on the appropriate container to see all
    ## the filters that are in effect on that container.
    # fwrule = -s main -j ACCEPT
    # fwrule = -s echo -j ACCEPT
    # fwrule = -j REJECT

```

Por ejemplo, las reglas comentadas permiten paquetes de los contenedores `main`
y `echo`, pero bloquean todos los otros paquetes. Cambiarás
estas reglas (y definirás reglas similares para otros contenedores)
mientras separamos privilegios más zookws.

Comenzaremos a separar privilegios más el servicio `zookfs` que
maneja tanto archivos estáticos como scripts dinámicos. Aunque se ejecuta en un contenedor,
algunos scripts de Python podrían tener fácilmente agujeros de seguridad; un script de Python vulnerable
podría ser engañado para eliminar archivos estáticos importantes que el servidor está
sirviendo. Por el contrario, el código de servicio de archivos estáticos podría ser engañado para servir
las bases de datos usadas por los scripts de Python, como person.db
y transfer.db. Una mejor organización es dividir zookfs
en dos servicios, uno para archivos estáticos y el otro para scripts de Python,
ejecutándose como usuarios diferentes.

>**Ejercicio 2.**
>Modifica zook.conf para reemplazar `zookfs` con
dos servicios separados, `dynamic` y `static`.
Ambos deberían usar `cmd = zookfs`.
>
>`dynamic` debería ejecutar solo `/zoobar/index.cgi`
(que ejecuta todos los scripts de Python), pero no debería servir ningún archivo
estático.
static debería servir archivos estáticos pero no ejecutar nada.
>
>Para eliminar el contenedor `zookfs` para que `zookld.py`
no lo inicie, ejecuta ./zookclean.py zookfs.
>
>Ejecuta los servicios dynamic y static en diferentes redes virtuales.
>
>Esta separación requiere que zookd determine cuál
servicio debería manejar una solicitud particular.
Puedes usar el filtrado de URL de `zookws` para hacer esto,
sin modificar la aplicación o las URLs que usa.
Los filtros de URL están especificados en zook.conf,
y soportan expresiones regulares.
Por ejemplo, url = .* coincide con todas las solicitudes, mientras que
url = /zoobar/(abc|def)\.html coincide con solicitudes
a /zoobar/abc.html y /zoobar/def.html.
>
>Para este ejercicio, solo deberías modificar zook.conf; no modifiques código C o
Python.
>
>Ejecuta make check-lab2 para verificar que
tu configuración modificada pase nuestras pruebas.

Nos gustaría controlar con quién dynamic y static pueden comunicarse. Por
ejemplo, incluso si static fuera comprometido, queremos que el atacante sea
incapaz de comunicarse con dynamic, haciendo más difícil para el atacante
comprometer dynamic también. Por tanto, nos gustaría configurar reglas de
firewall en cada contenedor para hacer cumplir este aislamiento. Usaremos
[iptables](https://wiki.archlinux.org/index.php/iptables)
para insertar reglas de filtro en cada contenedor, para que static solo
acepte paquetes de main (que ejecuta zookd). Esto asegura
que dynamic no pueda enviar paquetes directamente a static.
Similarmente, dynamic debería solo aceptar paquetes de main,
y no de static. Configurar reglas de seguridad como estas es
a menudo referido como segregación de red.

>**Ejercicio 3.**
>Escribe entradas fwrule apropiadas
para main, static, y dynamic para limitar la
comunicación como se especifica arriba.
>
>Si obtienes los filtros incorrectos, podrías ser incapaz de conectarte con cualquier
contenedor. Puedes resetear el firewall para permitir toda
comunicación deteniendo e iniciando los contenedores de nuevo,
usando zookstop.py seguido de zookld.py.

## Interludio: Librería RPC

En esta parte, separarás privilegios de la aplicación zoobar
en sí en varios procesos, ejecutándose en diferentes contenedores. Nos gustaría
limitar el daño de cualquier bug futuro que surja. Es decir, si una pieza de
la aplicación `zoobar` tiene un bug explotable, nos gustaría prevenir que un
atacante use ese bug para entrar en otras partes de la aplicación
zoobar.

Un desafío al dividir la aplicación `zoobar` en varios contenedores
es que los procesos dentro de los contenedores deben tener una manera de comunicarse entre
ellos. Primero estudiarás una librería de Remote Procedure Call (RPC) que permite
a los procesos comunicarse. Luego, usarás esa librería para
separar `zoobar` en varios procesos, cada uno dentro de su propio contenedor,
que se comunican usando RPC.

Para ilustrar cómo se podría usar nuestra librería RPC, hemos implementado un servicio
"echo" simple para ti, en zoobar/echo-server.py. Este servicio es
invocado por zookld y se ejecuta dentro de su propio contenedor; busca
la sección echo de zook.conf para ver cómo se inicia.

echo-server.py está implementado definiendo una clase RPC
EchoRpcServer que hereda de RpcServer, que a su vez
viene de zoobar/rpclib.py. La clase RPC EchoRpcServer
define los métodos que el servidor soporta, y rpclib invoca esos
métodos cuando un cliente envía una solicitud. El servidor define un método simple que
hace echo de la solicitud de un cliente.

echo-server.py inicia el servidor llamando a
run\_fork(port). Esta función escucha en un
socket TCP. El puerto viene del argumento, que en
este caso es 8081 (especificado en zook.conf).
Cuando un cliente se conecta a este socket, la función hace fork del proceso
actual. Una copia del proceso recibe mensajes y responde en
la conexión recién abierta, mientras que el otro proceso escucha otros
clientes que podrían abrir el socket.

También hemos incluido un cliente simple de este servicio echo como parte
de la aplicación web Zoobar. En particular, si vas a la
URL /zoobar/index.cgi/echo?s=hello, la solicitud se enruta
a zoobar/echo.py. Ese código usa el cliente RPC (implementado
por rpclib) para conectarse al servicio echo en (dirección IP del host,
puerto). El cliente busca la (dirección IP del host, puerto)
en zook.conf. El cliente invoca la operación echo. Una vez que
recibe la respuesta del servicio echo, retorna una página web conteniendo
la respuesta con echo.

El código del lado cliente RPC en rpclib está implementado por el
método call de la clase RpcClient. Este método
formatea los argumentos en una cadena, escribe la cadena en la conexión
al servidor, y espera una respuesta (una cadena). Al recibir la
respuesta, call parsea la cadena, y retorna los resultados al
llamador.

## Parte 2: Separar privilegios del servicio de login en Zoobar

Ahora usaremos la librería RPC para mejorar la seguridad de las
contraseñas de usuario almacenadas en la aplicación web Zoobar. Ahora mismo, un adversario que
explota una vulnerabilidad en cualquier parte de la aplicación Zoobar puede obtener todas las
contraseñas de usuario de la base de datos person.

El primer paso hacia proteger las contraseñas será crear un servicio
que maneje contraseñas de usuario y cookies, para que solo ese servicio
pueda acceder a ellas directamente, y el resto de la aplicación Zoobar no pueda.
En particular, queremos separar el código que maneja la autenticación de usuario
(i.e., contraseñas y tokens) del resto del código de la aplicación. La aplicación
zoobar actual almacena todo sobre el usuario (su perfil,
su balance de zoobar, y información de autenticación) en la tabla Person
(ver zoodb.py). Queremos mover la información de autenticación fuera de
la tabla Person a una tabla Cred separada (Cred significa
Credentials), y mover el código que accede a esta información de
autenticación (i.e., auth.py) a un servicio separado.

Nota que no es completamente necesario dividir los datos en
tablas separadas para seguridad: cada contenedor terminaría con su
propia copia de la base de datos, y no tendría datos en las partes de la
base de datos que nunca pobló. Dividimos los datos en tablas
separadas de todos modos, porque ayuda a entender cómo dividir los servicios
correctamente.

Específicamente, tu trabajo será el siguiente:

* Decide qué interfaz debería proporcionar tu servicio de autenticación
 (i.e., qué funciones ejecutará para clientes). Mira el
 código en login.py y auth.py, y decide qué
 necesita ejecutarse en el servicio de autenticación, y qué puede ejecutarse en
 el cliente (i.e., ser parte del resto del código zoobar). Ten
 en mente que tu objetivo es proteger tanto contraseñas como tokens.
 Hemos proporcionado stubs RPC iniciales para el cliente en el archivo
 zoobar/auth\_client.py.
* Crea un nuevo servicio auth para autenticación de usuario, siguiendo las líneas de
 echo-server.py. Hemos proporcionado un archivo inicial para
 ti, zoobar/auth-server.py, que deberías modificar para
 este propósito. La implementación de este servicio debería usar las
 funciones existentes en auth.py.
* Modifica zook.conf para iniciar el auth-server
 apropiadamente (en un contenedor en una red virtual diferente).
* Divide las credenciales de usuario (i.e., contraseñas y tokens) de
 la base de datos Person en una base de datos Cred
 separada, almacenada en /zoobar/db/cred. No mantengas ninguna
 contraseña o token en la base de datos Person antigua.
* Modifica el código de login en login.py para invocar tu
 servicio auth en lugar de llamar a auth.py directamente.

>**Ejercicio 4.**
>Implementa separación de privilegios para autenticación de usuario, como se describe arriba.
>
>Un buen punto de partida sería primero dividir las credenciales
originalmente almacenadas en la base de datos Person en una base de datos
Cred separada, pero aún hacer todo en el servicio
dynamic. No olvides crear una entrada regular de base de datos Person
para usuarios recién registrados.
>
>Una vez que eso funcione, agrega llamadas de función explícitas entre el código que
esperas que aún viva en el servicio dynamic (que no
toca Cred) y las funciones que eventualmente moverás
al auth-server (que sí toca Cred). Asegúrate
de que esto funcione solo con funciones primero, sin mover realmente el código
a un auth-server separado.
>
>Finalmente, configura auth-server.py para ejecutar el código manejando la
base de datos Cred, y convierte las llamadas de función del paso
anterior en RPCs reales al auth-server.
>
>Ejecuta make check-lab2 para verificar que
tu servicio de autenticación con separación de privilegios pase nuestras pruebas.

>Ejercicio 5.
Especifica las entradas fwrule apropiadas para auth.

Ahora, mejoraremos aún más la seguridad de las contraseñas, usando
hashing y salting. El código de autenticación actual almacena una copia
exacta de la contraseña del usuario en la base de datos. Así, si un adversario
de alguna manera obtiene acceso al archivo cred.db, todas las contraseñas de
usuario estarán inmediatamente comprometidas. ¡Peor aún, si los usuarios tienen
la misma contraseña en múltiples sitios, el adversario podrá
comprometer las cuentas de usuario allí también!

El hashing protege contra este ataque, almacenando un hash de la
contraseña del usuario (i.e., el resultado de aplicar una función hash a la contraseña),
en lugar de la contraseña misma. Si la función hash es difícil de
invertir (i.e., es un hash criptográficamente seguro), un adversario no
podrá obtener directamente la contraseña del usuario. Sin embargo, un servidor
aún puede verificar si un usuario proporcionó la contraseña correcta durante el login:
solo hará hash de la contraseña del usuario, y verificará si el valor hash
resultante es el mismo que se almacenó previamente.

Una debilidad con el hashing es que un adversario puede construir una tabla
gigante (llamada "rainbow table"), conteniendo los hashes de todas las contraseñas
posibles. Entonces, si un adversario obtiene la contraseña con hash de alguien,
el adversario puede simplemente buscarla en su tabla gigante, y obtener la
contraseña original.

Para derrotar el ataque de rainbow table, la mayoría de sistemas usan *salting*.
Con salting, en lugar de almacenar un hash de la contraseña, el servidor
almacena un hash de la contraseña concatenada con una cadena
generada aleatoriamente (llamada salt). Para verificar si la contraseña es correcta, el servidor
concatena la contraseña proporcionada por el usuario con el salt, y verifica si el
resultado coincide con el hash almacenado. Nota que, para que esto funcione, ¡el servidor
debe almacenar el valor salt usado para calcular originalmente el hash con salt!
Sin embargo, debido al salt, el adversario ahora tendría que generar
una tabla rainbow separada para cada valor salt posible. Esto aumenta
enormemente la cantidad de trabajo que el adversario tiene que realizar para
adivinar contraseñas de usuario basándose en los hashes.

Una consideración final es la elección de la función hash. La mayoría de funciones
hash, como MD5 y SHA1, están diseñadas para ser rápidas. Esto significa que
un adversario puede probar muchas contraseñas en un período corto de tiempo, ¡lo que
no es lo que queremos! En su lugar, deberías usar una función tipo hash especial
que esté explícitamente diseñada para ser *lenta*. Un buen ejemplo de tal
función hash es [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2),
que significa Password-Based Key Derivation Function (versión 2).

>Ejercicio 6.
>Implementa hashing y salting de contraseñas en tu servicio de autenticación.
En particular, necesitarás extender tu tabla Cred para incluir
una columna salt; modifica el código de registro para elegir un salt
aleatorio, y para almacenar un hash de la contraseña junto con el salt, en lugar
de la contraseña misma; y modifica el código de login para hacer hash de la contraseña
proporcionada junto con el salt almacenado, y compararla con el hash
almacenado. No elimines la columna password de la tabla Cred
(la verificación para el ejercicio 5 requiere que esté presente); puedes almacenar
la contraseña con hash en la columna password existente.
>
>Para implementar hashing PBKDF2, puedes usar el
[módulo Python PBKDF2](https://www.dlitz.net/software/python-pbkdf2/). 
Aproximadamente, deberías importar pbkdf2, y luego hacer hash de
una contraseña usando pbkdf2.PBKDF2(password, salt).hexread(32).
Hemos proporcionado una copia de pbkdf2.py en el directorio
zoobar. No uses la función random.random para generar un salt
ya que [la documentación del módulo random](https://docs.python.org/3/library/random.html)
establece que no es criptográficamente seguro. Una alternativa segura es
la función os.urandom.
>
>Ejecuta make check-lab2 para verificar que tu
código de hashing y salting pase nuestras pruebas. Ten en mente que nuestras pruebas
no son exhaustivas.

Un efecto secundario sorprendente de usar una función hash muy computacionalmente costosa
como PBKDF2 es que un adversario ahora puede usar esto
para lanzar ataques de denegación de servicio (DoS) en la CPU del servidor.
Por ejemplo, el popular framework web Django publicó un
[aviso de seguridad](https://www.djangoproject.com/weblog/2013/sep/15/security/) 
sobre esto, señalando que si un adversario trata de iniciar
sesión en alguna cuenta proporcionando una contraseña muy grande (1MB de tamaño),
el servidor pasaría un minuto entero tratando de calcular PBKDF2 en esa
contraseña. La solución de Django es limitar las contraseñas proporcionadas a máximo 4KB
de tamaño. Para este laboratorio, no requerimos que manejes tales ataques DoS.

## Parte 3: Separar privilegios del banco en Zoobar

Finalmente, queremos proteger el balance de `zoobar` de cada usuario de
adversarios que podrían explotar algún bug en la aplicación Zoobar.
Actualmente, si un adversario explota un bug en la aplicación principal Zoobar,
puede robar los zoobars de cualquier otra persona, y esto ni siquiera aparecería
en la base de datos Transfer si quisiéramos auditar las cosas más tarde.

Para mejorar la seguridad de los balances de zoobar, nuestro plan es similar a lo que
hiciste arriba en el servicio de autenticación: dividir la información de
balance de `zoobar` en una base de datos Bank separada, y configurar
un servicio bancario, cuyo trabajo es realizar operaciones en la
nueva base de datos Bank y la base de datos Transfer existente.
Mientras solo el servicio bancario pueda modificar las bases de datos Bank
y Transfer, los bugs en el resto de la aplicación Zoobar
no deberían dar a un adversario la capacidad de modificar balances de zoobar, y
asegurará que todas las transferencias se registren correctamente para futuras auditorías.

>**Ejercicio 7.**
>Separa privilegios de la lógica bancaria en un servicio bancario separado, siguiendo las
líneas del servicio de autenticación. Tu servicio debería implementar
las funciones transfer y balance, que actualmente están
implementadas por bank.py y llamadas desde varios lugares en el
resto del código de la aplicación.
>
>Deberías dividir la información de balance de `zoobar` en
una base de datos Bank separada (en zoodb.py);
implementar el servidor bancario modificando bank-server.py;
agregar el servicio bancario a zook.conf;
crear stubs RPC del cliente para invocar el servicio bancario;
y modificar el resto del código de la aplicación para invocar los stubs
RPC en lugar de llamar a las funciones de bank.py directamente.
>
>No olvides manejar el caso de creación de cuenta, cuando el nuevo usuario
necesita obtener 10 zoobars iniciales. Esto puede requerir que cambies la
interfaz del servicio bancario.
>
>Ejecuta make check-lab2 para verificar que
tu servicio bancario con separación de privilegios pase nuestras pruebas.

Finalmente, necesitamos arreglar un problema más con el servicio bancario.
En particular, un adversario que puede acceder al servicio bancario (i.e.,
puede enviarle solicitudes RPC) puede realizar transferencias desde la cuenta de
*cualquiera* a la suya propia. Por ejemplo, puede robar 1 `zoobar` de cualquier víctima
simplemente emitiendo una solicitud RPC transfer(victim, adversary, 1).
El problema es que el servicio bancario no tiene idea de quién está invocando la
operación de transferencia. Algunas librerías RPC proporcionan autenticación,
pero nuestra librería RPC es bastante simple, así que tenemos que agregarla explícitamente.

Para autenticar al llamador de la operación de transferencia,
requeriremos que el llamador proporcione un argumento token extra,
que debería ser un token válido para el remitente. El servicio bancario debería
rechazar transferencias si el token es inválido.

>**Ejercicio 8.**
>Agrega autenticación al RPC de transferencia en el servicio bancario.
El token del usuario actual es accesible como g.user.token.
¿Cómo debería el banco validar el token proporcionado?

>**Ejercicio 9.**
Especifica las entradas fwrule apropiadas para el servicio
bancario.

## Parte 4: Sandboxing del lado del servidor para perfiles ejecutables

En esta parte final, implementarás sandboxing para perfiles ejecutables,
lo cual es desafiante porque necesitamos aislar los perfiles de diferentes
usuarios entre sí y del resto del sistema.

Como ejemplo, aquí está el tipo de funcionalidad que nos gustaría soportar
con perfiles ejecutables. Un usuario podría configurar su perfil al siguiente
código (que puedes encontrar en profiles/hello-user.py):

```
#!python
import time
import api
print('Hello, <i>', api.call('get\_visitor'), '</i>')
print('<p>Current time:', time.time())

```

Cada vez que alguien vea el perfil de este usuario en Zoobar, el servidor
ejecutará este código Python, y mostrará la salida resultante como si fuera
el perfil del usuario. Por ejemplo, si el usuario alice ve este
perfil, podría ver el siguiente resultado en su pantalla:

> 
> **Hello**,  *alice*
>
>**Current time: 1708447443.7460613**
> 

La implementación inicial que proporcionamos para perfiles ejecutables ejecuta el
código del perfil directamente en el proceso Python del servidor, lo que significa que
un usuario malicioso podría manipular el servidor inyectando código
arbitrario a través de su perfil.

Usaremos WebAssembly para ejecutar el perfil ejecutable de un usuario en aislamiento,
para que el perfil ejecutable de un usuario no pueda manipular los perfiles
de otros usuarios. WebAssembly es útil aquí porque hace que crear
un nuevo entorno de ejecución aislado sea ligero, y la creación puede
realizarse fácilmente bajo demanda, en contraste con los contenedores (crear
contenedores es algo intensivo en recursos y requiere privilegios especiales
que no están disponibles para un contenedor mismo).

Para aislar código Python arbitrario usando WebAssembly, hemos construido una
versión del intérprete Python que puede ejecutarse dentro de un módulo
WebAssembly. Luego ejecutaremos todo este intérprete Python, más el
código de perfil Python proporcionado por el usuario, dentro del módulo WebAssembly.
Esta versión de Python está instalada en
/usr/local/share/Python-3.11.0-wasm32-wasi-16 dentro de tu VM;
python.wasm es el ejecutable del intérprete Python de nivel superior,
y los otros archivos (e.g., todos los archivos bajo lib) son
varias librerías que el intérprete Python en sandbox podría necesitar
acceder en tiempo de ejecución.

Si quieres tener una idea de este intérprete Python WebAssembly aislado,
puedes ejecutarlo desde la línea de comandos en tu VM como sigue:

```
student@6566-v24:~/lab$ wasmtime run --mapdir=/::/usr/local/share/Python-3.11.0-wasm32-wasi-16 -- /usr/local/share/Python-3.11.0-wasm32-wasi-16/python.wasm
Python 3.11.0 (tags/v3.11.0-dirty:deaf509, Oct 29 2022, 07:56:14) [Clang 14.0.4 (https://github.com/llvm/llvm-project 29f1039a7285a5c3a9c353d05414 on wasi
Type "help", "copyright", "credits" or "license" for more information.
>>> 

```

El comando de arriba usa el
[runtime WebAssembly wasmtime](https://docs.wasmtime.dev/)
para ejecutar
el intérprete Python desde /usr/local/share/Python-3.11.0-wasm32-wasi-16/python.wasm.
El argumento --mapdir le dice a wasmtime que dé al módulo WebAssembly
acceso al directorio /usr/local/share/Python-3.11.0-wasm32-wasi-16
como / (el directorio raíz) dentro del módulo. Esto efectivamente
monta el directorio /usr/local/share/Python-3.11.0-wasm32-wasi-16 del host
como / dentro del módulo aislado.

Dado que los perfiles ejecutables son una parte algo peligrosa del diseño general del
sistema (estamos ejecutando código arbitrario, después de todo), ejecutaremos
estos perfiles ejecutables en un contenedor separado dedicado a
ese propósito, como en las partes anteriores de este laboratorio. Esto no
aisla los perfiles entre sí, pero al menos proporciona cierto grado
de aislamiento entre todos los perfiles ejecutables y el resto del
sistema.

Deberías familiarizarte con el directorio profiles/,
que contiene varios perfiles ejecutables que usarás como ejemplos:

* profiles/hello-user.py es un perfil simple
 que imprime de vuelta el nombre del visitante cuando el
 código del perfil se ejecuta, junto con la hora actual.
* profiles/visit-tracker.py lleva registro de la
 última vez que cada visitante miró el perfil, e
 imprime la hora de la última visita (si es que existe).
* profiles/last-visits.py registra los últimos tres
 visitantes al perfil, y los imprime.
* profiles/xfer-tracker.py imprime la última
 transferencia de `zoobar` entre el dueño del perfil y el visitante.
* profiles/granter.py le da al visitante un zoobar.
 Para asegurar que los visitantes no puedan robar rápidamente todos los zoobars de
 un usuario, este perfil otorga un `zoobar` solo si el dueño del
 perfil tiene algunos zoobars restantes, el visitante tiene menos de 20
 zoobars, y ha pasado al menos un minuto desde la última
 vez que ese visitante obtuvo un `zoobar` de este perfil.

La pieza final de código es zoobar/profile-server.py: un
servidor RPC que acepta solicitudes para ejecutar el código de perfil de algún usuario,
y retorna la salida de ejecutar ese código. Al ejecutar un
perfil, profile-server.py configura un servidor RPC que
permite al código del perfil obtener acceso a cosas fuera del
sandbox, como los balances de `zoobar` de diferentes usuarios.
El ProfileAPIServer implementa esta interfaz;
profile-server.py hace fork de un proceso separado
para ejecutar el ProfileAPIServer.

Un desafío es que el servicio de perfil realiza rpc_xfer
desde la cuenta del dueño del perfil, lo que (dependiendo de tu diseño para
separar privilegios del banco en el ejercicio 8 de arriba) puede requerir un token
para el dueño. No puedes simplemente agregar un RPC al servicio auth
para obtener un token para el dueño del perfil, porque entonces cualquier servicio podría
pedirlo; queremos que solo el servicio de perfil pueda
hacer esta transferencia. Similarmente, no podemos agregar un RPC al servicio
bancario para hacer una transferencia desde la cuenta de cualquiera sin un token, ya que
eso rompería las garantías de seguridad para el ejercicio 8.

Para los propósitos de este laboratorio, queremos hacer la transferencia desde la cuenta del
dueño del perfil solo si la solicitud vino del servicio de
perfil. Así, el servicio bancario debe ser capaz de autenticar
que una solicitud vino del servicio de perfil. Para ayudarte
a hacerlo, rpcsrv.py proporciona el nombre del servicio llamador en
self.caller, basado en la dirección IP de la conexión desde
la cual recibió la solicitud.

Para empezar, necesitarás agregar el servicio de perfil a tu
zook.conf. Ejecuta el servicio en su propio contenedor y en su
propio enlace de red.

>**Ejercicio 10.**
>Agrega profile-server.py a tu servidor web, e implementa la
lógica en ProfileServer.rpc\_run() para ejecutar correctamente
perfiles ejecutables en un sandbox WebAssembly. Podrías
encontrar útil referirte a la documentación para los
[bindings Python de wasmtime](https://bytecodealliance.github.io/wasmtime-py/). 
También hay varias sugerencias en los comentarios en profile-server.py.
>
>Asegúrate de que tu sitio Zoobar pueda soportar todos los cinco perfiles.
>
>Ejecuta make check-lab2 para verificar que tu
configuración modificada pase nuestras pruebas. El caso de prueba crea algunas
cuentas de usuario, almacena uno de los perfiles Python en el perfil de un
usuario, hace que otro usuario vea ese perfil, y verifica que el otro
usuario vea la salida correcta.
>
>Si encuentras problemas con las pruebas de make check-lab2, puedes
revisar /tmp/html.out para la salida html de los perfiles.

El diseño de arriba puede tener varios problemas de seguridad. Primero, es
importante que el código de perfil en sandbox no pueda manipular el estado
de los perfiles de otros usuarios, y no pueda manipular el código de librería del sistema
para el intérprete Python mismo. Segundo, es importante que
un perfil malicioso no pueda hacer loop para siempre.

>**Ejercicio 11.**
>Modifica más rpc_run
en profile-server.py para que el sandbox prevenga que el código del perfil
corrompa archivos de librería del sistema y para que el código en sandbox
no pueda ejecutarse por más de 5 segundos.
>
>Nota que si los archivos de librería se corrompen por las pruebas, podrías necesitar
re-crear el contenedor para limpiar (o limpiar manualmente). Las pruebas
intentan crear un archivo /lib/testfile para ver si el directorio de librería
puede ser corrompido.
>
>Ejecuta make check-lab2 para ver si tu
implementación pasa nuestros casos de prueba.

>**Ejercicio 12.**
>Especifica las entradas fwrule apropiadas para profile
y otros servicios. Por ejemplo, profile no debería poder
comunicarse con auth.

¡Ya terminaste con el sandbox básico!

¡Terminaste!
Ejecuta make handin.zip y sube el archivo
handin.zip resultante 