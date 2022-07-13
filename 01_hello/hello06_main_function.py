#!/usr/bin/env python3
# Propósito: Decir hola

import argparse

def main():
    parser = argparse.ArgumentParser(description='Decir hola')
    parser.add_argument('-n', '--nombre', metavar='nombre',
                        default='Mundo', help='Nombre a saludar')
    args = parser.parse_args()
    print('Hola, ' + args.nombre + '!')

if __name__ == '__main__':
    main()
