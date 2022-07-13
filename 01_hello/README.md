# Chapter 1: Hola, Mundo! (Adaptado de Hello, World! )

Escriba un programa para saludar con entusiasmo al mundo:

```
$ ./hello.py
Hola, Mundo!
```

El programa también debería aceptar un nombre dado como un parámetro `--nombre` opcional:

```
$ ./hello.py --nombre Universe
Hola, Universe!
```

El programa debe producir documentación para `-h` o `--help`:

```
$ ./hello.py -h
usage: hello.py [-h] [-n nombre]

Decir hola

options:
  -h, --help            show this help message and exit
  -n nombre, --nombre nombre
                        Nombre a saludar

```

Ejecute `pytest -xv test.py` (o `make test`) para asegurarse de pasar todas las pruebas:

```
$ make test
pytest -xv test.py
============================= test session starts ======================================================================
...
collected 5 items                                                                                                                            

test.py::test_existencia PASSED                                                                                   [ 20%]
test.py::test_corrida PASSED                                                                                      [ 40%]
test.py::test_ejecutable PASSED                                                                                   [ 60%]
test.py::test_uso PASSED                                                                                          [ 80%]
test.py::test_entrada PASSED                                                                                      [100%]

============================================================= 5 passed in 0.25s ========================================
```
