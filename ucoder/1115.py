#https://ucoder.com.br/problems/1115/

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a == d+b+c) and (d == b+c) and (b == c):
    print("S")
else:
    print("N")