# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 20:54:41 2022

@author: Patricio Haro
"""
import math
x=int(input("x: "))
n=int(input("n: "))
e=1
contador=0
suma=0
for i in range(n):    
    pa=pow(x, e)
    # print(pa)
    pb=math.factorial(e)
    # print(">",pb)
    e=e+2
    contador=contador+1
    if contador%2==0:
        r=-1*(pa/pb)
    else:
        r=pa/pb
    print(r)
    suma=suma+r
    r=suma
    rounD=round(r,2)
print("y =",rounD)
# print(r)
    
    
    

