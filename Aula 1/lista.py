# Lista

cor = ["Azul", "Branco", "Amarelo"]
#         0        1          2

# Acessando um valor específico da lista

print(cor[0])

# Adicionando valores à lista:

cor.append("Preto") # Lembrando que o comando (.append) serve para adicionar o valor ao final da lista
cor.append("Vermelho") # Corrigi o erro de digitação em "Vermelho"

# Para adicionar o valor ao início, meio ou fim da lista, pode-se utilizar a função insert()

cor.insert(0, "Marrom") # Primeiro escolha onde gostaria de inserir o valor, acessando-o através do índice, e depois determine o valor
# Adicionar elementos:
# .append(item): Adiciona um item ao final da lista.
# .extend(iterável): Adiciona todos os itens de um iterável (outra lista, por exemplo) ao final da lista.
# .insert(índice, item): Insere um item em uma posição específica.

# ---------------------------------------Remoção---------------------------------
# Remover elementos:
# .pop(índice): Remove e retorna o item no índice especificado.
# .remove(item): Remove o primeiro item com o valor especificado.

cor.pop(1) # Essa função é utilizada quando você deseja apagar um valor específico através do índice
cor.remove("Amarelo") # Essa função você remove um valor específico através de sua TAG

# ----------------------------------Outras Funções--------------------------------

# Outras operações:
# .index(item): Retorna o índice do primeiro item com o valor especificado.
# .count(item): Conta quantas vezes um item aparece na lista.
# .sort(): Ordena a lista em ordem crescente.
# .reverse(): Inverte a ordem dos elementos.

cor.count("Preto") # Retorna a quantidade de vezes que o valor Preto foi encontrado
cor.sort() # Ordena a lista em ordem crescente
cor.sort(reverse=True) # Ordena a lista em ordem decrescente
cor.reverse() # Inverte a ordem dos elementos, Exemplos: o último índice torna-se o primeiro
