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
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='int',
                        type=int,
                        help='Tamaño')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    pos_arg = args.positional

    # ¿Qué pasa si varías la variable num?
    num = 1
    # Ejemplo primera fila de la pirámide a la derecha, es decir, num define el número de fila
    # Para que sea la piramide a la derecha se necesitan espacios
    print(" " * (pos_arg - num) + "*" * num)

    # ¿Qué pasa si varías la variable num?
    num = 0
    # Ejemplo primera fila de la pirámide al centro, es decir, num define el número de fila
    # Para que sea la pirámide al centro se necesita duplicar los puntos
    print(" " * (pos_arg - num) + "*" * (num * 2 + 1))


# --------------------------------------------------
if __name__ == '__main__':
    main()
