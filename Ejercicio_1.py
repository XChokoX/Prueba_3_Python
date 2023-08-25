# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 11:20:21 2023

@author: Lab-105_Pc10
"""

def primo_o_no(x):
    
    
    contador = 0
    for i in range(2,x):
        
        if(x % i == 0):
            contador = contador + 1
    
    
    if(contador == 0):
      
        return True
    
    else:
        
        return False





numero = input("Ingrese su numero: ")
numero = int(numero)


print(f"{primo_o_no(numero)}")


