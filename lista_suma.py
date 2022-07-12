# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 07:15:34 2022

@author: Patricio Haro
"""
vector1=[1,2,3,4,5,6,7,8,9,10]
vector2=[1,2,3,4,5,6,7,8,9,10]
vector3=[0]*10
for item in range(10):
    vector3[item]=vector1[item]+vector2[item]
for item in range(10):
    print(vector3[item],end=" ")
print("\n")
print(vector3)
    



