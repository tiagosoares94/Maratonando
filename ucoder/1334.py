#https://ucoder.com.br/problems/1134/

a = input().split()
alt = float(a[0])
if a[1] == '2':
    print("%.2f" %((72.7*alt) - 58))
else:
    print("%.2f" %((62.1*alt) - 44.7))