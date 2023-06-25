'''Exemplo
div = 0
num = int(input('Digite um numero: '))
print(f'Divisores de {num}')
for i in range(1,num+1):
    if num % i == 0:
        div += 1
        print(num/i)
if  div == 2:
    print('O numero é primo')
else:
    print('O numero não é primo')'''

'''Questão 1
i = 1
while i < 10:
  print(i)
  i += 1
else:
  print("i já não é menor que 10")'''

'''Questao 2
num = 0
while num < 10:
    num += 1
    if num % 2 == 1:
        print(num)'''

'''Questao 3
for i in range (9,-1,-1):
    print(i)'''

'''Questao 4
n = 1000
while n > -3000:
    print(n)
    n -= 1'''

'''Questao 5
div = 0
num = int(input('Digite um numero: '))
for i in range(1,num):
    if num % i == 0:
        div += i 
if div == num:
    print('Número Perfeito')
else:
    print('Numero não perfeito')'''

'''Questao 6
res = 1
num = int(input('Digite um numero: '))
for i in range(1,num):
    res = res * (i+1)
print(res)'''

'''Questao 7
palavra = ' '
maior = ' '
while palavra != 'pare':   
    palavra = str(input('Digite uma palavra ? '))
    print("Caso deseje parar digite pare")
    tamanho = int(len(palavra))
    if tamanho > len(maior):
        maior = palavra
print(maior)'''

'''Questao 8
res = 0
import random
num = random.randint(0,100)
res = int(input('A sorte foi lançada, acerte o numero sorteado para ganhar 0.5 na nota ;): '))
while res != num:
    print(num)
    res = int(input('Tente de novo: '))
    if res != num:
        if res > num:
            print('DICA: Tente diminuir um pouco')
        elif res < num:
            print('DICA: Tente aumentar um pouco')
    if num % 2 == 0:
            print('DICA: O numero é par')
    elif num % 2 == 1:
            print('DICA: O numero é impar')

else:
    res == num
    print('Parabéns voce acertou!!!')'''

