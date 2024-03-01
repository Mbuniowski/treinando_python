'''
operadores logicos usando and(e) quaando for True (verdade)

vamos utilizar outro exemplo de expressões lógicas.
Vamos criar um programa simples para saber se uma pessoa pode fazer
um financiamento:
Requesitos necessários:
Uma renda acima de R$ 5.000,00
Seu nome deve está limpo
'''

renda_acima_5mil = False
nome_limpo = True

if renda_acima_5mil and nome_limpo:
    print('Financiamento aprovado')
else:
    print('Financiamento Negado')

