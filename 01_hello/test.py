#!/usr/bin/env python3
"""Pruebas para hello08_formatted.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './hello08_formatted.py'


# --------------------------------------------------
def test_existencia():
    """Verifica si existe el script a probarse"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_corrida():
    """Ejecuta las pruebas usando python3"""

    out = getoutput(f'python3 {prg}')
    assert out.strip() == 'Hola, Mundo!'


# --------------------------------------------------
def test_ejecutable():
    """Dirá 'Hola, Mundo! por defecto"""

    out = getoutput(prg)
    assert out.strip() == 'Hola, Mundo!'


# --------------------------------------------------
def test_uso():
    """Probará la utilización de argumentos"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_entrada():
    """Probará las entradas"""

    for val in ['Universe', 'Multiverse']:
        for option in ['-n', '--nombre']:
            rv, out = getstatusoutput(f'{prg} {option} {val}')
            assert rv == 0
            assert out.strip() == f'Hola, {val}!'
