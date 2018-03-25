# -*- coding: utf-8 -*-

n = float(input())
lista1 = [100,50,20,10,5,2,1,0.50,0.25,0.10,0.05,0.01]
lista2 = [0,0,0,0,0,0,0,0,0,0,0,0]


for i in range(12):
    while (n - lista1[i]) >= 0:     
        n = n - lista1[i]
        lista2[i] = lista2[i]+1
        if (n > 0 and n < 0.01):
            n = 0.01
            break

print("NOTAS:\n%i nota(s) de R$ 100.00\n%i nota(s) de R$ 50.00\n%i nota(s) de R$ 20.00\n%i nota(s) de R$ 10.00\n%i nota(s) de R$ 5.00\n%i nota(s) de R$ 2.00\nMOEDAS:\n%i moeda(s) de R$ 1.00\n%i moeda(s) de R$ 0.50\n%i moeda(s) de R$ 0.25\n%i moeda(s) de R$ 0.10\n%i moeda(s) de R$ 0.05\n%i moeda(s) de R$ 0.01"%(lista2[0],lista2[1],lista2[2],lista2[3],lista2[4],lista2[5],lista2[6],lista2[7],lista2[8],lista2[9],lista2[10],lista2[11]))   

