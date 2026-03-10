try:
    # Código que pode gerar uma exceção
    x = 1 / 0
except:
    # Código que será executado se uma exceção ocorrer
    print("Ocorreu um erro!")

#----------------------------------------------------------
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Divisão por zero não é permitida!")

#----------------------------------------------------------

try:
    x = 1 / 0
except (ZeroDivisionError, ValueError):
    print("Ocorreu um erro de divisão por zero ou um valor inválido!")

#-----------------------------------------------------------

try:
    x = 1 / 1
except ZeroDivisionError:
    print("Divisão por zero não é permitida!")
else:
    print("Nenhuma exceção ocorreu, o resultado é:", x)

#-----------------------------------------------------------

try:
    x = 1 / 1
except ZeroDivisionError:
    print("Divisão por zero não é permitida!")
else:
    print("Nenhuma exceção ocorreu, o resultado é:", x)
finally:
    print("Esta mensagem é sempre exibida, independentemente de erros.")

#-----------------------------------------------------------

try:
    nome = jonas

    print(nome)

except NameError:
    print("Defina o valor da variavel corretamente")


#------------------------------------------------------------
try:
    n1 = 10
    n2 = 0  # Divisão por zero para gerar uma exceção

    if n1 > 15:
        print(True)

    resultado = n1 / n2  # Isto levantará uma ZeroDivisionError
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

#Função except Exception as e serve para capturar qaulquer erro inesperado que aconteca

#-----------------------------------------------------------------------
try:
    arquivo = open('meuarquivo.txt', 'r')
    conteudo = arquivo.read()
    # Processar o conteúdo do arquivo
except FileNotFoundError:
    print("Arquivo não encontrado!")
finally:
    arquivo.close()


#---------------------------------------------------------------------------

try:
    # Código que pode gerar um ValueError
    idade = int(input("Digite sua idade: "))
except ValueError:
    print("Ocorreu um erro! Certifique-se de digitar um número inteiro para a idade.")
#-----------------------------------------------------------------------

try:
    # Código que pode gerar um TypeError
    resultado = 10 + "5"
except TypeError:
    print("Ocorreu um erro! Certifique-se de que os tipos de dados sejam compatíveis para a operação desejada.")

#------------------------------------------------------------------------
try:
    # Tente usar uma variável ou nome que não está definido
    print(variavel_inexistente)
except NameError:
    print("Ocorreu um erro! Certifique-se de que a variável ou nome esteja definido antes de usá-lo.")

