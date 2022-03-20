# Escreva um programa que leia três números e que imprima o maior e o menor

a = int(input('Entre com um número: '))
b = int(input('Entre com mais um número: '))
c = int(input('Mais um número por favor: '))


#if a == b == c:
    #print('Os números são iguais. ')

    
#else:

maior = a

if b > a and b > c:
    maior = b

if c > a and c > b:
    maior = c

menor = a

if b < a and b < c:
    menor = b

if c < b and c < a:
    menor = c

print('O maior número digitado foi {}'.format(maior))
print('O menor número digitado foi {}'.format(menor))

