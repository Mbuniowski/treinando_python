'''Crie um programa que exiba a seguinte frase: 
Meu nome é <seu nome> tenho <cidade>anos e moro em <cidade>.
Obs:a palavra que esta dentro de<>deve ser usada como variavel.'''

nome= "Michelle"
idade= str(40)
cidade= "Jandira"

print("Meu nome é" , nome,"tenho" , idade,"anos e moro em " , cidade)

''' Crie um programa que imprima os operadores Aritméticos:+,-,*,/,%,**.//'''

print(2+2)#conta simples de adição
print(2-1)#conta de subtração simples
print(2*2)#conta de multiplicação simples
print(2/4)#conta de divisão simples
print(20%2)#para ver a sobra da divisão
print(2**2)#conta de numero elevado,potencia
print(2//2)#divisão de numero inteiro sobra de uma casa decimal

'''Crie um programa utilizando os Operadores de Comparação: ==,!=,>,>=,<='''

print(2==2)#para verificar se o número e igual
print(2!=2)#para verificar se o numero é diferente
print(2>3)#para verificar se o número e maior que 
print(2>=2)#para verificar se o número é maior ou igual
print(2<=3)#para verificar se o número é menor ou igual

'''Construa um programa que faça o seguinte calculo um aumento de 15% para um salário de R$1000,00.'''

salario = 1000
aumento = 15
# calculo
resultado = salario + (salario * aumento / 100)
# primeiro método
print ( "o aumento é","R$",resultado)
# segundo método
print("O aumento é","R$",salario + (salario* 0.15))
# terceiro metodo
print("O aumento é","R$",salario + (salario* aumento / 100))

''' Elabore um programa que exiba o lucro de uma empresa:
Sendo a formula lucro = faturamento - custo'''


faturamento = 1000
custo = 35
# calculo 
resultado = faturamento - custo
#resolução
print("o lucro é:",resultado)





