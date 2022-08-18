# Programa de las tablas de multiplicación
- Este programa tendrá como objetivo la puesta en práctica de la utilización de un `for` dentro de un `for`
- Entonces este programa funcionará de la forma que generará los resultados de las tablas de multiplicar desde el 1 
hasta el número definido por el usuario
- Luego se puede tener un argumento `-m` o `--maximo` para definir el máximo número de la tabla de multiplicación 
- El último número de cada línea impresa de las tablas será el total sumado de la tabla definida 
- La última línea será una línea de total acumulado

Los resultados de ayuda al utilizar `-h` o `--help` se obtendrá lo siguiente:
```bash
$ python multiplication_table.py --help
usage: multiplication_table.py [-h] [-m int] int

Generador de tablas de multiplicación

positional arguments:
  int                   Hasta que tabla se generará

options:
  -h, --help            show this help message and exit
  -m int, --maximo int  Hasta que número será la tabla (default: 10)
```

Si el usuario ingresa 1 se obtendrán los siguientes resultados, donde al final se tendrá el resultado de la suma de los 
números multiplicados

Y la última línea será el total que en este caso será el mismo del de la línea
Recordemos que `1+2+3+4+5+6+7+8+9+10=55`
```bash
$ python multiplication_table.py 1
    1     2     3     4     5     6     7     8     9    10    55
total    55
```

Si, en cambio, escribe 5 se tendrá:
Recordemos que `55+110+165+220+275=825`

```bash
$ python multiplication_table.py 5
    1     2     3     4     5     6     7     8     9    10    55
    2     4     6     8    10    12    14    16    18    20   110
    3     6     9    12    15    18    21    24    27    30   165
    4     8    12    16    20    24    28    32    36    40   220
    5    10    15    20    25    30    35    40    45    50   275
total   825
```

Si utilizamos la bandera `-m` o `--maximo` con las líneas anteriores se tendrían resultados como:
Con un valor de 5
```bash
$ python multiplication_table.py 1 -m 5
    1     2     3     4     5     6     7     8     9    10    55
total    55
```

Con un valor de 12
```bash
python multiplication_table.py 5 -m 12
    1     2     3     4     5     6     7     8     9    10    11    12    78
    2     4     6     8    10    12    14    16    18    20    22    24   156
    3     6     9    12    15    18    21    24    27    30    33    36   234
    4     8    12    16    20    24    28    32    36    40    44    48   312
    5    10    15    20    25    30    35    40    45    50    55    60   390
total  1170
```
