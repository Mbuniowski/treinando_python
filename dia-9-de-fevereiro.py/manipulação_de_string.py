'''
palavra = "Apostila de Python"

# lower (troca as letras para minusculo)
print(palavra.lower())
# upper(troca as letras para maiusculo)
print(palavra.upper())
#swapcase(Inverte o conteudo da string(minusculo/maiusculo))
print(palavra.swapcase())
#title (converte para maiusculo todas as primeiras letras de cada palavra da string)
print(palavra.title())
#split () Transforma a string em uma lista, utilizando os espaços como referencia)
print(palavra.split())

________________________________________________________________________

'''
'''
#essa função serve para fatiar a palavra voce escolhe a posição de letras para imprimir
s = "Python"
print(s[1:4])
print(s[2:])
print(s[:5])
_____________________________________________________________________________________
'''
'''
# função imprime uma palavra e imprime as posiçoes da palavra
s = str(input("digite uma palavra  "))
print(s[1:4])
print(s[2:])
print(s[:5])

________________________________________________________________________
'''
'''
#Lista

# uma lista pode ter valores de qualquer tipo,incluindo outras listas.Exemplos:

L = [3 , 'abacate',9.7 , [5,6,3] , "Python" , (3 , 'j')]
print(L[2])
print(L[3])
print(L[3][1])
___________________________________________________________________________
'''
'''
#Para alterar um elemento da lista,basta fazer uma atribuição de valor atraves do indice.
#O valor existente sera subtituido pelo novo valor
#exemplo

L = [3 , 'abacate',9.7 , [5,6,3] , "Python" , (3 , 'j')]
L [3]= str(input('Digite uma palavra ou numero :  '))
print (L)

________________________________________________________________________
'''
'''
#funçoes para manipulação de listas

L = [1 ,2, 3, 4]
#len (retorna o tamanho da lista)
print(len(L))
# min( retorna o menor valor da lista)
print(min(L))
# max (retorna o maior valor da lista)
print(max(L))
#sum (retorna a soma dos elementos da lista)
print(sum(L))
#in (verifica se um valor pertence alista)
print(3 in L)

L = [5,7,2,9,4,1,3]
L.sort()
print("Lista em ordem crescente: " , L)
L.reverse()
print("inverte os elementos",L)

_____________________________________________________________________________________
'''
'''
#OPERAÇÕES COM LISTAS

#Concatenação (+)
a=[0,1,2]
b=[3,4,5]
c=a+b
print(c)
#[0,1,2,3,4,5]  (resposta)


#Repetição (*) 
L= [1,2]
R= L*4
print(R)
#[1,2,1,2,1,2,1,2] (resposta)

________________________________________________________________________
'''
'''
L1 = list(range (5))
print(L1)
#[0,1,2,3,4] (resposta)

L2 = list(range(3,8))
print(L2)
#[3,4,5,6,7]

L3 = list(range(2,11,3))
print(L3)
#[2, 5, 8]
________________________________________________________________________
'''
'''
#TUPLAS

#Exemplos

T = (1,2,3,4,5)
print(T)
#(1,2,3,4,5) (resposta)
#------------------------------
T = (1,2,3,4,5)
print(T[3])
#4 (resposta)


________________________________________________________________________

'''
'''
#desempacotamento de tuplas

T = (10,20,30,40,50)
a,b,c,d,e = T
print("a=" ,a,"b=",b)
#a= 10 b=20 (resposta)

________________________________________________________________________
'''
'''
#DICIONARIOS

#exemplos

D={"arroz":17.30, "feijão":12.50,"carne":23.90,"alface":3.40 }
print(D)
#{'arroz': 17.3, 'feijão': 12.5, 'carne': 23.9, 'alface': 3.4} (resposta)

D={"arroz":17.30,"feijão":12.50,"carne":23.90,"alface":3.40}
print(D["carne"])
#23.9 (resposta)

# e possivel acrescentar ou modificar

D={"arroz":17.30, "feijão":12.50,"carne":23.90,"alface":3.40 }
D["carne"]=25.0
D["tomate"]=8.80
print(D)
#{'arroz': 17.3, 'feijão': 12.5, 'carne': 25.0, 'alface': 3.4, 'tomate': 8.8} (resposta)

#os valores do dicionario não possuem ordem por isso a oredem de impressao dos valores nao 
#e a mesma
_____________________________________________________________________________________
'''
'''
#OPERAÇOES EM DICIONARIOS

#del exclui um item informando a chave
Dx ={2:"carro",3:[4,5,6],7:('a','b'),4: 173.8}
print(Dx[7])
print(Dx[3])
print(Dx[2])
#resposta
#('a', 'b')
#[4, 5, 6]
#carro
________________________________________________________________________
'''
'''
#BIBLIOTECAS
# chama a biblioteca inteira
import math
print(math.factorial(6))
#720 (resposta)
#pode-se importar uma função especifica da biblioteca

#chama uma função especifica da biblioteca 
from math import factorial
print(factorial(6))
#720 (resposta)
________________________________________________________________________
'''

#FUNÇÕES

#exemplo de função
'''
def hello():
    print("Olá Mundo!!!")
hello()        
#Olá Mundo!!! (resposta)
'''

'''
______________________________________________________________
#exemplo: Função para imprimir o maior entre 2 valores

def maior(x,y):
    if x>y:
        print(x)
    else:
        print(y)   
maior(4,7) 
# 7 (resposta)

____________________________________________________
'''
'''
#escopo das variáveis

def soma(x,y):
    total = x+y
    print("Total soma = ",total)
 #programa principal
total = 10
soma(3,5)
print("Total principal = ",total)
#resposta
#Total soma =  8
#Total principal =  10

________________________________________________
'''
'''
#retorno de valores
#exemplo
def soma (x,y):
    total = x+y
    return total
#programa principal
s=soma (3,5)
print("soma = " ,s)
#resposta 
#soma = 8
________________________________________________
'''
#INTERFACES GRAFICAS COM TK

