#https://ucoder.com.br/problems/1027/

a = input().split()
n1 = int(a[0])
n2 = int(a[1])

if ((n1%n2)>(n2%n1)):
    print(n1)
else:
    print(n2)