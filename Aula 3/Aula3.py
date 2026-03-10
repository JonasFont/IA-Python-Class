def soma(a, b):
    resultado = a + b
    return resultado

# Chamando a função e armazenando o resultado em uma variável
resultado_da_soma = soma(3, 5)
print(resultado_da_soma)

#Neste exemplo, a função soma aceita dois parâmetros a e b, os adiciona e retorna o resultado.
#As funções em Python são extremamente flexíveis e poderosas.
#Elas podem aceitar argumentos padrão, argumentos de palavra-chave,
#retornar múltiplos valores usando tuplas e até mesmo aceitar funções como argumentos.
#Elas são uma parte fundamental da programação em Python e são usadas extensivamente em qualquer projeto Python significativo.


def saudacao(nome):
    print("Olá, " + nome + "! Como você está?")

saudacao("Maria")  # Saída: Olá, Maria! Como você está?
#Neste caso, a função saudacao() aceita um argumento nome,
#que é usado para personalizar a saudação.

def soma(a, b):
    return a + b

print(soma(3, 5))  # Saída: 8

#Neste exemplo, a função soma() aceita dois argumentos a e b, e retorna a soma deles.


def desafio():
    print("-------------------------Desafio----------------------------")



def calculo(a, b):
    soma = a + b
    print(f"A soma entre os valores {a} + {b} = {soma}")


a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
calculo(a, b)

#def calculo(a, b): Esta linha define a função calculo,
#que aceita dois argumentos a e b.
#soma = a + b: Calcula a soma dos dois valores.
#ste programa pedirá ao usuário para inserir dois números inteiros e,
#em seguida, chamará a função calculo com esses números.
#Em seguida, ele imprimirá os resultados da soma, subtração,
#multiplicação e divisão desses dois números.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def faixa_de_peso(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"


#---------------------------------Desafio 2-------------------------------

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        print(f"Abaixo do peso {imc:.2f}")
    elif 18.5 <= imc < 25:
        print(f"Peso normal {imc:.2f}")
    elif 25 <= imc < 30:
        print(f"Sobrepeso {imc:.2f}")
    else:
        print("Obesidade")
    print(imc)

# Solicitar ao usuário o peso em quilogramas e a altura em metros
peso = float(input("Digite o seu peso em quilogramas: "))
altura = float(input("Digite a sua altura em metros: "))

# Calcular o IMC
imc = calcular_imc(peso, altura)


#-------------------------------Desafio 3-----------------------------
def verificar_par_impar(numero):
    if numero % 2 == 0:
        print(f"par {numero}")
    else:
        print(f"Impar {numero}")


# Solicitar ao usuário para inserir um número
numero = int(input("Digite um número: "))

# Verificar se o número é par ou ímpar
verificar_par_impar(numero)



