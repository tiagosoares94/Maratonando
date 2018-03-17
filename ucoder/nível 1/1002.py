#https://ucoder.com.br/problems/1002/

n = int(input())
def fat(n):
     if n <= 1:
         return 1
     else:
         return n*fat(n-1)
print(fat(n))
