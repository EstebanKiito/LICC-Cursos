## Demo

Este es un ejemplo de distintas formas para compilar los códigos.
El objetivo es demostrar la diferencia y facilidad de compilar con **make** vs **gcc**, además de mostrar cómo usar distintos archivos `.txt` de input.


Paso 1: Estar en el directorio `Demo`. Pueden utilizar el siguiente comando para asegurarse:

```
pwd
```
y que la respuesta sea algo del estilo `.../Demo`
### GCC:
Paso 3: primero vamos a compilar con gcc
```
gcc src/HelloWorld/Objects/struct.c src/HelloWorld/main.c -o HelloWorld
```
Paso 4: Correr el código.
```
./HelloWorld input_0.txt output.txt
```
Prueba cambiando el archivo de input por los otros que se encuentran en el directorio


### Make:
Paso 3: primero vamos a compilar con el archivo make que se entregó
```
make
```
Paso 4: Correr el código.
```
./HelloWorld input_1.txt output.txt
```
Prueba cambiando el archivo de input por los otros que se encuentran en el directorio
