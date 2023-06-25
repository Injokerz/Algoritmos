'''Questao 1
num = int(input('Digite um numero: '))
if num >= 0 :
    print('O numero digitado é positivo')
else:
    print('O numero digitado é negativo')'''

'''Questao 2
num = int(input('Digite um numero: '))
if num%3 == 0:
    print('O número é multiplo de 3')
else :
    print('O número não é multiplo de 3')'''

'''Questao 3
num = int(input('Digite um numero: '))
if num%5 == 0:
    print('O número é multiplo de 5')
else :
    print('O número não é multiplo de 5')'''

'''Questao 4
num = int(input('Digite um número: '))
if num > 10:
    print('O número é maior que 10')
else :
    if num == 10:
      print('Número igual a 10')
    else:
      print('O número é menor que 10')'''

'''Questao 5
num = int(input('Digite um número: '))
if num > 100:
    print('O número é maior que 100')
else :
    if num == 100:
      print('Número igual a 100')
    else:
      print('O número é menor que 100')'''

'''Questao 6
frase = input('Digite uma palavra ou frase: ')
if len(frase) > 10: 
    print('Essa palavra/frase tem mais de 10 caracteres')
else:
    if len(frase) == 10:
        print('Essa palavra/frase tem 10 caracteres')
    else:
        print('Essa palavra/frase tem menos de 10 caracteres')'''

'''Questao 7
frase = input('Digite uma palavra ou frase: ')
if len(frase) > 20: 
    print('Essa palavra/frase tem mais de 20 caracteres')
else:
    if len(frase) == 20:
        print('Essa palavra/frase tem 20 caracteres')
    else:
        print('Essa palavra/frase tem menos de 20 caracteres')'''


'''Questao 8 e 9 
idade = int(input('Olá quantos anos tem ? '))
if idade>= 18:
    print('Muito bem, maiores de idade podem passar.')
else: 
    print('Lamento menores de idade nao sao permitidos')'''

'''Questao 10
genero = str(input('qual seu sexo? \n''[M]masculino [F]feminino : '))
if genero == 'M':
    print('Usuario do sexo masculino')
else:
    print('Usuario do sexo feminino')'''

'''Questao 11
EstadoCivil = str(input('Qual seu estado civil no momento ? \n [s]Solteiro(a) [c]Casado(a) [v]Viuvo(a) [d]Divorciado(a): '))
if EstadoCivil == 's':
    print('Solteiro(a)')
elif EstadoCivil == 'c':
    print('Casado(a)')
elif EstadoCivil == 'v':
    print('Viuvo(a)')
elif EstadoCivil == 'd':
    print('Divorciado(a)')'''

'''Questao 12
num = int(input('Digite um numero: '))
c = num/2
if c%1 :
    print('Numero impar')
else:
    print('Numero par')'''
    
'''Questao 13
idade = int(input('Qual sua idade: '))
Ec = str(input('Solteiro(a) ? \n [s] [n]: '))
if idade < 18 and Ec == 's':
    print('Isso ai foca nos estudos')
elif idade >= 18 and Ec == 's':
    print('Aceita sair para jantar ???')
else: 
    print('A que pena :c')'''

'''Questao 14
idade = int(input('Qual sua idade: '))
Ec = str(input('Casado(a) ? \n [s] [n]: '))
if idade < 18 and Ec == 's':
    print('Quer que eu chame a policia ?')
elif idade >= 18 and Ec == 's':
    print('Aceita sair para jantar ???')'''

'''Questao 15
num = int(input('Digite um numero: '))
if num > 0 :
    print('O numero digitado é positivo')
elif num == 0:
    print('numero igual a 0')
else:
    print('O numero digitado é negativo')'''

'''Questao 16
num = int(input('Digite um numero: '))
if  num%2 == 0 and num != 2:
     print('numero nao primo')
elif num%3 == 0 and num != 3:
     print('numero nao primo')
elif num%5 == 0 and num != 5:
     print('numero nao primo')
else:
     print('numero primo')'''

'''Questao 17
Ano = int(input('Digite o ano: '))
if Ano%100 != 0 and Ano%4 == 0 or Ano%400 == 0:
  print('É um ano bissexto')
else:
  print('Não é bissexto')'''

'''Questao 18
idade = int(input('Qual sua idade ? '))
if idade>=18 :
    print('Vote conciente... por favor')
else:
    print('Volte daqui alguns anos.')'''

'''Questao 19
print('Parado isso é uma blitz 👮')
idade = int(input('Diga sua idade jovem: '))
if idade>= 18:
    print('Ta liberado, dirija com cuidado ;)')
else:
    print('ORA ORA ORA, ligue para os teus pais vai')'''

'''Questao 20
num = int(input('Digite um numero: '))
if num%3 == 0 and num%5 == 0:
    print('Numero divisivel por 3 e 5')
else:
    print('Numero nao divisivel por 3 e 5')'''