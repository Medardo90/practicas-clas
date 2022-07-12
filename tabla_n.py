# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 12:31:06 2022

@author: Patricio Haro
"""

def cmatriz(m, n):
    return[[i*j for j in range(n)] for i in range(m)]

filas=int(input("ingrese la cantidad de filas: "))

columnas=int(input("ingrese la cantidad de columnas: "))
ma=cmatriz(filas, columnas)
    

print(ma,)