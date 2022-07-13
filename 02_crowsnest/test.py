#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './solution.py'
consonant_words = [
    'calamar', 'lenguado', 'pulpo', 'delfin', 'tiburón', 'pez', 'cangrejo'
]
vowel_words = ['tortuga', 'ballena', 'raya', 'almeja', 'pintarroja']
template = '¡Capitán, {} {} por la amura de babor!'


# --------------------------------------------------
def test_existencia():
    """Verifica si existe el script a probarse"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_uso():
    """Probará la utilización de argumentos"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_masculino():
    """pulpo -> un pulpo"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('un', word)


# --------------------------------------------------
def test_masculino_mayuscula():
    """Pulpo -> un Pulpo"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word.title()}')
        assert out.strip() == template.format('un', word.title())


# --------------------------------------------------
def test_femenino():
    """ballena -> una ballena"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('una', word)


# --------------------------------------------------
def test_femenino_mayuscula():
    """ballena -> una Ballena"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word.upper()}')
        assert out.strip() == template.format('una', word.upper())
