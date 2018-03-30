#https://ucoder.com.br/problems/1231/

a = input().split()
numeros = []
for k in a:
    numeros.append(int(k))
numeros = sorted(numeros, reverse=True)
for k in numeros:
    print(k)