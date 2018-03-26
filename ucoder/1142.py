#https://ucoder.com.br/problems/1142/

a = input().split()
numeros = []
for k in a:
    numeros.append(int(k))
numeros = sorted(numeros)
print(numeros[-1])