#!/usr/bin/env python3
"""
Autor:  Ken Youens-Clark <kyclark@gmail.com>
Adaptado al español por: Luis Andrade <https://github.com/andr3slelouch>
Propósito: Decir hola
"""

import argparse


# --------------------------------------------------
def get_args():
    """Permite obtener los argumentos de la línea de comandos"""

    parser = argparse.ArgumentParser(description='Decir hola')
    parser.add_argument('-n', '--nombre', metavar='nombre',
                        default='Mundo', help='Nombre a saludar')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Función principal"""

    args = get_args()
    print('Hola, ' + args.nombre + '!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
