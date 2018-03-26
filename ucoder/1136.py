#https://ucoder.com.br/problems/1136/

area = int(input())
if area % 54 == 0:
    latas = area/54
else:
    latas = int(area/54) + 1
print("%d %d" %(latas, latas*80))