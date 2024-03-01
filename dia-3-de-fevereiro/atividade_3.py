#Crie um programa que o usuário insira seu nome e imprima letra por letra.
'''
nome = str(input("Digite seu nome: "))
for letra in nome:
    print(f' {letra} esta dentro do nome ', nome)
    '''
'''
Utilizando o for junto com if e else
    
    Vamos utiliza agora o for junto com if e else para isso vamos cria um codigo 
de uma loja online,com a condição de o cliente receberá uma mensagem de 
"compra no valor de R$12,50 e entrega confirmada" e "Detalhes enviado para o seu email " ou 
"Falha na compra"
'''
compra_confirmada= True
dados_compra = 'compra no valor de R$12.50 e entrega confirmada'
for enviar in range(3):
    if compra_confirmada:
       print(dados_compra)
       print('Detalhes enviado para o seu email')
       break
else:
       print('falha no envio')


