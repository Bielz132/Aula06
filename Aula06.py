# Indentação:
# É sobre a encapsular corretamente os blocos de códigos e a organização dos blocos
if 10 > 2:
    print('hello')
x = 0
if x == 0:
    print('ola')

#------------------------------------------------------------------------------------------#

# Concatenar:
# É juntar os códigos

# %
nome = 'carlos'
print('Olá %s'%(nome))

# f'
nome = 'Joao'
print(f'olá {nome}')

# .format
nome = 'paula'
print('Olá {}'.format(nome))

# ,
nome = 'jorge'
print('Olá',nome)


# formas de pular linha:

# \n
print('Ola\nmundo')

# '''
print('''
O rato
Roeu
A
Roupa
DO
Rei
De
Roma''')

# Dica: para deixar todos em '#' use Ctrl + :

#------------------------------------------------------------------------------------------#

# Aula 07:

# Lista (sim, dnv ;-;)

lista = [1,2,3,4,5,6]
n1 = lista[0]
n2 = lista[5]
soma = n1 + n2
print(soma)

# remover alguem da lista:

lista2 = [1,2,3,4,5,6]

del lista2[2]
lista2.remove(6)
lista2.pop(1)
print(lista2)

# adicionar alguem na lista:

lista3 = [1,2,3,4,5,666]
lista3[0] = 12          # isso apenas trocou o '1' pelo '123'.
lista3.append(23)
lista3 += (919, 50, 'teste')
lista3.insert(0,24)     # mesma coisa com o 'lista3[0] = 12'
print(lista3)

# Metodo Range | Inicio | Fim | Step by Step |

lista = list(range(2,122,2))
print(lista)

#---------------------------------------------------------------------------#

# ATIVIDADE 01

lista = list(range(0,22,2))
print(lista)

# ATIVIDADE 02

lista2 = list(range(0,55,5))
print(lista2)

# ATIVIDADE 03

pessoa1 = 1
pessoa2 = 2
pessoa3 = 3
pessoa4 = 4
pessoa5 = 5
pessoas = ['pessoa1','pessoa2','pessoa3','pessoa4','pessoa5']
print(pessoas)

# ATIVIDADE 04
carro = ['uno', 'jeep', 'ferrari']
print(carro + lista)

#---------------------------------------------------------------------------------#

print('mercado')

produtos = ['ARROZ','FEIJÃO','MACARRÃO','MOLHO']
valores = [10.00,15.00,8.00,3.50]
carrinho = []
meus_valores = []

produto1 = int(input('''
0 - ARROZ
1 - FEIJÃO
2 - MACARRÃO
3 - MOLHO
-> '''))

produto2 = int(input('''
0 - ARROZ
1 - FEIJÃO
2 - MACARRÃO
3 - MOLHO
-> '''))

carrinho = [produtos[produto1], produtos[produto2]]
meus_valores = [valores[produto1], valores[produto2]]
SOMA = sum(meus_valores)

print(f'''
.............................................
CUPOM

1 - {produtos[produto1]} R$ {valores[produto1]:.2f}
2 - {produtos[produto2]} R$ {valores[produto2]:.2f}

.............................................

R$ {SOMA:.2f}

VOLTE SEMPRE

''')

#---------------------------------------------------------------------------#

# Dicionário

pessoa = {
    'nome':'Paulo',
    'idade':25,
    'endereco': 'rua 10',
    'email' : 'paulo@gmail.com',
    'curso' : 'Python 60',
}

pessoa['idade'] = 30
pessoa['novo'] = 25
pessoa['CPF'] = 123232131312

print(pessoa)

# Condicionais em Python
# se condicao == True
#    faça isso

numero = int(input('->'))

if 35 > numero:
    print('é maior')
elif 35 == numero:
    print('é igual')    
else:
    print('é menor')

import random

numero_aleatorio = random.randint(1,2)
chute = int(input('Escolha um numero: '))

if numero_aleatorio == chute:
    print('Parabéns, vc acertou')
    print('o numero é',numero_aleatorio)
else:
    print('errou feio, o numero é',numero_aleatorio)    

