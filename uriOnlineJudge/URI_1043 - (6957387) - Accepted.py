# -*- coding: utf-8 -*-
entradas = input()
a = entradas.split()
x = float(a[0])
y = float(a[1])
z = float(a[-1])
perimetro = x+y+z
area = ((x+y)*z)/2

if (x<y+z) and (y<x+z) and (z<x+y):
    print("Perimetro = %.1f" %perimetro)
else:
    print("Area = %.1f" %area)
