'''Questao 1
lista = ["Limao", "Caju", "Acerola", "Laranja", "Goiaba", "Banana", "Pitaya", "Uva", "Pera", "Maça", "Tamarindo", "Açai"]
print(lista)
lista[10] = 'Joao'
print(lista)'''

'''Questao 2
soma = 0
val = [1, 6, 8, 9, 3, 5, 6, 2, 3, 4, 1, 90, 3, 88, 54, 2, 34, 78, 23, 98, 34, 23, 7, 8, 6, 1, 9, 2, 3, 4, 5, 2, 66, 7, 4, 85, 36, 2, 3, 9, 52, 13, 16, 21, 8, 9, 3, 5, 6, 2, 3, 4, 1, 90, 3, 88, 54, 2, 34, 78, 23, 98, 34, 23, 7, 8, 6, 1, 9, 2, 3, 4, 5, 2, 66, 7, 4, 85, 36, 2, 3, 9, 52, 13, 16, 25, 8, 9, 8, 5, 6, 2, 3, 4, 1, 90, 3, 88, 54, 2, 34, 78, 230, 98, 34, 23, 7, 8, 6, 1, 9, 2, 3, 4, 5, 2, 66, 7, 4, 85, 36, 2, 3, 9, 52, 13, 16, 26, 8, 9, 5, 5, 6, 2, 3, 4, 1, 90, 3, 88, 54, 2, 34, 78, 23, 98, 34, 23, 7, 8, 6, 109, 9, 2, 3, 4, 5, 2, 66, 7, 4, 85, 36, 2, 3, 9, 52, 13, 16, 23, 8, 9, 3, 5, 6, 2, 3, 4, 1, 90, 3, 88, 54, 2, 34, 78, 23, 98, 34, 231, 7, 8, 6, 1, 9, 2, 3, 4, 5, 2, 66, 7, 4, 85, 36, 2, 3, 9, 52, 13, 16, 28, 8, 9, 1, 5, 6, 2, 3, 4, 1, 90, 3, 88, 54, 2, 34, 78, 23, 98, 34, 23, 7, 8, 6, 1, 9, 2, 3, 4, 5, 2, 66, 7, 4, 85, 36, 2, 3, 9, 52, 13, 16, 29]
for v in val:
    soma += v
print(soma)'''

'''Questao 3
num = [1, 6, 8, 9, 3, 5, 6, 2, 3, 4, 1, 90, 3, 88, 54, 2, 34, 78, 23, 98, 34, 23, 7, 8, 6, 1, 9, 2, 3, 4, 5, 2, 66, 7, 4, 85, 36, 2, 3, 9, 52, 13, 16, 21, 8, 9, 3, 5, 6, 2, 3, 4, 1, 90, 3, 88, 54, 2, 34, 78, 23, 98, 34, 23, 7, 8, 6, 1, 9, 2, 3, 4, 5, 2, 66, 7, 4, 85, 36, 2, 3, 9, 52, 13, 16, 25, 8, 9, 8, 5, 6, 2, 3, 4, 1, 90, 3, 88, 54, 2, 34, 78, 230, 98, 34, 23, 7, 8, 6, 1, 9, 2, 3, 4, 5, 2, 66, 7, 4, 85, 36, 2, 3, 9, 52, 13, 16, 26, 8, 9, 5, 5, 6, 2, 3, 4, 1, 90, 3, 88, 54, 2, 34, 78, 23, 98, 34, 23, 7, 8, 6, 109, 9, 2, 3, 4, 5, 2, 66, 7, 4, 85, 36, 2, 3, 9, 52, 13, 16, 23, 8, 9, 3, 5, 6, 2, 3, 4, 1, 90, 3, 88, 54, 2, 34, 78, 23, 98, 34, 231, 7, 8, 6, 1, 9, 2, 3, 4, 5, 2, 66, 7, 4, 85, 36, 2, 3, 9, 52, 13, 16, 28, 8, 9, 1, 5, 6, 2, 3, 4, 1, 90, 3, 88, 54, 2, 34, 78, 23, 98, 34, 23, 7, 8, 6, 1, 9, 2, 3, 4, 5, 2, 66, 7, 4, 85, 36, 2, 3, 9, 52, 13, 16, 29]
maior = 0
for v in num:
    if v > maior:
        maior = v
print(f'O maior numero da lista é {maior}')'''

'''Questao 4
text = ["O", "seu", "Tatá", "tá?", "Não", "o", "seu", "Tatá", "não", "tá", "mas", "a", "mulher", "do", "seu", "Tatá", "tá", ".", "E", "quando", "a", "mulher", "do", "seu", "Tatá", "tá", "é", "a", "mesma", "coisa", "que", "o", "seu", "Tatá", "tá", "tá?"]
soma = 0
for v in text:
    if v == 'Tatá':
        soma += 1
print(soma)'''

'''Questao 5
letras = ["a", "b", "c", "d", "e", "f", "g", "h"]
letras.sort(reverse = True)
print(letras)'''

'''Questao 6
lista = [1, 3, 5, 7, 9, 11, 13, 10, 14]
ordenada = True
for i in range(len(lista) - 1):
    if lista[i] > lista[i + 1]:
        ordenada = False
        break
if ordenada:
    print("A lista e crescente.")
else:
    print("A lista não e crescente.")'''

