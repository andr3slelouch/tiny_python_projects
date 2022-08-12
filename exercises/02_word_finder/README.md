# Buscador de palabras
- Contar cuantas veces la palabra se repite
- ~~Poder reemplazar la palabra buscada por otra y guardarla en el mismo archivo~~
- Poder exportar el nuevo archivo con las palabras reemplazadas
- Poder especificar si se busca una palabra o una parte de una palabra

Para realizar una búsqueda y contar una palabra en un archivo se lo puede realizar con la bandera `-w` o `--word`:
```
$ python finder.py ./inputs/pablito.txt -w Pablito
Pablito     4 ./inputs/pablito.txt
```

Se podrá realizar búsquedas en más de un archivo agregando mas archivos a la búsqueda como se mostrará a continuación, además se mostrará un total:
```
$ python finder.py ./inputs/pablito_1.txt ./inputs/pablito_2.txt -w Pablito
Pablito     4 ./inputs/pablito_1.txt
Pablito     3 ./inputs/pablito_2.txt
Pablito     7 total

```

También se pueden buscar palabras que son parte de otras palabras como por ejemplo si se busca `la` dentro del mismo 
archivo sin habilitar la bandera `-s` no se encontrará resultados:
```
$ python finder.py ./inputs/pablito.txt -w la
la        0 ./inputs/pablito.txt
```

Sin embargo si se habilita la bandera `-s` o `--substring`  se encontrarán 7 resultados:
```
$ python finder.py ./inputs/pablito.txt -w la -s
la        7 ./inputs/pablito.txt

```

Lo mismo puede repetirse para multiples archivos
```
$ python finder.py ./inputs/pablito_1.txt ./inputs/pablito_2.txt -w la -s
la        7 ./inputs/pablito_1.txt
la        2 ./inputs/pablito_2.txt
la        9 total

```

Se podrá también reemplazar la palabra buscada en nuevos archivos utilizando `-r` y la palabra que reemplazará y `-o` para especificar los archivos nuevos:
```
$ python finder.py ./inputs/pablito.txt -w Pablito -r Robertito -o ./outs/robertito.txt
Pablito     4 ./inputs/pablito.txt
```
Archivo pablito.txt
```
Pablito clavó un clavito ,

¿ qué clavito clavó Pablito ?

el clavito que clavó Pablito ,

era el clavito de Pablito .
```

Archivo robertito.txt generado
```
Robertito clavó un clavito ,

¿ qué clavito clavó Robertito ?

el clavito que clavó Robertito ,

era el clavito de Robertito .
```

También será posible reemplazar una palabra que pertenezca a otra:
```
$ python finder.py ./inputs/pablito.txt -w la -s -r ./outs/pablito_la.txt
la        7 ./inputs/pablito.txt

```

Archivo pablito_la.txt
```
Pablito cLAvó un cLAvito ,

¿ qué cLAvito cLAvó Pablito ?

el cLAvito que cLAvó Pablito ,

era el cLAvito de Pablito .
```

Los reemplazos también podrán ejecutarse en multiples archivos a la vez de la forma:
```
$ python finder.py ./inputs/pablito_1.txt ./inputs/pablito_2.txt ./inputs/pablito_3.txt -w Pablito -r Robertito -o ./outs/pablito_1.txt ./outs/pablito_2.txt ./outs/pablito_3.txt
Pablito     4 ./inputs/pablito_1.txt
Pablito     3 ./inputs/pablito_2.txt
Pablito     3 ./inputs/pablito_3.txt
Pablito    10 total
```

Si se lo ejecuta con la bandera substring será de la forma:
```
$ python finder.py ./inputs/pablito_1.txt ./inputs/pablito_2.txt ./inputs/pablito_3.txt -w Pablito -s -r Robertito -o ./outs/pablito_1.txt ./outs/pablito_2.txt ./outs/pablito_3.txt
Pablito     4 ./inputs/pablito_1.txt
Pablito     3 ./inputs/pablito_2.txt
Pablito     4 ./inputs/pablito_3.txt
Pablito    11 total

```

Ejecuta los tests para asegurar que el programa funciona correctamente

```
$ python -m pytest -xvv test.py 
============================= test session starts ==============================
...
collected 12 items                                                                                                                           

test.py::test_exists PASSED                                               [  8%]
test.py::test_usage PASSED                                                [ 16%]
test.py::test_bad_file PASSED                                             [ 25%]
test.py::test_empty PASSED                                                [ 33%]
test.py::test_one PASSED                                                  [ 41%]
test.py::test_more PASSED                                                 [ 50%]
test.py::test_sub_flag_one PASSED                                         [ 58%]
test.py::test_sub_flag_more PASSED                                        [ 66%]
test.py::test_replace_one_file_at_time PASSED                             [ 75%]
test.py::test_replace_one_file_at_time_substring PASSED                   [ 83%]
test.py::test_replace_multiple_files_at_time PASSED                       [ 91%]
test.py::test_replace_multiple_files_at_time_substring PASSED             [100%]

============================== 12 passed in 0.51s ===============================
```
