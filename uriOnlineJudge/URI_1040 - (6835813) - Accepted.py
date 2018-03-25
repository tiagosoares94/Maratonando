# -*- coding: utf-8 -*-

inputs = input()
a = inputs.split()
n1 = round(float(a[0]),1)
n2 = round(float(a[1]),1)
n3 = round(float(a[2]),1)
n4 = round(float(a[-1]),1)

media = (n1*2 + n2*3 + n3*4 + n4*1)/10

status = ''

if media >= 7:
    status = 'Aluno aprovado.'
elif media < 5:
    status = 'Aluno reprovado.'
else:
    status = 'Aluno em exame.'

print("Media: %.1f\n%s" %(media,status))

if status == 'Aluno em exame.':
    ne = round(float(input()),1)
    print("Nota do exame: %.1f" %ne)

    nm = (media+ne)/2

    if nm > 5:
        status = 'Aluno aprovado.'
    else:
        status = 'Aluno reprovado.'

    print('%s'%status)
    print('Media final: %.1f'%nm) 


