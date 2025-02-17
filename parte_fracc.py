"""
Determinar si un número dado tiene parte fraccionaria (decimales)
Karen Durán, 757136 e Ingeniería Civil
Algoritmos y Programación 
ESI232B2
07/02/25
10 minutos 
"""

# Entradas
numero = float(input("Introduzca un número: "))
PARTE_FRACCIONARIA = numero % 1

# Proceso
if PARTE_FRACCIONARIA != 0:
    decimales = True 
else: 
    decimales = False 

# Salidas
if decimales: 
    print("Sí tiene decimales")
else: 
    print("No tiene decimales")