# Operadores Aritméticos:
# Esses operadores são usados para realizar operações matemáticas com valores numéricos:

a = 10
b = 11

soma = a + b  # Aqui criamos uma variável para armazenar o valor da soma das variáveis (a) e (b)
print(soma)  # Depois utilizamos a função print() para retornar o valor para nós

subtracao = a - b  # Subtração das variáveis (a) e (b)
print(subtracao)

multi = a * b  # Multiplicação das variáveis (a) e (b)
print(multi)

div = a / b  # Divisão das variáveis (a) e (b)
print(div)

expo = a ** b  # Exponenciação da variável (a) elevada à variável (b)
print(expo)

resto = a % b  # Resto da divisão de (a) por (b)
print(resto)

# Utilizando a função input() para captar um dado do usuário

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

# Observação: Se não convertemos a função input para int ele irá armazenar dentro das variáveis
# valores do tipo string, perceba que dentro da função input("Utilizamos aspas")

# Operadores de Atribuição:

# Atribuição (=):
# O operador de atribuição (=) é usado para atribuir um valor a uma variável.

y = 5
y += 3  # Equivalente a y = y + 3
# Agora y é 8

z = 20
z -= 7  # Equivalente a z = z - 7
# Agora z é 13

w = 3
w *= 4  # Equivalente a w = w * 4
# Agora w é 12

# Operadores de Comparação:

# Igual (==): Verifica se os valores são iguais.
# Diferente (!=): Verifica se os valores são diferentes.
# Maior que (>): Verifica se o primeiro valor é maior que o segundo.
# Menor que (<): Verifica se o primeiro valor é menor que o segundo.
# Maior ou igual a (>=): Verifica se o primeiro valor é maior ou igual ao segundo.
# Menor ou igual a (<=): Verifica se o primeiro valor é menor ou igual ao segundo.

a = 10
b = 5

print(a == b)  # A expressão a == b é falsa, pois 10 não é igual a 5!
print(a != b)  # A expressão a != b é verdadeira, pois 10 é diferente de 5!
print(a > b)   # A expressão a > b é verdadeira!
print(a < b)   # A expressão a < b é falsa!
print(a >= b)  # A expressão a >= b é verdadeira!
print(a <= b)  # A expressão a <= b é falsa!

# Lembre-se de que os operadores de comparação são amplamente usados em
# estruturas condicionais (como if, elif e else) para tomar decisões com base em valores.

# E (and): Retorna True se ambas as expressões forem verdadeiras.
# OU (or): Retorna True se pelo menos uma das expressões for verdadeira.
# NÃO (not): Inverte o valor da expressão.

x = 10
y = 5
resultado = (x > 0) and (y < 10)  # And significa "e"
# O resultado é True, pois ambas as expressões são verdadeiras

a = 15
b = 20
resultado = (a > 10) or (b < 5)  # Or significa "ou"
# O resultado é True, pois a primeira expressão é verdadeira

c = True
resultado = not c
# O resultado é False, pois inverte o valor de c

# Operadores de Associação:
# Esses operadores testam se um valor está presente em uma sequência (como uma lista, tupla ou conjunto):
# Em (in): Retorna True se o valor estiver na sequência.

numeros = [1, 2, 3, 4, 5]
resultado = 3 in numeros
# O resultado é True, pois 3 está na lista
