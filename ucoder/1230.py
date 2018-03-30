#https://ucoder.com.br/problems/1230/

p1 = float(input())
p2 = float(input())
p3 = float(input())
if p2 > p1 < p3:
    print("1")
elif p1 > p2 < p3:
    print("2")
else:
    print("3")