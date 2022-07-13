#!/usr/bin/env python3
"""Crow's Nest"""

import argparse


# --------------------------------------------------
def get_args():
    """Permite obtener los argumentos de la línea de comandos"""

    parser = argparse.ArgumentParser(
        description="Nido del cuervo -- Elige le artículo correcto",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('palabra', metavar='palabra', help='Una palabra')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Función principal"""

    args = get_args()
    word = args.palabra
    article = 'una' if word[-1].lower() in 'a' else 'un'

    print(f'¡Capitán, {article} {word} por la amura de babor!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
