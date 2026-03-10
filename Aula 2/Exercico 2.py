#--------------------------Input Desafio----------------------------

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Calcula a soma
soma = num1 + num2

# Imprime o resultado
print("A soma de", num1, "e", num2, "é:", soma)


#Neste exercício, você pede ao usuário para inserir dois números (num1 e num2).
#Em seguida, você calcula a soma desses números e armazena o resultado na variável “soma”.
#Por fim, imprime a mensagem “A soma de {num1} e {num2} é: {soma}”.


#------------------------Condições Desafio-------------------------
#Verificação de número par ou ímpar:
#Peça ao usuário para inserir um número e, em seguida, 
#determine se o número é par ou ímpar.

numero = int(input("Digite um número: "))

if numero % 2 == 0:             #Função de resto    
    print("O número é par.")
else:
    print("O número é ímpar.")

#Função de resto supondo que o usuario escolha o numero 5
#Dentro do numero 5 cabem quantos numeros dois

#             Ou          

numero = int(input("Digite um número: "))

if numero & 1 == 0:       #Função de busca binaria 
    print("O número é par.")
else:
    print("O número é ímpar.")
#Verificação de Número Par ou Ímpar:
#Aqui, você solicita ao usuário que digite um número.
#Usando a operação de módulo (%), verifica se o número é divisível por 2.
#Se o resto da divisão for zero, imprime “O número é par”.
#Caso contrário, imprime “O número é ímpar”.


#------------------------Condições Desafio-------------------------
#Verificação de elegibilidade para votar:
#Solicite a idade do usuário e informe se ele é elegível para votar ou não.

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é elegível para votar.")
else:
    print("Você não é elegível para votar ainda.")

#Verificação de Elegibilidade para Votar:
#Você pede a idade do usuário.
#Se a idade for maior ou igual a 18, imprime “Você é elegível para votar”.
#Caso contrário, imprime “Você não é elegível para votar ainda”.

#------------------------Condições Desafio-------------------------
#Determinação do maior de três números:
#Peça ao usuário para inserir três números e informe qual é o maior deles.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 >= num2 and num1 >= num3:
    print("O primeiro número é o maior.")
elif num2 >= num1 and num2 >= num3:
    print("O segundo número é o maior.")
else:
    print("O terceiro número é o maior.")

#Determinação do Maior de Três Números:
#Solicita ao usuário que insira três números (num1, num2 e num3).
#Compara os números para determinar qual é o maior.
#Imprime a mensagem correspondente (“O primeiro número é o maior”,
#“O segundo número é o maior” ou “O terceiro número é o maior”).


#------------------------Condições Desafio-------------------------
#Calculadora de IMC (Índice de Massa Corporal):
#Solicite o peso (em quilogramas) e a altura (em metros) do usuário e calcule o IMC. 
#Em seguida, forneça uma mensagem indicando a faixa de peso.

peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Peso normal.")
elif 25 <= imc < 30:
    print("Acima do peso.")
else:
    print("Obeso.")

#Calculadora de IMC (Índice de Massa Corporal):

#Pede ao usuário o peso (em quilogramas) e a altura (em metros).
#Calcula o IMC usando a fórmula: 
#IMC=     peso  / (altura²)
#Com base no IMC, fornece uma mensagem indicando a faixa de peso 
#(“Abaixo do peso”, “Peso normal”, “Acima do peso” ou “Obeso”).