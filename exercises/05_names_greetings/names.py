#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Programa que te dice con que letra empieza y con que letra termina tu nombre',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('names',
                        metavar='str',
                        nargs="*",
                        help='Nombre(s) a ser saludado(s)')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    if len(args.names) == 1:
        print(f"Hola soy el saludador me enviaste {len(args.names)} nombre")
    elif len(args.names) > 1:
        print(f"Hola soy el saludador me enviaste {len(args.names)} nombres")
    for name in args.names:
        print(f"Hola {name}, tu nombre inicia con la letra {str(name[0]).lower()} y termina con la letra {name[-1]}.")


# --------------------------------------------------
if __name__ == '__main__':
    main()
