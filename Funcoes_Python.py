"""FUNÇÕES
Uma função em Python é uma estrutura que permite agrupar um
conjunto de instruções para que possam ser executadas várias vezes,
sem que seja necessário repetir todo o código. 
A sintaxe básica para criar uma função em Python é a seguinte:

def nome_da_funcao(argumentos):
    # corpo da função
    return resultado
    
A palavra-chave "def" indica o início da definição da função.
"nome_da_funcao" é o nome que você escolhe para identificar a função. 
É uma boa prática usar nomes descritivos que indiquem o que a função faz.
"argumentos" são valores que você pode passar para a função para que ela possa trabalhar com eles.
Os argumentos são opcionais e você pode ter quantos quiser (ou nenhum). 
Eles são separados por vírgulas.
O corpo da função é onde você coloca as instruções que serão executadas quando a função for chamada. 
O corpo é identado com quatro espaços (ou um tab).
"return" é uma palavra-chave que indica qual é o valor de retorno da função. 
Quando a função é chamada, ela executa o código no seu corpo e, em seguida, 
retorna o valor especificado pelo "return". Se a função não tiver um "return", ela retorna "None".
"""

#Criando a Função
def quadrado(numero):
    resultado = numero ** 2
    return resultado

#Chamando a Função
resultado = quadrado(5)
print(resultado)

#----------------------------------------------------------------------------------------------

#Criando uma função do programador sem passagem de parâmetro
#Início da função
#def linha():
#    print("#"*100)
#Fim da Função  

#-------------------------------------------------------------------------------------------------

#Início do programa
#print("Inicio do Programa")
#linha()
#print("Fim do programa")
#Fim de Programa 

#----------------------------------------------------------------------------------------------------

#Criando uma função do programador com passagem de parâmetro
#Início da função
#def soma(a, b):
#    c = a + b
#    return c
#Fim da Função

#--------------------------------------------------------------------------------------------------

#Início do programa
#resultado = soma(1, 2)
#print(resultado)
#Fim de Programa 

#=================================================================================================

"""
Argumentos opcionais: Forneça valores padrão para argumentos opcionais 
para permitir que a função seja chamada sem fornecer valores para eles.
"""

#----------------------------------------------------------------------------------------------

#Início da função
#def soma(a, b, c=0):
#    return a + b + c
#Fim da Função

#---------------------------------------------------------------------------------------------

#Início do programa
#resultado = soma(1, 2)
#print(resultado)

#------------------------------------------------------------------------------------------

#resultado = soma(1, 2, 3)
#print(resultado)
#Fim de Programa

#-----------------------------------------------------------------------------------------

"""Argumentos variáveis: Use a notação * para 
receber uma quantidade variável de argumentos."""

#-------------------------------------------------------------------------------------------

#Início da função
#def soma(*números):
#    total = 0
#    for n in números:
#        total += n
#    return total
#Fim da Função

#------------------------------------------------------------------------------------------

#Início do programa
#resultado = soma(1, 2, 3, 4, 5)
#print(resultado)
#Fim de Programa

#---------------------------------------------------------------------------------------------

#Início do programa
"""Funções anônimas ou LAMBDAS: Use a função lambda para criar 
funções anônimas, que são funções sem nome."""

#soma = lambda a, b: a + b
#resultado = soma(1, 2)
#print(resultado)
#Fim de Programa

#-------------------------------------------------------------------------------------------

"""
Funções externas ou MÓDULOS do Programador, são arquivos que contêm diversas funções
que podem ser invocadas no programa com o comando import, esses arquivos
devem ser salvos juntos na pasta do programa.
"""
#-------------------------------------------------------------------------------------------

#Programa da Calculadora
"""
import calculadora
c = "s"
while c == "s":
    a = float(input("Digite o Primeiro Numero: "))
    b = float(input("Digite o segundo Numero: "))
    print("Escolha uma função matemática")
    e = int(input("1 - Soma\n2 - subtração\n3 - Multiplicação\n4 - Divisão\n: "))
    if e == 1:
        calculadora.soma_n(a,b)
    elif e == 2:
        calculadora.subtracao_n(a,b)
    elif e == 3:
        calculadora.multiplicacao_n(a,b)
    elif e == 4:
        calculadora.divisao_n(a,b)
    else:
        print("Não escolheu nenhum numero")
    c = str(input("Deseja continuar? [S/N] "))
print("Programa finalizado")
"""
 