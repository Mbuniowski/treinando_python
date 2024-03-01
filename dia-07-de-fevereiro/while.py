'''

resp = input('Deseja iniciar o programa? s/n ')
while resp != "s" and resp != "n":
    resp = input('resposta invalida!!!! continuar? s/n')
print('resposta ok. Vamos continuar o programa')
print("fim do programa")

______________________________________________________
'''
'''
n = int (input('digite um numero para ser somado: [999 - para parar]'))
soma = 0
while n!= 999:
    soma+= n
    n= int(input('digite outro numero para ser somado com os anteriores: 999 - para sair'))
print("soma = {}" .format(soma))
_____________________________________________________________________
'''
'''
senha = "54321"
leitura = " "
while (leitura != senha):
 leitura = input("Digite a senha: ")   
 if leitura == senha :
    print(' Acesso liberado ')
 else:
    print('Senha incorreta. Tente novamente')

________________________________________________________________________
'''
'''
#fibonacci
qtde = int(input("quantos termos do fibonacci você deseja?  "))
anterior = 0
atual = 1
contador = 1

while contador <= qtde:
    print('{} -'.format (atual),end = ' ')
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    contador += 1
print (contador)
print ( "FIM DO PROGRAMA DE FIBONACCI")

____________________________________________________________
'''
# o programa abaixo soma diversos números digitados pelo usuário.Este programa exibe a soma calculadora
# e também qual foi o menor e maior números digitados:

soma = 0
qtdenumeros = 1
resp = 's'
while resp == 's':
    n = int(input('digite um numero:  '))
    if qtdenumeros == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n <menor:
        menor = n
    soma+= n
    resp = input('deseja continuar digitando? s/n : ')
    while resp != 's' and resp != 'n':
        resp = input ('informe corretamente se deseja continuar digitando: s/n ')
    if resp == 's':
      qtdenumeros += 1
print("quantidade de números somados:{}".format(qtdenumeros))
print(f'soma = {soma}') 
print(f'menor número entre os digitados foi {menor}')  
print(f'maior número entre os digitados foi {maior}')      

















