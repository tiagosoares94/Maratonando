#https://ucoder.com.br/problems/1219/

a = int(input())
b = input()
pos = 0
for k in b:
    if k == "D":
        pos+=1
    elif k == "E":
        pos-=1
    if pos > 3 or pos < -3:
        pos = 0

if pos == -1:
    print("O")
elif pos == -3:
    print("L")
elif pos == -2:
    print("S")
elif pos == 0:
    print("N")
elif pos == 1:
    print('L')
elif pos == 2:
    print("S")
else:
    print("O")