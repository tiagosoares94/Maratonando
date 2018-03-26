#https://ucoder.com.br/problems/1141/

a = input().split()
n1 = int(a[0])
n2 = int(a[1])
if (n1+n2)/2 == 10:
    print("APROVADO COM DISTINCAO")
elif (n1+n2)/2 < 7:
    print("REPROVADO")
else:
    print("APROVADO")