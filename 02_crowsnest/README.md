# Nido del cuervo(Adaptado de Crow's Nest)


Escriba un programa que anuncie la aparición de algo "por la amura de babor" al capitán del barco.
Tenga en cuenta que necesitará diferenciar el artículo masculino("un") y el femenino("una") antes de cada palabra

```
$ ./crowsnest.py pulpo
¡Capitán, un pulpo por la amura de babor!
```

O "una" antes de una palabra que sea femenina:

```
$ ./crowsnest.py ballena
¡Capitán, una ballena por la amura de babor!
```

Sin argumentos, el programa debe imprimir un breve uso:

```
$ ./crowsnest.py
usage: crowsnest.py [-h] str
crowsnest.py: error: the following arguments are required: str
```

Debería imprimir un uso más largo para `-h` y `--help`:

```
$ ./crowsnest.py -h
usage: crowsnest.py [-h] str

Nido del cuervo -- Elige le artículo correcto

positional arguments:
  str         Una palabra

optional arguments:
  -h, --help  show this help message and exit
```

Un conjunto de pruebas aprobado se ve así:

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 6 items

test.py::test_existencia PASSED                                              [ 16%]
test.py::test_uso PASSED                                               [ 33%]
test.py::test_masculino PASSED                                           [ 50%]
test.py::test_masculino_mayuscula PASSED                                     [ 66%]
test.py::test_femenino PASSED                                               [ 83%]
test.py::test_femenino_mayuscula PASSED                                         [100%]

============================== 6 passed in 2.89s ===============================
```
