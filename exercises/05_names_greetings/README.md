# Programa de los nombres
- Este programa saludará a los nombres ingresados por el usuario
- En primer lugar dirá cuantos nombres el usuario envió
- Luego procederá a saludar a cada nombre indicando la letra con la que inicia en minúscula y la letra con la que termina

Los resultados de ayuda al utilizar `-h` o `--help` se obtendrá lo siguiente:
```bash
python names.py -h
usage: names.py [-h] [str ...]

Programa que te dice con que letra empieza y con que letra termina tu nombre

positional arguments:
  str         Nombre(s) a ser saludado(s) (default: None)

options:
  -h, --help  show this help message and exit
```

Si el usuario ingresa un solo nombre:
```bash
$ python names.py Renzo
Hola soy el saludador me enviaste 1 nombre
Hola Renzo, tu nombre inicia con la letra r y termina con la letra o.
```

Si el usuario ingresa dos nombres:
```bash
$ python names.py Renzo Alisson
Hola soy el saludador me enviaste 2 nombres
Hola Renzo, tu nombre inicia con la letra r y termina con la letra o.
Hola Alisson, tu nombre inicia con la letra a y termina con la letra n.
```

Si el usuario ingresa tres nombres:
```bash
$ python names.py Renzo Alisson Carlos
Hola soy el saludador me enviaste 3 nombres
Hola Renzo, tu nombre inicia con la letra r y termina con la letra o.
Hola Alisson, tu nombre inicia con la letra a y termina con la letra n.
Hola Carlos, tu nombre inicia con la letra c y termina con la letra s.
```

Y así sucesivamente mientras más nombres ingrese el usuario.