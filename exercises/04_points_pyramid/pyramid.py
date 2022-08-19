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
        description='Pirámides de puntos',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('tamano',
                        metavar='int',
                        type=int,
                        help='Tamaño de la o las pirámides')
    parser.add_argument('-m',
                        '--modo',
                        help='Modo de la o las pirámides',
                        nargs='*',
                        type=str,
                        metavar="Modo",
                        default=["Izquierda"])
    parser.add_argument('-f',
                        '--full',
                        help="Imprime las pirámides con sus reversos completo",
                        action="store_true")
    parser.add_argument('-r',
                        '--reverse',
                        help="Define la bandera para revertir la impresión de las banderas",
                        action="store_true")
    return parser.parse_args()


def left_pyramid(length: int, reverse=False):
    range_to_iterate = []
    range_to_iterate.extend(range(1, length + 1))
    counter = 0
    if reverse:
        reversed_list = []
        reversed_list.extend(reversed(range_to_iterate))
        range_to_iterate = reversed_list
    for num in range_to_iterate:
        print("*" * num)
        counter += num
    return counter


def right_pyramid(length: int, reverse=False):
    range_to_iterate = []
    range_to_iterate.extend(range(1, length + 1))
    counter = 0
    if reverse:
        reversed_list = []
        reversed_list.extend(reversed(range_to_iterate))
        range_to_iterate = reversed_list
    for num in range_to_iterate:
        print(" " * (length - num) + "*" * num)
        counter += num
    return counter


def center_pyramid(length: int, reverse=False):
    range_to_iterate = []
    range_to_iterate.extend(range(0, length + 1))
    counter = 0
    if reverse:
        reversed_list = []
        reversed_list.extend(reversed(range_to_iterate))
        range_to_iterate = reversed_list
    for num in range_to_iterate:
        print(" " * (length - num) + "*" * (num * 2 + 1))
        counter += num * 2 + 1
    return counter


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    pos_arg = args.tamano
    points = 0
    for modo in args.modo:
        if modo == "Izquierda":
            points += left_pyramid(pos_arg, args.reverse)
            if args.full:
                points += left_pyramid(pos_arg, not args.reverse)
        if modo == "Derecha":
            points += right_pyramid(pos_arg, args.reverse)
            if args.full:
                points += right_pyramid(pos_arg, not args.reverse)
        if modo == "Centro":
            points += center_pyramid(pos_arg, args.reverse)
            if args.full:
                points += center_pyramid(pos_arg, not args.reverse)
    print(f'total {points}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
