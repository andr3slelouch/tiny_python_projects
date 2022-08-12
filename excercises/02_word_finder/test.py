import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './finder.py'
empty = './inputs/empty.txt'
pablito_input = "./inputs/pablito.txt"
pablito_1_input = "./inputs/pablito_1.txt"
pablito_2_input = "./inputs/pablito_2.txt"
pablito_3_input = "./inputs/pablito_3.txt"
pablito_salida = "./test-outs/pablito_tornillo.txt"
pablito_1_out = "./test-outs/pablito_1.txt"
pablito_2_out = "./test-outs/pablito_2.txt"


def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


def test_exists():
    """exists"""

    assert os.path.isfile(prg)


def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'python {prg} {flag}')
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


def test_bad_file():
    """bad_file"""

    bad = random_string()
    rv, out = getstatusoutput(f'python {prg} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


def test_empty():
    """Test on empty"""

    rv, out = getstatusoutput(f'python {prg} {empty} -w Pablito')
    assert rv == 0
    assert out.rstrip() == 'Pablito     0 ./inputs/empty.txt'


def test_one():
    """Test on one"""

    rv, out = getstatusoutput(f'python {prg} {pablito_1_input} -w Pablito')
    assert rv == 0
    assert out.rstrip() == 'Pablito     4 ./inputs/pablito_1.txt'


def test_more():
    """Test on more than one file"""

    rv, out = getstatusoutput(f'python {prg} {pablito_1_input} {pablito_2_input} -w Pablito')
    expected = ('Pablito     4 ./inputs/pablito_1.txt\n'
                'Pablito     3 ./inputs/pablito_2.txt\n'
                'Pablito     7 total')
    assert rv == 0
    assert out.rstrip() == expected


def test_sub_flag_one():
    """Test on one"""

    rv, out = getstatusoutput(f'python {prg} {pablito_3_input} -w la -s')
    assert rv == 0
    assert out.rstrip() == 'la       10 ./inputs/pablito_3.txt'


def test_sub_flag_more():
    """Test on one"""

    rv, out = getstatusoutput(f'python {prg} {pablito_1_input} {pablito_2_input} {pablito_3_input} -w la -s')
    expected = ('la        7 ./inputs/pablito_1.txt\n'
                'la        2 ./inputs/pablito_2.txt\n'
                'la       10 ./inputs/pablito_3.txt\n'
                'la       19 total')

    assert rv == 0
    assert out.rstrip() == expected


def test_replace_one():
    """Test on one"""

    rv, out = getstatusoutput(f'python {prg} {pablito_1_input} {pablito_2_input} {pablito_3_input} -w la -s')
    expected = ('la        7 ./inputs/pablito_1.txt\n'
                'la        2 ./inputs/pablito_2.txt\n'
                'la       10 ./inputs/pablito_3.txt\n'
                'la       19 total')

    assert rv == 0
    assert out.rstrip() == expected


