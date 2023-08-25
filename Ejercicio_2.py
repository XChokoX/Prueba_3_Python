# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 11:33:48 2023

@author: Lab-105_Pc10
"""

while(True):
    
    print("\n1) kilo a millas: ")
    print("2) Millas a kilometros: ")
    print("3) Kilogramos a libras: ")
    print("4) Libras a Kilogramos: ")
    print("5) Celsius a Fahrenheit: ")
    print("6) Fahrenheit a Celsius: ")
    print("0) Salir: ")
    
    opcion = input("\nIngrese la opcion: ")
    opcion = int(opcion)
    
    if(opcion == 1):
        valor = input("\nIngrese las kilometros: ")
        valor = float(valor)
        print(f"\nMillas: {valor * 0.621371}") 
    
    if(opcion == 2):
        valor = input("\nIngrese los millas: ")
        valor = float(valor)
        print(f"\nKilometros: {valor * 1.60934}") 
    
    if(opcion == 3):
        valor = input("\nIngrese los Kilogramos: ")
        valor = float(valor)
        print(f"\nLibras: {valor * 2.20462}") 
    
    if(opcion == 4):
        valor = input("\nIngrese los libras: ")
        valor = float(valor)
        print(f"\nkilogramos: : {valor * 0.453592}") 
    
    if(opcion == 5):
        valor = input("Ingrese los celsius: ")
        valor = float(valor)
        print(f"\nfahrenheit: : {(valor * 9/5) + 32}") 
    
    if(opcion == 6):
        valor = input("Ingrese los fahrenheit: ")
        valor = float(valor)
        print(f"\ncelsius: : {((valor - 32) * 5/9)}")
    
    if(opcion == 0):
        break