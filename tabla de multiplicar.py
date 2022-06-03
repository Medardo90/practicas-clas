# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 07:50:54 2022

@author: Alumno
"""
suma=0
promedio=0
for j in range (1,16):
    print("la tabla de n6:",j)
    print("\n")
    par=0
    impar=0
    for i in range (1,16):
        res=i*j
        suma+=res
        promedio=suma //15
        print(i,"x",j,"=",res)
        if res%2==0:
            par=par+1
        else:
            impar=impar+1
        
    print("la suma de los numeros es",suma)
    print("el promedio de los numeros es:",promedio)
    print("hay",par,"numeros pares")
    print("hay",impar,"numeros impares")
    print("\n"*2)
 