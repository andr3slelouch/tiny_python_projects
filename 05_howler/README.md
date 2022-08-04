# Howler

Escriba un programa que escriba en mayúsculas el texto dado:

```
$ ./howler.py 'El veloz zorro marrón salta sobre el perro perezoso.'
EL VELOZ ZORRO MARRÓN SALTA SOBRE EL PERRO PEREZOSO.
```

Si el texto nombra un archivo, escriba en mayúsculas el contenido del archivo:

```
$ ./howler.py ../inputs/fox.txt
EL VELOZ ZORRO MARRÓN SALTA SOBRE EL PERRO PEREZOSO.
```

Si no se le dan argumentos, imprima un breve uso:

```
$ ./howler.py
usage: howler.py [-h] [-o str] str
howler.py: error: the following arguments are required: str
```

Si la opción `-o` o `--outfile` está presente, escriba la salida en el archivo dado y no imprima nada:

```
$ ./howler.py ../inputs/fox.txt -o out.txt
```

Ahora debería haber un archivo `out.txt` con el contenido:

```
$ cat out.txt
EL VELOZ ZORRO MARRÓN SALTA SOBRE EL PERRO PEREZOSO.
```

Responda a `-h` o `--help` con un uso más largo:

```
$ ./howler.py -h
usage: howler.py [-h] [-o str] str

Howler (upper-cases input)

positional arguments:
  str                   Input string or file

optional arguments:
  -h, --help            show this help message and exit
  -o str, --outfile str
                        Output filename (default: )
```

Ejecute el conjunto de pruebas para asegurarse de que su programa funcione correctamente:

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 5 items

test.py::test_exists PASSED                                              [ 20%]
test.py::test_usage PASSED                                               [ 40%]
test.py::test_text_stdout PASSED                                         [ 60%]
test.py::test_text_outfile PASSED                                        [ 80%]
test.py::test_file PASSED                                                [100%]

============================== 5 passed in 0.40s ===============================
```
