# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 12:24:27 2023

@author: Lab-105_Pc10
"""

palabra = input("Ingrese una palabra: ")
palabra = palabra.lower()

letra = input("Ingrese una letra: ")
contador = 0
letra = letra.lower()

for i in palabra:
    
    if(i == letra):
        contador = contador + 1

print(f"La letra {letra} aparece {contador} veces")