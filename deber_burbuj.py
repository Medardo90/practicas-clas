# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 22:29:27 2022

@author: Patricio Haro
"""

def mburbuja(vec):
    long=len(vec)-1
    #print(long)
    for i in range(0, long):
        print(f"pasada #{i+1}")
        
        #print(i)
        for j in range(0, long):
            print(f"comparación: {vec[j]}>{vec[j+1]} ")
            if vec[j]> vec[j+1]:
                print(f"intercambiar: {vec[j]}x{vec[j+1]}")
                aux=vec[j]
                vec[j]=vec[j+1]
                vec[j+1]=aux
        print(f"lista: {vec}")
    return vec

lista=[50,90,100,78,95,68]
print("Antes de ordenar: ")
print(lista)
print("Despues de ordenar: ")
print(mburbuja(lista))

    
    
    