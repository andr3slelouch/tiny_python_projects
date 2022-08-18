"""
Una forma para imprimir elementos dinámicos como los de un for en una línea es el siguiente
"""

# Línea sin formato
for numero in range(1, 11):
    print(numero, end=' ')

# Para imprimir un salto de línea se puede utilizar solo el print
print()

# Ahora para que este formateado como en el deber se puede hacer así
for numero in range(1, 11):
    print(f'{numero:5}', end=' ')

#Imprimimos un salto de línea adicional para tener un comportamiento adecuado
print()
