import os
import random
import re
import string
from subprocess import getstatusoutput, getoutput

prg = './finder.py'
empty = './inputs/empty.txt'
pablito_input = "./inputs/pablito.txt"
pablito_1_input = "./inputs/pablito_1.txt"
pablito_2_input = "./inputs/pablito_2.txt"
pablito_3_input = "./inputs/pablito_3.txt"
pablito_salida_test = "./test-outs/pablito_tornillo.txt"
pablito_1_out_test = "./test-outs/pablito_1.txt"
pablito_2_out_test = "./test-outs/pablito_2.txt"
pablito_3_out_test = "./test-outs/pablito_3.txt"
pablito_1_out_sub_test = "./test-outs/pablito_1_s.txt"
pablito_2_out_sub_test = "./test-outs/pablito_2_s.txt"
pablito_3_out_sub_test = "./test-outs/pablito_3_s.txt"


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


def out_flag():
    """Either -o or --outfile"""

    return '-o' if random.randint(0, 1) else '--outfile'


def word_flag():
    """Either -o or --outfile"""

    return '-w' if random.randint(0, 1) else '--word'


def replace_flag():
    """Either -o or --outfile"""

    return '-r' if random.randint(0, 1) else '--replace'


def substring_flag():
    """Either -o or --outfile"""

    return '-s' if random.randint(0, 1) else '--substring'


def test_replace_one_file_at_time():
    """Test file in/out"""

    out_test_files = [pablito_1_out_test, pablito_2_out_test, pablito_3_out_test]
    expected_results = ['Pablito     4 ./inputs/pablito_1.txt', 'Pablito     3 ./inputs/pablito_2.txt',
                        'Pablito     3 ./inputs/pablito_3.txt']

    for expected_file, expected_result in zip(out_test_files, expected_results):
        try:
            out_file = random_string()
            if os.path.isfile(out_file):
                os.remove(out_file)

            basename = os.path.basename(expected_file)
            in_file = os.path.join('./inputs', basename)
            rv, out = getstatusoutput(f'python {prg} {in_file} {word_flag()} Pablito {replace_flag()} Robertito '
                                      f'{out_flag()} {out_file}')
            assert rv == 0
            assert out.rstrip() == expected_result
            produced = open(out_file).read().rstrip()
            expected = open(expected_file).read().strip()
            assert expected == produced
        finally:
            if os.path.isfile(out_file):
                os.remove(out_file)


def test_replace_one_file_at_time_substring():
    """Test file in/out"""

    input_test_files = [pablito_1_input, pablito_2_input, pablito_3_input]
    out_test_files = [pablito_1_out_sub_test, pablito_2_out_sub_test, pablito_3_out_sub_test]
    expected_results = ['Pablito     4 ./inputs/pablito_1.txt', 'Pablito     3 ./inputs/pablito_2.txt',
                        'Pablito     4 ./inputs/pablito_3.txt']

    for input_test_file, expected_file, expected_result in zip(input_test_files, out_test_files, expected_results):
        try:
            out_file = random_string()
            if os.path.isfile(out_file):
                os.remove(out_file)

            in_file = input_test_file
            rv, out = getstatusoutput(
                f'python {prg} {in_file} {word_flag()} Pablito {substring_flag()} {replace_flag()} Robertito '
                f'{out_flag()} {out_file}')
            assert rv == 0
            assert out.rstrip() == expected_result
            produced = open(out_file).read().rstrip()
            expected = open(expected_file).read().strip()
            assert expected == produced
        finally:
            if os.path.isfile(out_file):
                os.remove(out_file)


def test_replace_multiple_files_at_time():
    out_test_files = [pablito_1_out_test, pablito_2_out_test, pablito_3_out_test]
    input_files = [os.path.join('./inputs', os.path.basename(out_test_files[0])),
                   os.path.join('./inputs', os.path.basename(out_test_files[1])),
                   os.path.join('./inputs', os.path.basename(out_test_files[2]))]
    out_files = [random_string(), random_string(), random_string()]
    try:
        rv, out = getstatusoutput(
            f'python {prg} {input_files[0]} {input_files[1]} {input_files[2]} {word_flag()} Pablito {replace_flag()} Robertito {out_flag()} {out_files[0]} {out_files[1]} {out_files[2]}')
        expected = ('Pablito     4 ./inputs/pablito_1.txt\n'
                    'Pablito     3 ./inputs/pablito_2.txt\n'
                    'Pablito     3 ./inputs/pablito_3.txt\n'
                    'Pablito    10 total')
        assert rv == 0
        assert out.rstrip() == expected
        for expected_file, out_file in zip(out_test_files, out_files):
            produced = open(out_file).read().rstrip()
            expected = open(expected_file).read().strip()
            assert expected == produced
    finally:
        for out_file in out_files:
            if os.path.isfile(out_file):
                os.remove(out_file)


def test_replace_multiple_files_at_time_substring():

    out_test_files = [pablito_1_out_sub_test, pablito_2_out_sub_test, pablito_3_out_sub_test]
    input_files = [pablito_1_input, pablito_2_input, pablito_3_input]
    out_files = [random_string(), random_string(), random_string()]
    try:
        rv, out = getstatusoutput(
            f'python {prg} {input_files[0]} {input_files[1]} {input_files[2]} {word_flag()} Pablito {substring_flag()} {replace_flag()} Robertito {out_flag()} {out_files[0]} {out_files[1]} {out_files[2]}')
        expected = ('Pablito     4 ./inputs/pablito_1.txt\n'
                    'Pablito     3 ./inputs/pablito_2.txt\n'
                    'Pablito     4 ./inputs/pablito_3.txt\n'
                    'Pablito    11 total')
        assert rv == 0
        assert out.rstrip() == expected
        for expected_file, out_file in zip(out_test_files, out_files):
            produced = open(out_file).read().rstrip()
            expected = open(expected_file).read().strip()
            assert expected == produced
    finally:
        for out_file in out_files:
            if os.path.isfile(out_file):
                os.remove(out_file)