'''Questao 7
numeros = []
soma = 0
while True:
    numeros.append(int(input('Digite um numero: ')))
    res = input('Deseja continuar ? [s] [n]: ')
    if res == 'n':
        break
for v in numeros:
    soma += v
media = soma/len(numeros)
print(f'A media entre os numeros digitados é {media}')'''

'''Questao 8
mult = []
num = []
while True:
    num.append(int(input('Digite o numero que deseja adicionar a lista: ')))
    res = input('Deseja continuar ? [s] [n]: ')
    if res == 'n':
        break
n = int(input('Digite o numero que deseja multiplicar a lista: '))
for v in num:
    mult.append(v * n)
print(num)
print(mult)'''

'''Questao 9
lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,3]
if lista1 == lista2:
    print('Sao iguais.')
else:
    print('São diferentes')'''

'''Questao 10
impar = 0
par = 0
lista = [1,2,3,4,5,6,7,8,9,10]
for v in lista:
    if v % 2 == 0:
        par += 1
    else:
        impar += 1
if impar > 1:
    print('Nessa lista tambem contem elementos impares')
else:
    print('Nessa lista só existem pares.')
print(f'Existem {par} numeros pares, e {impar} numeros impares')'''

'''Questao 11
n = 0
num = [1, 6, 8, 9, 3, 5, 6, 2, 3, 4, 1, 90, 3, 88, 54, 2, 34, 78, 23, 98, 34, 23, 7, 8, 6, 1, 9, 2, 3, 4, 5, 2, 66, 7, 4, 85, 36, 2, 3, 9, 52, 13, 16, 21, 8, 9, 3, 5, 6, 2, 3, 4, 1, 90, 3, 88, 54, 2, 34, 78, 23, 98, 34, 23, 7, 8, 6, 1, 9, 2, 3, 4, 5, 2, 66, 7, 4, 85, 36, 2, 3, 9, 52, 13, 16, 25, 8, 9, 8, 5, 6, 2, 3, 4, 1, 90, 3, 88, 54, 2, 34, 78, 230, 98, 34, 23, 7, 8, 6, 1, 9, 2, 3, 4, 5, 2, 66, 7, 4, 85, 36, 2, 3, 9, 52, 13, 16, 26, 8, 9, 5, 5, 6, 2, 3, 4, 1, 90, 3, 88, 54, 2, 34, 78, 23, 98, 34, 23, 7, 8, 6, 109, 9, 2, 3, 4, 5, 2, 66, 7, 4, 85, 36, 2, 3, 9, 52, 13, 16, 23, 8, 9, 3, 5, 6, 2, 3, 4, 1, 90, 3, 88, 54, 2, 34, 78, 23, 98, 34, 231, 7, 8, 6, 1, 9, 2, 3, 4, 5, 2, 66, 7, 4, 85, 36, 2, 3, 9, 52, 13, 16, 28, 8, 9, 1, 5, 6, 2, 3, 4, 1, 90, 3, 88, 54, 2, 34, 78, 23, 98, 34, 23, 7, 8, 6, 1, 9, 2, 3, 4, 5, 2, 66, 7, 4, 85, 36, 2, 3, 9, 52, 13, 16, 29]
for v in num:
    if v < 100:
        n += 1
print(f'Nessa lista existem {n} numeros menores que 100.')'''

'''Questao 12'''
import random  
#Listas de letras certas
res = []

#Lista de letras erradas
erradas = []
chances = 6
#Lista de palavras
frutas = ["limao", "caju", "acerola", "laranja", "goiaba", "banana", "pitaya", "uva", "pera", "maça", "tamarindo", "açai"]

#Sorteia uma palavra
palavra = frutas[random.randint(0,11)]

#Separa as letras da palavra.
letras = list(palavra)

#Mostra a quatidade de letras da palavra sorteada.
for i in letras:
    res.append('_')

#Detalhes
print('-'*33)
print(' '*9,'F  O  R  C  A')
print('-'*33)
print(f'Voce tem {chances} chances.')
print(res)

while True:
    #Verifica se a letra ja foi digitada
    tentativas = str(input('Tente uma letra: '))
    if tentativas in res or tentativas in erradas:
        print('Letra ja digitada, tente outra!')
        continue

    #Verifica se a letra digitada esta certa ou errada.
    if tentativas in letras:
        #Mostra a posição da letra digitada
        quant = palavra.count(tentativas,0,len(palavra))
        if quant != 1:
            for i, valor in enumerate(letras):
                if valor == tentativas:
                    res[i] = tentativas
        else:
            pos = letras.index(tentativas)
            res[pos] = tentativas
        print(res)
        print(f'Letras erradas: {erradas}')
    elif tentativas not in letras:
        erradas.append(tentativas)
        print(res)
        print(f'Letras erradas: {erradas}')

    #Verifica o numero de chances.
    if tentativas in erradas:
        chances -= 1
        print(f'Voce tem {chances} chances.')

    #Condiçao de derrota    
    if len(erradas) == 6:
        print('Suas chances acabaram, tente novamente!')
        break

#Condiçao de vitoria
    if res == letras:
        print('Parabéns voce descobriu a palavra!!!')
        print(f"A palavra era '{palavra}'")
        break


    
    
        

        

