# -*- coding: utf-8 -*-

entradas = input()
a = entradas.split()
x = float(a[0])
y = float(a[-1])

if x == 0 and y == 0:
    print("Origem")

if x != 0 and y != 0:
    if x > 0 and y > 0:
        print("Q1")

    elif  x < 0 and y > 0:
        print("Q2")

    elif x < 0 and y < 0:
        print("Q3")

    else:
        print("Q4")

elif x == 0 and y != 0:
    print("Eixo Y")
elif y ==0 and x != 0:
    print("Eixo X")
