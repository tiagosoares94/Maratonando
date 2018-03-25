# -*- coding: utf-8 -*-

inputs = input()
a = inputs.split()
cod = int(a[0])
qnt = int(a[-1])

p = [4.00, 4.50, 5.00, 2.00, 1.50]

print("Total: R$ %.2f" %(qnt*p[cod-1]))