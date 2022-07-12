# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 22:43:04 2022

@author: Patricio Haro
"""
import random

print("\n\nGENERACION DE MATRICE NXM \n")

filas= int(input("Ingrese filas n:"))
while filas<4 or filas>30:
    print("Ingrese un numero del 4 al 30 porfavor, Repita la operacion")
    filas= int(input("Ingrese filas n:"))   
       
columnas= int(input("Ingrese columnas m:"))
while columnas<4 or columnas>30:
       print("Ingrese un numero del 4 al 30 porfavor, Repita la operacion")
       columnas = int(input("Ingrese columnas m:")) 



matriz=[[random.randint(1,100) for j in range(columnas)]for i in range(filas)]

mayor= None
fi=0
col=0

print("\nMATRIZ N X M\n")

for c in range (filas):
    for d in range (columnas):
        if mayor is None:
            mayor=matriz[c][d]-1 
        if matriz[c][d]> mayor:
            mayor= matriz[c][d]
            filmayor=c
            colmayor=d
        print(matriz[fi][col],end=" ")
        col=col+1
    fi=fi+1
    col=0
    print("")

fi=0
col=0
c=0
d=0

print("\nDIAGONAL PRINCIPAL")
for c in range (filas):
       print(matriz[c][c],end=" ")
       
print("\n")
       
   

print("DIAGONAL SECUNDARIA")
i=0
for i in range(filas):
    print((matriz[i][(columnas-1)-i]), end=" ")

print("\n")   


print("El numero mayor es",mayor )
print("La ubicacion del mayor es: FILA",filmayor, "COLUMNA", colmayor)
