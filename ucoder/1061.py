#https://ucoder.com.br/problems/1061/

a = input().split()
tomadas = []
soma = 0
for k in a:
    tomadas.append(int(k))
print(sum(tomadas)-len(tomadas)+1)