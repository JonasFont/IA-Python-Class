import matplotlib.pyplot as plt

# Dados para o gráfico
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Criar o gráfico de linha
plt.scatter(x, y, label='Pontos', color='green')

# Adicionar título e rótulos aos eixos
plt.title('Exemplo de Gráfico de Linha')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adicionar uma legenda
plt.legend()

# Exibir o gráfico
plt.show()

#-----------------------------------------------------
#Gráficos de Linhas:
plt.plot(x, y, label='Linha 1')
plt.legend()

#Gráficos de Barras:

plt.bar(x, y, label='Barras', color='blue')
plt.legend()

#Histograma:
plt.hist(y, bins=5, label='Histograma', color='green')
plt.legend()

#Gráficos de Dispersão:
plt.scatter(x, y, label='Pontos', color='red')
plt.legend()

#Gráficos de Pizza:
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Gráfico de Pizza')