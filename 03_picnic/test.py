#!/usr/bin/env python3
"""tests for picnic.py"""

import os
from subprocess import getoutput

prg = 'solution.py'


# --------------------------------------------------
def test_existencia():
    """Verifica si existe el script a probarse"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_uso():
    """Probará la utilización de argumentos"""

    for flag in ['', '-h', '--help']:
        out = getoutput(f'python {prg} {flag}')
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_uno():
    """Un item"""

    out = getoutput(f'python {prg} papas')
    assert out.strip() == 'Tú estas trayendo papas.'


# --------------------------------------------------
def test_dos():
    """Dos items"""

    out = getoutput(f'python {prg} gaseosa "papas fritas"')
    assert out.strip() == 'Tú estas trayendo gaseosa y papas fritas.'


# --------------------------------------------------
def test_mas_de_dos():
    """Más de dos items"""

    arg = '"papas fritas" ensalada cupcakes "Pastel de seda francés"'
    out = getoutput(f'python {prg} {arg}')
    expected = ('Tú estas trayendo papas fritas, ensalada, '
                'cupcakes, y Pastel de seda francés.')
    assert out.strip() == expected


# --------------------------------------------------
def test_dos_ordenado():
    """Salida ordenada de dos elementos"""

    out = getoutput(f'python {prg} -o gaseosa dulces')
    assert out.strip() == 'Tú estas trayendo dulces y gaseosa.'


# --------------------------------------------------
def test_mas_de_dos_ordenado():
    """Salida ordenada de más de dos elementos"""

    arg = 'bananas manzanas helados cerezas'
    out = getoutput(f'python {prg} {arg} --ordenar')
    expected = 'Tú estas trayendo bananas, cerezas, helados, y manzanas.'
    assert out.strip() == expected
