import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# pip install openpyxl
# pip install pandas
# pip install matplotlib

# Conectar ao banco de dados SQLite (usando um arquivo .db)
conn = sqlite3.connect('pandas.db')
cursor = conn.cursor()

# Criar uma tabela se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER,
    email TEXT UNIQUE NOT NULL
)
''')
conn.commit()

# Inserir alguns dados na tabela (se necessário)
def inserir_dados():
    nome = input("Digite o nome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    email = input("Digite o email do usuário: ")
    cursor.execute('''
        INSERT INTO usuarios (nome, idade, email) VALUES (?, ?, ?)
        ''', (nome, idade, email))
    conn.commit()
    print("Usuário adicionado com sucesso.")

# Função para exportar para CSV
def exportar_para_csv():
    df = pd.read_sql_query('SELECT * FROM usuarios', conn)
    df.to_csv('usuarios.csv', index=False)
    print("Dados exportados para usuarios.csv com sucesso.")

# Função para exportar para Excel
def exportar_para_excel():
    df = pd.read_sql_query('SELECT * FROM usuarios', conn)
    df.to_excel('usuarios.xlsx', index=False)
    print("Dados exportados para usuarios.xlsx com sucesso.")

# Função para visualizar os dados
def visualizar_dados():
    df = pd.read_sql_query('SELECT * FROM usuarios', conn)
    df['idade'].hist()
    plt.xlabel('Idade')
    plt.ylabel('Frequência')
    plt.title('Distribuição de Idades dos Usuários')
    plt.show()

# Função para importar dados de um arquivo Excel
def importar_de_excel():
    root = tk.Tk()
    root.withdraw()

    # Abre uma janela de diálogo para selecionar um arquivo Excel
    arquivo_selecionado = filedialog.askopenfilename(
        title="Selecione o arquivo Excel",
        filetypes=(("Arquivos Excel", "*.xlsx"), ("Todos os arquivos", "*.*"))
    )

    if not arquivo_selecionado:
        print("Nenhum arquivo selecionado.")
        return None

    # Ler os dados do arquivo Excel para um DataFrame
    df = pd.read_excel(arquivo_selecionado)

    # Insere os dados no banco de dados SQLite
    df.to_sql('usuarios', conn, if_exists='append', index=False)

    print(f"Dados importados de {arquivo_selecionado} com sucesso.")
    return arquivo_selecionado

# Função para exibir todos os usuários
def exibir_todos_usuarios():
    df = pd.read_sql_query('SELECT * FROM usuarios', conn)
    print(df)

# Menu principal
while True:
    try:
        print("\nMenu:")
        print("1. Inserir usuário")
        print("2. Mostrar dados")
        print("3. Importar dados de arquivo Excel")
        print("4. Visualizar distribuição de idades")
        print("5. Exportar dados para CSV")
        print("6. Exportar dados para Excel")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            inserir_dados()
        elif escolha == '2':
            exibir_todos_usuarios()
        elif escolha == '3':
            importar_de_excel()
        elif escolha == '4':
            visualizar_dados()
        elif escolha == '5':
            exportar_para_csv()
        elif escolha == '6':
            exportar_para_excel()
        elif escolha == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")
    except Exception as e:
        print(f"Erro: {e}")

# Fechar o cursor e a conexão com o banco de dados
cursor.close()
conn.close()
