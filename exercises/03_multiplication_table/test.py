import os
import random
import re
import string
from subprocess import getstatusoutput, getoutput

prg = './multiplication_table.py'


def test_exists():
    """exists"""

    assert os.path.isfile(prg)


def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'python {prg} {flag}')
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


def test_one_table():
    """Test with 1 argument"""
    rv, out = getstatusoutput(f'python {prg} 1')
    expected = ('    1     2     3     4     5     6     7     8     9    10    55\n'
                'total    55')
    assert rv == 0
    assert out.rstrip() == expected


def test_three_table():
    rv, out = getstatusoutput(f'python {prg} 3')
    expected = ('    1     2     3     4     5     6     7     8     9    10    55\n'
                '    2     4     6     8    10    12    14    16    18    20   110\n'
                '    3     6     9    12    15    18    21    24    27    30   165\n'
                'total   330')
    assert rv == 0
    assert out.rstrip() == expected


def test_five_table():
    """Test with 1 argument"""
    rv, out = getstatusoutput(f'python {prg} 5')
    expected = ('    1     2     3     4     5     6     7     8     9    10    55\n'
                '    2     4     6     8    10    12    14    16    18    20   110\n'
                '    3     6     9    12    15    18    21    24    27    30   165\n'
                '    4     8    12    16    20    24    28    32    36    40   220\n'
                '    5    10    15    20    25    30    35    40    45    50   275\n'
                'total   825')
    assert rv == 0
    assert out.rstrip() == expected


def max_flag():
    """Either -m or --maximo"""

    return '-m' if random.randint(0, 1) else '--maximo'


def test_one_with_max_five():
    """Test with 1 argument"""
    rv, out = getstatusoutput(f'python {prg} 1 {max_flag()} 5')
    expected = ('    1     2     3     4     5    15\n'
                'total    15')
    assert rv == 0
    assert out.rstrip() == expected


def test_five_with_max_ten():
    """Test with 1 argument"""
    rv, out = getstatusoutput(f'python {prg} 5 {max_flag()} 10')
    expected = ('    1     2     3     4     5     6     7     8     9    10    55\n'
                '    2     4     6     8    10    12    14    16    18    20   110\n'
                '    3     6     9    12    15    18    21    24    27    30   165\n'
                '    4     8    12    16    20    24    28    32    36    40   220\n'
                '    5    10    15    20    25    30    35    40    45    50   275\n'
                'total   825')
    assert rv == 0
    assert out.rstrip() == expected


def test_three_with_max_twelve():
    """Test with 1 argument"""
    rv, out = getstatusoutput(f'python {prg} 3 {max_flag()} 12')
    expected = ('    1     2     3     4     5     6     7     8     9    10    11    12    78\n'
                '    2     4     6     8    10    12    14    16    18    20    22    24   156\n'
                '    3     6     9    12    15    18    21    24    27    30    33    36   234\n'
                'total   468')
    assert rv == 0
    assert out.rstrip() == expected
