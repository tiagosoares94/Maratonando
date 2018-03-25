# -*- coding: utf-8 -*-

ordem = []
entradas = input()
a = entradas.split()
x = int(a[0])
y = int(a[1])
z = int(a[-1])

ordem.append(x)
ordem.append(y)
ordem.append(z)
ordem = sorted(ordem)
print("%i\n%i\n%i\n\n%i\n%i\n%i" %(ordem[0],ordem[1],ordem[-1],x,y,z))
