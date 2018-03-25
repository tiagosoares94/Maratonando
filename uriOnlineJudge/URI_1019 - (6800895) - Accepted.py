# -*- coding: utf-8 -*-

n = int(input(""))
h = int(n/3600)
m = int((n - (h*3600))/60)
s = n - (h*3600) - (m*60)

print("%i:%i:%i"%(h,m,s))