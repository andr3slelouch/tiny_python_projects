import os
import re
from subprocess import getstatusoutput

prg = "./names.py"


def test_exists():
    """exists"""

    assert os.path.isfile(prg)


def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'python {prg} {flag}')
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


def test_one_name():
    rv, out = getstatusoutput(f'python {prg} Renzo')
    expected = ('Hola soy el saludador me enviaste 1 nombre\n'
                'Hola Renzo, tu nombre inicia con la letra r y termina con la letra o.')
    assert rv == 0
    assert out.rstrip() == expected


def test_two_names():
    rv, out = getstatusoutput(f'python {prg} Renzo Alisson')
    expected = ('Hola soy el saludador me enviaste 2 nombres\n'
                'Hola Renzo, tu nombre inicia con la letra r y termina con la letra o.\n'
                'Hola Alisson, tu nombre inicia con la letra a y termina con la letra n.')
    assert rv == 0
    assert out.rstrip() == expected


def test_three_names():
    rv, out = getstatusoutput(f'python {prg} Renzo Alisson Carlos')
    expected = ('Hola soy el saludador me enviaste 3 nombres\n'
                'Hola Renzo, tu nombre inicia con la letra r y termina con la letra o.\n'
                'Hola Alisson, tu nombre inicia con la letra a y termina con la letra n.\n'
                'Hola Carlos, tu nombre inicia con la letra c y termina con la letra s.')
    assert rv == 0
    assert out.rstrip() == expected


def test_four_names():
    rv, out = getstatusoutput(f'python {prg} Renzo Alisson Carlos Santana')
    expected = ('Hola soy el saludador me enviaste 4 nombres\n'
                'Hola Renzo, tu nombre inicia con la letra r y termina con la letra o.\n'
                'Hola Alisson, tu nombre inicia con la letra a y termina con la letra n.\n'
                'Hola Carlos, tu nombre inicia con la letra c y termina con la letra s.\n'
                'Hola Santana, tu nombre inicia con la letra s y termina con la letra a.')
    assert rv == 0
    assert out.rstrip() == expected
