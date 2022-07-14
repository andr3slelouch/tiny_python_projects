#!/usr/bin/env python3
"""Juego del Picnic"""

import argparse


# --------------------------------------------------
def get_args():
    """Obtener argumentos de línea de comandos"""

    parser = argparse.ArgumentParser(
        description='Juego del Picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Objeto(s) a llevar')

    parser.add_argument('-o',
                        '--ordenar',
                        action='store_true',
                        help='Ordenar los elementos')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.item
    num = len(items)

    if args.ordenar:
        items.sort()

    bringing = ''
    if num == 1:
        bringing = items[0]
    elif num == 2:
        bringing = ' y '.join(items)
    else:
        items[-1] = 'y ' + items[-1]
        bringing = ', '.join(items)

    print('Tú estas trayendo {}.'.format(bringing))


# --------------------------------------------------
if __name__ == '__main__':
    main()
