#https://ucoder.com.br/problems/1060/

a = input().split()
dias = int(a[0])
saldo = int(a[1])

valores = []
cont = 0
while cont < dias:
    entrada = int(input())
    valores.append(entrada)
    cont+=1

balanco = []
for k in valores:
    saldo += k 
    balanco.append(saldo)

balanco = sorted(balanco)
print(balanco[0]) 