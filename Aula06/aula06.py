# Crie um programa em python que solicite ao usuário o peso e a altura, e calcule o seu IMC. IMC = peso/(altura²)

# peso = float(input('Digite o peso: '))
# altura = float(input('Digite a altura: '))

# imc = peso/(altura**2)
# print(f'Seu imc é {imc:.2f}')

# # operadores condicionais: ==,===, !=, >, <, >=, <=

# if imc < 18.5:
#     print('Abaixo do peso')
# elif imc < 25:
#     print('Peso normal')
# elif imc < 30:
#     print("sobrepeso")
# else:
#     print('obesidade')

# Listas

# listaFrutas = ['maçã','banana','laranja']

# print(listaFrutas[2])

# # append
# listaFrutas.append('goiaba')
# listaFrutas.insert(2,'morango')
# listaFrutas.pop()
# listaFrutas.pop(0)

# print(listaFrutas)

# Dicionários

# aluno = {
#     "nome":"Maria",
#     "idade":25,
#     "curso":'Python'
# }
# print(aluno)
# print(aluno["nome"])
# print(aluno.get('idade','idade não fornecida'))

# for

# for i in range(1,11):
#     print(i)

# listaFrutas = ['maçã','banana','laranja']

# for fruta in listaFrutas:
#     print(fruta)

# for key in aluno:
#     if key == 'idade':
#         if aluno[key]<18:
#             print('menor de idade')
#         else:
#             print('maior de idade')



# for key, value in aluno.items():
#     print(f'{key} : {value}')


# Crie um programa para receber do teclado o nome, idade, e curso de um aluno, salve esses valores em um dicionário chamado aluno, e depois inclua esse dicionário em uma lista de alunos, quando cadastrar 3 alunos printar a lista completa e encerrar o programa.

# alunos = []
# pessoa = {}

# pessoa['nome'] = 'Ana'
# print(pessoa)


# pip install requests
# pip freeze > requirements.txt

import requests

url = 'https://fakestoreapi.com/products/1'
resposta = requests.get(url)

# print(resposta.status_code)
# print(resposta.text)

opcao = input('temos 20 produtos, escolha um dos 20: ')
url = f'https://fakestoreapi.com/products/{opcao}'
resposta = requests.get(url)

print('O produto que você escolheu foi: ')


produto = resposta.json()
print(produto['image'])

# comando para criar ambiente virtual
# python -m venv venv

# comando para ativar ambiente virtual no windows
# .\venv\Scripts\activate

# Comando para o erro de política de excução de scripts no windows
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# pip install -r .\requirements.txt