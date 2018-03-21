#https://ucoder.com.br/problems/1073/

a = input().split()
r = []
for k in a:
    r.append(int(k))
r = sorted(r)
print(r[1])