''' A partir da digitação da base e altura de um triângulo o programa deverá 
calcular sua área e exibi-la no monitor.
Formula: área (base x altura) /2'''

base= float(input("Digite o valor da base do triangulo: "))
altura= float(input("Digite a altura do triangulo: "))
resultado= float (base * altura) /2
print( 'O resultado é: ', resultado)
