# -*- coding: utf-8 -*-

inputs = input()
a = inputs.split()
n1 = float(a[0])
n2 = float(a[1])
n3 = float(a[-1])

b = n2*n2 - 4*n1*n3

if (n1 != 0 and n2!=0 and n3!=0):
    if b < 0:
         print("Impossivel calcular")
    
    else:   
        x1 = (-n2 + b**(1/2.0))/(2*n1)
        x2 = (-n2 - b**(1/2.0))/(2*n1)
        print("R1 = %.5f\nR2 = %.5f" %(x1,x2))    

else:
    print("Impossivel calcular")
