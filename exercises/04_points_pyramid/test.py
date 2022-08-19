import os
import random
import re
import string
from subprocess import getstatusoutput, getoutput

prg = './pyramid.py'


def test_exists():
    """exists"""

    assert os.path.isfile(prg)


def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'python {prg} {flag}')
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


def test_three():
    rv, out = getstatusoutput(f'python {prg} 3')
    expected = ('*\n'
                '**\n'
                '***\n'
                'total 6')
    assert rv == 0
    assert out.rstrip() == expected


def test_five():
    """Test with 1 argument"""
    rv, out = getstatusoutput(f'python {prg} 5')
    expected = ('*\n'
                '**\n'
                '***\n'
                '****\n'
                '*****\n'
                'total 15')
    assert rv == 0
    assert out.rstrip() == expected


def mode_flag():
    """Either -m or --modo"""

    return '-m' if random.randint(0, 1) else '--modo'


def test_three_with_m_right():
    """Test with 1 argument"""
    rv, out = getstatusoutput(f'python {prg} 3 {mode_flag()} Derecha')
    expected = ('  *\n'
                ' **\n'
                '***\n'
                'total 6')
    assert rv == 0
    assert out.rstrip() == expected


def test_three_with_m_center():
    """Test with 1 argument"""
    rv, out = getstatusoutput(f'python {prg} 3 {mode_flag()} Centro')
    expected = ('   *\n'
                '  ***\n'
                ' *****\n'
                '*******\n'
                'total 16')
    assert rv == 0
    assert out.rstrip() == expected


def test_three_with_m_right_left():
    """Test with 1 argument"""
    rv, out = getstatusoutput(f'python {prg} 3 {mode_flag()} Derecha Izquierda')
    expected = ('  *\n'
                ' **\n'
                '***\n'
                '*\n'
                '**\n'
                '***\n'
                'total 12')
    assert rv == 0
    assert out.rstrip() == expected


def test_three_with_m_left_right():
    """Test with 1 argument"""
    rv, out = getstatusoutput(f'python {prg} 3 {mode_flag()} Izquierda Derecha')
    expected = ('*\n'
                '**\n'
                '***\n'
                '  *\n'
                ' **\n'
                '***\n'
                'total 12')
    assert rv == 0
    assert out.rstrip() == expected


def test_three_with_m_left_center_right():
    """Test with 1 argument"""
    rv, out = getstatusoutput(f'python {prg} 3 {mode_flag()} Izquierda Centro Derecha')
    expected = ('*\n'
                '**\n'
                '***\n'
                '   *\n'
                '  ***\n'
                ' *****\n'
                '*******\n'
                '  *\n'
                ' **\n'
                '***\n'
                'total 28')
    assert rv == 0
    assert out.rstrip() == expected


def reverse_flag():
    """Either -r or --reverse"""

    return '-r' if random.randint(0, 1) else '--reverse'


def test_reverse():
    """Test with 1 argument"""
    rv, out = getstatusoutput(f'python {prg} 3 {mode_flag()} Derecha {reverse_flag()}')
    expected = ('***\n'
                ' **\n'
                '  *\n'
                'total 6')
    assert rv == 0
    assert out.rstrip() == expected


def test_left_right_reverse():
    """Test with 1 argument"""
    rv, out = getstatusoutput(f'python {prg} 3 {mode_flag()} Izquierda Derecha {reverse_flag()}')
    expected = ('***\n'
                '**\n'
                '*\n'
                '***\n'
                ' **\n'
                '  *\n'
                'total 12')
    assert rv == 0
    assert out.rstrip() == expected


def test_left_center_right_reverse():
    """Test with 1 argument"""
    rv, out = getstatusoutput(f'python {prg} 3 {mode_flag()} Izquierda Centro Derecha {reverse_flag()}')
    expected = ('***\n'
                '**\n'
                '*\n'
                '*******\n'
                ' *****\n'
                '  ***\n'
                '   *\n'
                '***\n'
                ' **\n'
                '  *\n'
                'total 28')
    assert rv == 0
    assert out.rstrip() == expected


def full_flag():
    """Either -f or --full"""

    return '-f' if random.randint(0, 1) else '--full'


def test_right_full():
    """Test with 1 argument"""
    rv, out = getstatusoutput(f'python {prg} 3 {mode_flag()} Derecha {full_flag()}')
    expected = ('  *\n'
                ' **\n'
                '***\n'
                '***\n'
                ' **\n'
                '  *\n'
                'total 12')
    assert rv == 0
    assert out.rstrip() == expected


def test_right_full_reverse():
    """Test with 1 argument"""
    rv, out = getstatusoutput(f'python {prg} 3 {mode_flag()} Derecha {full_flag()} {reverse_flag()}')
    expected = ('***\n'
                ' **\n'
                '  *\n'
                '  *\n'
                ' **\n'
                '***\n'
                'total 12')
    assert rv == 0
    assert out.rstrip() == expected


def test_left_right_full():
    """Test with 1 argument"""
    rv, out = getstatusoutput(f'python {prg} 3 {mode_flag()} Izquierda Derecha {full_flag()}')
    expected = ('*\n'
                '**\n'
                '***\n'
                '***\n'
                '**\n'
                '*\n'
                '  *\n'
                ' **\n'
                '***\n'
                '***\n'
                ' **\n'
                '  *\n'
                'total 24')
    assert rv == 0
    assert out.rstrip() == expected


def test_left_right_full_reverse():
    """Test with 1 argument"""
    rv, out = getstatusoutput(f'python {prg} 3 {mode_flag()} Izquierda Derecha {full_flag()} {reverse_flag()}')
    expected = ('***\n'
                '**\n'
                '*\n'
                '*\n'
                '**\n'
                '***\n'
                '***\n'
                ' **\n'
                '  *\n'
                '  *\n'
                ' **\n'
                '***\n'
                'total 24')
    assert rv == 0
    assert out.rstrip() == expected


def test_left_center_right_full():
    """Test with 1 argument"""
    rv, out = getstatusoutput(f'python {prg} 3 {mode_flag()} Izquierda Centro Derecha {full_flag()}')
    expected = ('*\n'
                '**\n'
                '***\n'
                '***\n'
                '**\n'
                '*\n'
                '   *\n'
                '  ***\n'
                ' *****\n'
                '*******\n'
                '*******\n'
                ' *****\n'
                '  ***\n'
                '   *\n'
                '  *\n'
                ' **\n'
                '***\n'
                '***\n'
                ' **\n'
                '  *\n'
                'total 56')
    assert rv == 0
    assert out.rstrip() == expected


def test_left_center_right_full_reverse():
    """Test with 1 argument"""
    rv, out = getstatusoutput(f'python {prg} 3 {mode_flag()} Izquierda Centro Derecha {full_flag()} {reverse_flag()}')
    expected = ('***\n'
                '**\n'
                '*\n'
                '*\n'
                '**\n'
                '***\n'
                '*******\n'
                ' *****\n'
                '  ***\n'
                '   *\n'
                '   *\n'
                '  ***\n'
                ' *****\n'
                '*******\n'
                '***\n'
                ' **\n'
                '  *\n'
                '  *\n'
                ' **\n'
                '***\n'
                'total 56')
    assert rv == 0
    assert out.rstrip() == expected
