
'''
a= int(input("Primeiro valor:"))
b= int(input("Segundo valor:"))
if a> b:
    print("O primeiro número é o maior")
if b> a:
    print("O segundo número é o maior")'''

     
     
''' Atividade
    Criar um codigo que exiba a idade do carro 
se ele for menor ou igual a 3 a mensagem é seu carro e novo
ou se for maior que 3 seu a mensagem é carro e velho

idade= int(input("Digite a idade do carro: "))
if idade<= 3:
    print("Seu carro é novo")
if idade>3:
    print("Seu carro e velho")
    '''

salario= float(input("Digite o sálario para cálculo do imposto:"))
base= salario
imposto =0
if base >3000:
    imposto = imposto +((base - 3000)*0.35)
    base =3000
if base >=1000:
    imposto = imposto +((base - 1000)*0.20)
print("salário: R$%6.2f Imposto a pagar: R$%6.2f" % (salario, imposto))