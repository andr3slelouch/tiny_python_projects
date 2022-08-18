#!/usr/bin/env python3
"""
Author : andr3slelouch <andr3slelouch@github.com>
Date   : 17/08/2022
Purpose: Generar tablas de multiplicación con sus resultados acumulados
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Generador de tablas de multiplicación',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('tabla',
                        metavar='int',
                        type=int,
                        default=1,
                        help='Hasta que tabla se generará')

    parser.add_argument('-m',
                        '--maximo',
                        metavar='int',
                        type=int,
                        default=10,
                        help='Hasta que número será la tabla')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    numero_tabla = args.tabla
    maxim_tabla = args.maximo
    acumulador_total = 0
    for numero in range(1, numero_tabla + 1):
        acumulador_tabla = 0
        for maxim in range(1, maxim_tabla + 1):
            acumulador_tabla += numero * maxim
            print(f'{numero * maxim:5}', end=' ')
        acumulador_total += acumulador_tabla
        print(f'{acumulador_tabla:5}')
    print(f'total {acumulador_total:5}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
