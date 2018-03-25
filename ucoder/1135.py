#https://ucoder.com.br/problems/1135/

a = input().split()
peso = int(a[0])
reg = int(a[1])
if peso < reg:
    print("0")
else:
    print((peso-reg)*4)

