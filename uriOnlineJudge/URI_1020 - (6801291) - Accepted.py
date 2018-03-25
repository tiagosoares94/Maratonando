# -*- coding: utf-8 -*-

n = int(input())
a = int(n/365)
m = int((n - (a*365))/30)
d = n - (a*365) - (m*30)
print("%i ano(s)\n%i mes(es)\n%i dia(s)"%(a,m,d))
