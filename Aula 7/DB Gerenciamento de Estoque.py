import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# pip install openpyxl seaborn pandas matplotlib

# Conectar ao banco de dados e criar a tabela se não existir
conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    preco REAL NOT NULL
)
''')
conn.commit()


# Função para inserir um novo produto
def inserir_produto():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    preco = float(input("Digite o preço do produto: "))
    cursor.execute('''
    INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)
    ''', (nome, quantidade, preco))
    conn.commit()
    print("Produto adicionado com sucesso.")


# Função para atualizar um produto existente
def atualizar_produto():
    id_produto = int(input("Digite o ID do produto a ser atualizado: "))
    novo_nome = input("Digite o novo nome do produto (ou pressione Enter para manter o atual): ")
    nova_quantidade = input("Digite a nova quantidade do produto (ou pressione Enter para manter a atual): ")
    novo_preco = input("Digite o novo preço do produto (ou pressione Enter para manter o atual): ")

    if novo_nome:
        cursor.execute('''
        UPDATE produtos
        SET nome = ?
        WHERE id = ?
        ''', (novo_nome, id_produto))
    if nova_quantidade:
        cursor.execute('''
        UPDATE produtos
        SET quantidade = ?
        WHERE id = ?
        ''', (int(nova_quantidade), id_produto))
    if novo_preco:
        cursor.execute('''
        UPDATE produtos
        SET preco = ?
        WHERE id = ?
        ''', (float(novo_preco), id_produto))

    conn.commit()
    print("Produto atualizado com sucesso.")


# Função para remover um produto
def remover_produto():
    id_produto = int(input("Digite o ID do produto a ser removido: "))
    cursor.execute('''
    DELETE FROM produtos
    WHERE id = ?
    ''', (id_produto,))
    conn.commit()
    print("Produto removido com sucesso.")


# Função para exibir todos os produtos
def exibir_produtos():
    df = pd.read_sql_query('SELECT * FROM produtos', conn)
    print(df)




# Função para exportar dados para Excel
def exportar_excel():
    df = pd.read_sql_query('SELECT * FROM produtos', conn)
    df.to_excel('produtos.xlsx', index=False)
    print("Dados exportados com sucesso!")


def visualizar_estoque():
    # Ler os dados da tabela 'produtos' do banco de dados SQLite
    df = pd.read_sql_query('SELECT * FROM produtos', conn)

    # Criar o gráfico de barras
    plt.figure(figsize=(10, 6))  # Define o tamanho da figura

    plt.bar(df['nome'], df['quantidade'], color='blue')  # Cria o gráfico de barras
    plt.xlabel('Produto')  # Rótulo do eixo x
    plt.ylabel('Quantidade')  # Rótulo do eixo y
    plt.title('Quantidade de Produtos em Estoque')  # Título do gráfico
    plt.xticks(rotation=90)  # Rotaciona os rótulos no eixo x para melhorar a legibilidade

    plt.tight_layout()  # Ajusta o layout para evitar que os rótulos se sobreponham
    plt.show()  # Exibe o gráfico
# Menu interativo
while True:
    print("\nMenu:")
    print("1. Inserir produto")
    print("2. Atualizar produto")
    print("3. Remover produto")
    print("4. Exibir todos os produtos")
    print("5. Importar dados de Excel")
    print("6. Exportar dados para Excel")
    print("7. Visualizar estoque")
    print("0. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        inserir_produto()
    elif escolha == '2':
        atualizar_produto()
    elif escolha == '3':
        remover_produto()
    elif escolha == '4':
        exibir_produtos()
    elif escolha == '5':
        pass
    elif escolha == '6':
        exportar_excel()
    elif escolha == '7':
        visualizar_estoque()
    elif escolha == '0':
        print("Saindo...")
        break
    else:
        print("Opção inválida, tente novamente.")

# Fechar o cursor e a conexão
cursor.close()
conn.close()
