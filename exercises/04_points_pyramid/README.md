# Programa de las pirámides
- Este programa tendrá como objetivo la puesta en práctica de la utilización de un `for` dentro de un `for`.
- Entonces este programa funcionará de la forma que generará distintos tipos de pirámides alineadas a la izquierda,
derecha y al centro.
- Se recibirá un argumento posicional de valor entero que definirá el tamaño de la pirámide. 
- El modo por defecto del programa será la alineada a la izquierda.
- Luego se puede tener un argumento `-m` o `--modo` para definir el modo de la aplicación y podrá recibir los 
argumentos `Izquierda`, `Derecha` y `Centro`, uno a la vez, dos a la vez o todos a la vez, lo que permitirá definir las 
pirámides a imprimirse y su orden en el caso de imprimirse más de una.
- También se podrá utilizar la bandera `-r` o `--reverse` que permitirá graficar la pirámide al revés es decir la base
primero y al final la punta. 
- Si se utiliza la bandera `-f` o `--full` que permitirá graficar la pirámide con su reverso, si la bandera `--reverse`
está activa se mostrará revertida. 
- Finalmente, se mostrará el conteo final de los puntos de las pirámides

Los resultados de ayuda al utilizar `-h` o `--help` se obtendrá lo siguiente:
```bash
$ python pyramid.py -h
usage: pyramid.py [-h] [-m [Modo ...]] [-f] [-r] int

Pirámides de puntos

positional arguments:
  int                   Tamaño de la o las pirámides

options:
  -h, --help            show this help message and exit
  -m [Modo ...], --modo [Modo ...]
                        Modo de la o las pirámides (default: ['Izquierda'])
  -f, --full            Imprime las pirámides con sus reversos completo (default: False)
  -r, --reverse         Define la bandera para revertir la impresión de las banderas (default: False)
```

Si el usuario ingresa 3 se obtendrán los siguientes resultados

Y la última línea será el total de puntos
```bash
python pyramid.py 3
*
**
***
total 6
```

Si, en cambio, escribe 5 se tendrá:

```bash
$ python pyramid.py 5
*
**
***
****
*****
total 15
```

Si utilizamos la bandera `-m` o `--modo` con las líneas anteriores se tendrían resultados como:
Con un valor de Derecha
```bash
$ python pyramid.py 3 -m Derecha
  *
 **
***
total 6
```

Con un valor de Centro
```bash
$ python pyramid.py 3 -m Centro
   *
  ***
 *****
*******
total 16
```

Si lo combinamos con dos modos se tendrá lo siguiente:
Con Derecha e Izquierda
```bash
$ python pyramid.py 3 -m Derecha Izquierda
  *
 **
***
*
**
***
total 12
```

Si se pone en diferente orden se tendrá:
```bash
$ python pyramid.py 3 -m Izquierda Derecha
*
**
***
  *
 **
***
total 12
```

Si se ingresan los tres:
```bash
$ python pyramid.py 3 -m Izquierda Centro Derecha
*
**
***
   *
  ***
 *****
*******
  *
 **
***
total 28
```

Al utilizar la bandera `-r` o `--reverse` las pirámides se imprimirá de forma reversa:
```bash
$ python pyramid.py 3 -m Derecha -r
***
 **
  *
total 6
```

```bash
$ python pyramid.py 3 -m Izquierda Derecha -r
***
**
*
***
 **
  *
total 12
```

```bash
$ python pyramid.py 3 -m Izquierda Centro Derecha -r
***
**
*
*******
 *****
  ***
   *
***
 **
  *
total 28

```

Al utilizar la bandera `-f` o `--full` se imprimirá la normal con su version reversa creando un rombo
```bash
$ python pyramid.py 3 -m Derecha -f
  *
 **
***
***
 **
  *
total 12
```

Si se combina con `-r` o `--reverse`:

```bash
$ python pyramid.py 3 -m Derecha -f -r
***
 **
  *
  *
 **
***
total 12
```

Lo mismo al tener con dos banderas:
```bash
$ python pyramid.py 3 -m Izquierda Derecha -f
*
**
***
***
**
*
  *
 **
***
***
 **
  *
total 24
```

Si se combina con `-r` o `--reverse`:
```bash
$ python pyramid.py 3 -m Izquierda Derecha -f -r
***
**
*
*
**
***
***
 **
  *
  *
 **
***
total 24
```

Finalmente, el comportamiento con tres modos sería:
```bash
$ python pyramid.py 3 -m Izquierda Centro Derecha -f
*
**
***
***
**
*
   *
  ***
 *****
*******
*******
 *****
  ***
   *
  *
 **
***
***
 **
  *
total 56
```

Si se combina con `-r` o `--reverse`:
```bash
$ python pyramid.py 3 -m Izquierda Centro Derecha -f -r
***
**
*
*
**
***
*******
 *****
  ***
   *
   *
  ***
 *****
*******
***
 **
  *
  *
 **
***
total 56
```






