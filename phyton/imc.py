nome = input("Digite seu nome: ").title()
idade = input("Digite sua idade: ")
altura = input("Digite sua altura (em metros): ")
peso = input("Digite o seu peso (em kg): ")

# Convertendo os dados
int_idade = int(idade)
float_altura = float(altura)
float_peso = float(peso)

# Calculando o IMC
imc = float_peso / (float_altura ** 2)

# Montando a string com os dados
dados_pessoais = f'{nome} tem {int_idade} anos, com {float_altura:.2f}m de altura, pesa {float_peso}kg e seu IMC é:'

# Exibindo os dados
print(dados_pessoais)
print(f'{imc:.2f}')
