#----------------------Ctrlplay CY4 -----------------------
# Definindo o valor como 16
valor = 16

# Verifica se o valor é maior que 15 e imprime uma mensagem correspondente
if valor > 15:
    print(f"O número {valor} é maior que 15")
else:
    # Se o valor não for maior que 15, imprime que é menor que 15
    print(f"O número {valor} é menor que 15")
#-----------------------Explicação------------------------
#Definindo o valor como 16:
#Neste exercício, você atribuiu o valor 16 à variável chamada “valor”.
#Em seguida, você verifica se esse valor é maior que 15.
#Se for maior, imprime a mensagem “O número 16 é maior que 15”.
#Caso contrário, imprime a mensagem “O número 16 é menor que 15”.
# Verificação direta de igualdade entre strings

#----------------------Ctrlplay CY4 -----------------------
if "Ctrlplay" == "Ctrlplay":
    print("Os valores são iguais")
#Verificação direta de igualdade entre strings:
#Aqui, você compara duas strings: “Ctrlplay” e “Ctrlplay”.
#Como elas são idênticas, imprime a mensagem “Os valores são iguais”.

#----------------------Ctrlplay CY4 -----------------------
# Solicita a idade do usuário e verifica se é maior ou menor que 18
idade = int(input("Digite sua idade: "))
if idade < 12:
    print("Você é uma crinaça")
elif idade < 18:
    print("Voce é adolecente")
else:
    print("Você é adulto")
#Verificando a idade do usuário:
#Você solicita a idade do usuário.
#Se a idade for menor que 12, imprime “Você é uma criança”.
#Se for menor que 18 (mas maior ou igual a 12), imprime “Você é adolescente”.
#Caso contrário, imprime “Você é adulto”.


#----------------------Ctrlplay CY4 -----------------------
# Solicita uma cor ao usuário e verifica se é "amarelo" ou "azul"
cor = input("Digite uma cor: ").lower()
if cor == "amarelo" or cor == "azul":
    print("Você acertou a cor!")
else:
    print("Desculpe, você não acertou a cor!")

#Verificando a cor escolhida pelo usuário:
#Pede ao usuário que digite uma cor (em minúsculas).
#Se a cor for “amarelo” ou “azul”, imprime “Você acertou a cor!”.
#Caso contrário, imprime “Desculpe, você não acertou a cor!”.

#----------------------Ctrplay CY4 -----------------------
# Lista de frutas
frutas = ["maçã", "pera", "goiaba"]
# Solicita ao usuário que escolha uma fruta e verifica se está na lista
escolha = input("Escolha uma fruta: ").lower()
if escolha in frutas:
    print(f"A fruta {escolha} está na lista!")
else:
    print(f"A fruta {escolha} não está na lista")

#Verificando se uma fruta está na lista:
#Você tem uma lista de frutas: [“maçã”, “pera”, “goiaba”].
#Solicita ao usuário que escolha uma fruta (em minúsculas).
#Verifica se a fruta escolhida está na lista.
#Se estiver, imprime “A fruta escolhida está na lista!”.
#Caso contrário, imprime “A fruta escolhida não está na lista”