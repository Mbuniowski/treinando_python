'''
exemplo
Vamos imaginar que administramos um site e varias pessoas publicam produtos,só
que para publicar nesse site tem uma regra o valor deve ser entre 20 reais e 40 reais.
Se o produto custar 19 reais ele não pode ser cadastro no site se for maior de 41 reais também não 
será aceito.
vamos criar o programa.
'''

'''
valor = 40

if valor >= 20 and valor <= 40:
    print('Produto aceito')
else:
    print('Produto não aceito')

    ou

valor_produto =float(input("Digite o valor do produto "))
if valor_produto >= 20 and valor_produto <= 40:
    print('Produto aceito')
else:
    print('Produto não aceito')

    ou
    
    

valor = 25
    # melhorar sintaxe de forma matemética
if 20<= valor <40:
    # if valor >= 20 and valor< 40:
    print('produto foi aceito')
else:
    print('Produto não aceito')

    '''
'''
Atividade Pratica

O programa deverá solicitar a digitação de suas 4 notas bimestrais,
feito isso deverá clacular e exibir a sua média final(média aritmética entre as 4 notas).
Feito isso deverá tambem mostrar as mensagens:- Você está aprovado!,-Você está de exame!-
Voce esta reprovado!de acordo com o seguinte critério:Média final 
maior ou igual a seis o aluno esta aprovado,menor que três reprovado,
entre 3 e 6 de exame.
'''

nota 1=float(input('Digite a nota do 1º bimestre'))
nota 2=float(input('Digite a nota do 2º bimestre'))
nota 3=float(input('Digite a nota do 3º bimestre'))
nota 4=float(input('Digite a nota do 4º bimestre'))
media=((nota1 +nota2 +nota3 +nota4)/4)

if (media>= 6):
    print("Você está aprovado!")

if (media<= 3):
    print("Você está reprovado!")
else:
    print("Exame",media)






