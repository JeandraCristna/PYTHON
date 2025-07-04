#01 - Usando a conficional If, faça um programa que peça dois números diferentes ao usuário e retorne qual deles é o maior número.
num1 = int(input('DIgite o 1° numero: '))
num2 = int(input('DIgite o 2° numero: '))

if num1 > num2:
    print(f'O numero {num1} é maior') 
else:
    print(f'O numero {num2} é maior')
print('--'*15)  

numero = float(input("Digite um número: "))

if numero >= 0:
    print(f'O numero {numero} é positivo')
else:
    print(f'O numero {numero} é negativo')    
    
#Usando a condicioal If, faça um programa que verifique a letra digita pelo usuário:

#Se a letra for igual a 'F' retorne 'Feminino'
#Se a letra for igual a 'M' retorne 'Masculino'
#Qualquer outra letra retorne 'Sexo inválido'
letra = input("Digite a letra correspondente ao sexo (F/M): ")
if letra == 'F' or letra == 'f':
    print("Feminino")
elif letra == 'M' or letra == 'm':
    print("Masculino")
else:
    print("Sexo inválido")
print('--'*15)

#Faça um Programa que peça um número inteiro e retorne se ele e par ou ímpar.
#Dicas: Todo número divisível por 2 é par!
#Formúla: % (Módulo ou resto de divisão)​
numero = int(input('Digite um número inteiro'))
if numero % 2 == 0: 
    print(f'{numero} é um numero par')
else:
    print(f'{numero} é um ímpar')
    
print('--'*15)    

#Faça um programa que pergunte a idade do usuário:
#Se a idade for maior ou igual a 18 anos retorne 'Você é maior de idade.'
#Senão retorne 'Você é menor de idade.'
idade = int(input('Digite sua idade'))
if idade > 18:
    print(f'Você é maior de idade') 
else:
    print(f'Você é menor de idade')

print('--'*15)

#Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é o número 1234. Devem ser impressas as seguintes mensagens:
#ACESSO PERMITIDO, caso a senha seja válida.
#ACESSO NEGADO, caso a senha seja inválida.
senha = input('Digite sua senha')
if senha == '1234':
    print(f'ACESSO PERMITIDO')
else:
    print(f'ACESSO NEGADO') 

print('--'*15) 

#Escreva um programa que peça para o usuário digitar um senha, em seguida peça para ele confirmar a senha digitada. Devem ser impressas as seguintes
#SENHA CORRETA, caso ele tenha digitado a mesma senha duas vezes.
#SENHA INCORRETA, caso ele tenha digitado senhas diferentes.
senha = input('Digite sua senha')
confirmação = input('Confirme sua senha: ')
if senha == confirmação:
    print(f'SENHA CORRETA')   
else:
    print(f'SENHA INCORRETA') 
    
print("-------------------------------------------------------------------------")

#Escreva um programa que pergunte a nota final do aluno, em seguida retorne:
#Caso a nota final for maior ou igual a 5 retorne 'Você está aprovado.'
#Caso a nota final for menor a 5 retorne 'Você está reprovado.
nota = int(input('digite sua nota final'))
if nota > 5:
    print('Você está aprovado')                                                 
else:
    print('Você está reprovado')

print('--------------------------------------------------------------------------')        