# Juego del Picnic

Escriba un programa que formatee correctamente los elementos que llevaremos a nuestro picnic.
Para un elemento, debe imprimir el elemento único:

```
$ ./picnic.py sanduches
Tú estas trayendo sanduches.
```

Para dos elementos, coloque "y" en el medio:

```
$ ./picnic.py sanduches papas
Tú estas trayendo sanduches y papas.
```

Para tres o más elementos, use comas y la letra "y":

```
$ ./picnic.py sanduches papas pastel
Tú estas trayendo sanduches, papas, y pastel.
```

Si el indicador `--ordenar` está presente, primero se deben ordenar los elementos:

```
$ ./picnic.py sanduches papas pastel --ordenar
Tú estas trayendo papas, pastel, y sanduches.
```

Si no se dan artículos, imprima un breve uso:

```
$ ./picnic.py
usage: picnic.py [-h] [-s] str [str ...]
picnic.py: error: the following arguments are required: str
```

Responde a `-h` y `--help` con un uso más largo:

```
$ ./picnic.py -h
usage: picnic.py [-h] [-s] str [str ...]

Picnic game

positional arguments:
  str           Item(s) to bring

optional arguments:
  -h, --help    show this help message and exit
  -s, --sorted  Sort the items (default: False)
```

Run the test suite to ensure your program is correct:

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 7 items

test.py::test_exists PASSED                                              [ 14%]
test.py::test_usage PASSED                                               [ 28%]
test.py::test_one PASSED                                                 [ 42%]
test.py::test_two PASSED                                                 [ 57%]
test.py::test_more_than_two PASSED                                       [ 71%]
test.py::test_two_sorted PASSED                                          [ 85%]
test.py::test_more_than_two_sorted PASSED                                [100%]

============================== 7 passed in 0.51s ===============================
```
