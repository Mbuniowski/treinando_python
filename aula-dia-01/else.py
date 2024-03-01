''''
#else

a = int(input("Digite a idade do seu carro:"))
if a <=3:
    print("seu carro é novo")
else:
    print("Seu carro é velho")
'''
'''
Vejamos o exemplo de calcular a conta de um telefone celular da empresa Tchau.Os planos de empresa são 
bem interessantes e oferecem preços diferenciados de acordo com a quantidade de minutos usasdos por mês.
Abaixo de 200 minutos, a empresa cobra R$ 0,20 poe minuto.Entre 200 e 400 minutos,o preço é de R$0,18.
Acima de 400 minutos, o preço é de R$0.15.O programa resolve o problema.
'''
minutos = int(input("Digite os minutos utilizados: "))
if minutos < 200:
   preco = 0.20
if minutos < 400:
   preco = 0.40
else:
   preco = 0.15
print("Seu plano custara: R$%6.2F"% (minutos * preco))