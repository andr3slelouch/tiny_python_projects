# Jump the Five


Escriba un programa que codifique cualquier número en una cadena dada usando un algoritmo para "saltar el cinco" en un teclado telefónico estándar de EE. UU. de manera que "1" se convierta en "9", "4" se convierta en "6", etc.
El "5" y el "0" se intercambiarán entre sí.
Aquí está la tabla de sustitución completa:

```
1 => 9
2 => 8
3 => 7
4 => 6
5 => 0
6 => 4
7 => 3
8 => 2
9 => 1
0 => 5
```

Codifique solo los números y deje el resto del texto igual:

```
$ ./jump.py 867-5309
243-0751
```

Si no se le dan argumentos, presente un breve uso:

```
$ ./jump.py
usage: jump.py [-h] str
jump.py: error: the following arguments are required: str
```

Responda a `-h` o `--help` con un uso más largo:

```
$ ./jump.py -h
usage: jump.py [-h] str

Jump the Five

positional arguments:
  str         Input text

optional arguments:
  -h, --help  show this help message and exit
```

Ejecute el conjunto de pruebas para asegurarse de que su programa funcione correctamente:
```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 4 items

test.py::test_exists PASSED                                              [ 25%]
test.py::test_usage PASSED                                               [ 50%]
test.py::test_01 PASSED                                                  [ 75%]
test.py::test_02 PASSED                                                  [100%]

============================== 4 passed in 0.53s ===============================
```
