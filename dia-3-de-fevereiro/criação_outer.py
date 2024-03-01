#criação do Outer for loop

'''
for numero1 in range(5):
    print(numero1)

    # criação do Inner for loop
    for numero2 in range(5):
        print(numero1 , numero2)

        ____________________________________________________
'''
"""
#crição do Outer for loop
for numero1 in range(1,6):
    print('Produto', str(numero1))

    # criação do Inner for loop
    for numero2 in range(11):
        print(numero1 , numero2)
_____________________________________________________
"""
'''
# A resposta vai ficar na horizontal
palavra = 'FANTASTICO'
#DECLARAÇÃO FOR

for spaco in palavra:
    print(spaco)
_____________________________________________________
'''
'''
#A resposta vai ficar na vertical
#Forma feia
palavra = 'FANTASTICO'

#DECLARAÇÃO FOR

for spaco in palavra:
    print(spaco, end = '')
'''

'''
#A resposta vai ficar na vertical
#Forma bonita
palavra = 'FANTASTICO'

#DECLARAÇÃO FOR

for spaco in palavra:
    print( f' {spaco}', end = ' ')
_____________________________________________________________
'''

'''
#para digitar uma palavra

palavra = str(input('Digite uma palavra: '))
#declaração for
for spaco in palavra:
    print(f' {spaco}', end = ' ')

    ____________________________________________________________
    '''

#criação do retangulo
    # criar um retangulo de 6 x 6 

linhas = 6
colunas = 6 
simbolo = '#'
for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end = '  ')
    print()    