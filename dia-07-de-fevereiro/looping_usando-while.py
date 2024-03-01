'''
while True:
    n = int(input('digite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'você somou {cont} numeros')
print(f'a soma de todos foi {soma}')

__________________________________________
'''
# Jogando Par ou Impar com o computador.O programa deve terminar quando o computador
#vencer o usuario .quando terminar mostre quantas partidas o usuario venceu.

'''
import random
ptsusuario = ptscomputador = 0 
while True:
    n= int(input('qual numero entre 0 e 10? '))
    parouimpar = input('par ou impar? responda: p/i ')
    while parouimpar != 'p' and parouimpar != 'i' :
        parouimpar = input ('Resposta invalida? Responda: p/i')
    computador = random.randint(0,10)  
    soma = n + computador
    if soma %2 == 0 and parouimpar == 'p' :
        ptsusuario +=1
    elif soma %2 == 1 and parouimpar == 'i' :  
        ptsusuario +=1
    else:
        ptscomputador += ptscomputador
        break
print(f'você venceu {ptsusuario} partidas') 

_____________________________________________________________
'''
# Escreva um programa que leia um número de 1 a 10 
#e mostre a tabuada desse numero.
"""    
numero=int(input("Tabuada do numero: "))
for n in range(0,11):
    print (f'{numero} x {n} = {numero*n}')
"""
#tem outra forma de resolver 
'''
numero = int(input('Digite um numero '))
for sequencia in range(1,11):
    print("%2d x %2d = %3d" %(sequencia,numero,sequencia*numero))

'''


    