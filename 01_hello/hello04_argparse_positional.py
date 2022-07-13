#!/usr/bin/env python3
# Propósito: Decir hola

import argparse

parser = argparse.ArgumentParser(description='Decir hola')
parser.add_argument('nombre', help='Nombre a saludar')
args = parser.parse_args()
print('Hola, ' + args.nombre + '!')
