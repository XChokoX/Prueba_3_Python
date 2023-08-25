# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 12:14:23 2023

@author: Lab-105_Pc10
"""

diccionario = {}
total = 0

while(True):
    
    articulo = input("Ingrese un articulo: ")
    precio = input("Ingrese el precio del producto: ")
    precio = float(precio)
    
    diccionario[articulo] = precio

    total = precio + total
    

    opcion = input("¿Quiere agregar otro articulo? (si/no): ")
    
    if(opcion == "no"):
        break
    
    if(opcion == "si"):
        continue
    
for articulo,precio in diccionario.items():
    print(f"Articulo: {articulo} / Precio: {precio} ")

print(f"Total: {total}")

