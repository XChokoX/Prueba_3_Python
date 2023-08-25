# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 11:57:20 2023

@author: Lab-105_Pc10
"""

def palindromo(x):
    
    x = x.lower()
    print(f"{x}")
    auxiliar = x[::-1]
    print(f"{auxiliar}")
    
    if(auxiliar == x):
        
        return True
    
    else:
        return False
    
    
    return


while(True):
    
    palabra = input("Ingrese una palabra: ")

    largo = len(palabra)

    if(largo > 2):
        break
        
opcion = palindromo(palabra)

print(f"{opcion}")


if(opcion == True):
    print("Es Palindromo")

else:
    print("No es palindromo")