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
                            