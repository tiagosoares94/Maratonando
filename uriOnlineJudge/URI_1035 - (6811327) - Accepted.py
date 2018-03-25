# -*- coding: utf-8 -*-

lista = input()
oi = lista.split()
a = int(oi[0])
b = int(oi[1])
c = int(oi[2])
d = int(oi[-1])

if (c >= 0) and (d >= 0):
    if (b > c and d > a):
        if(c+d > a+b):
            print("Valores aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
        
else:
    print("Valores nao aceitos")
        
