import seaborn as sns
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# pip install openpyxl seaborn pandas matplotlib

# Conectar ao banco de dados e criar a tabela se não existir
conn = sqlite3.connect('saude.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS pacientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    genero TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS metricas_saude (
    id INTEGER PRIMARY KEY,
    paciente_id INTEGER,
    data DATE NOT NULL,
    pressao_arterial TEXT,
    frequencia_cardiaca INTEGER,
    peso REAL,
    FOREIGN KEY(paciente_id) REFERENCES pacientes(id)
)
''')
conn.commit()

# Função para inserir um novo paciente
def inserir_paciente():
    nome = input("Digite o nome do paciente: ")
    idade = int(input("Digite a idade do paciente: "))
    genero = input("Digite o gênero do paciente: ")
    cursor.execute('''
    INSERT INTO pacientes (nome, idade, genero) VALUES (?, ?, ?)
    ''', (nome, idade, genero))
    conn.commit()
    print("Paciente adicionado com sucesso.")

# Função para inserir métricas de saúde
def inserir_metricas():
    paciente_id = int(input("Digite o ID do paciente: "))
    data = input("Digite a data (YYYY-MM-DD): ")
    pressao_arterial = input("Digite a pressão arterial (ex: 120/80): ")
    frequencia_cardiaca = int(input("Digite a frequência cardíaca: "))
    peso = float(input("Digite o peso: "))
    cursor.execute('''
    INSERT INTO metricas_saude (paciente_id, data, pressao_arterial, frequencia_cardiaca, peso)
    VALUES (?, ?, ?, ?, ?)
    ''', (paciente_id, data, pressao_arterial, frequencia_cardiaca, peso))
    conn.commit()
    print("Métricas de saúde adicionadas com sucesso.")

# Função para exibir todos os pacientes
def exibir_pacientes():
    df = pd.read_sql_query('SELECT * FROM pacientes', conn)
    print(df)

# Função para exibir métricas de saúde de um paciente
def exibir_metricas():
    paciente_id = int(input("Digite o ID do paciente: "))
    df = pd.read_sql_query('SELECT * FROM metricas_saude WHERE paciente_id = ?', conn, params=(paciente_id,))
    print(df)

# Função para importar dados de um arquivo Excel
def importar_excel():
    root = tk.Tk()
    root.withdraw()
    arquivo_selecionado = filedialog.askopenfilename(
        title="Selecione o arquivo Excel",
        filetypes=(("Arquivos Excel", "*.xlsx"), ("Todos os arquivos", "*.*"))
    )
    if not arquivo_selecionado:
        print("Nenhum arquivo selecionado.")
        return None

    df = pd.read_excel(arquivo_selecionado)
    df.to_sql('metricas_saude', conn, if_exists='append', index=False)
    print(f"Dados importados de {arquivo_selecionado} com sucesso.")
    return arquivo_selecionado

# Função para exportar dados para Excel
def exportar_excel():
    df = pd.read_sql_query('SELECT * FROM metricas_saude', conn)
    df.to_excel('metricas_saude.xlsx', index=False)
    print("Dados exportados com sucesso!")

# Função para visualizar métricas de saúde ao longo do tempo
def visualizar_metricas():
    paciente_id = int(input("Digite o ID do paciente: "))
    df = pd.read_sql_query('SELECT * FROM metricas_saude WHERE paciente_id = ?', conn, params=(paciente_id,))
    sns.lineplot(data=df, x='data', y='frequencia_cardiaca', marker='o', label='Frequência Cardíaca')
    sns.lineplot(data=df, x='data', y='peso', marker='o', label='Peso')
    plt.xlabel('Data')
    plt.ylabel('Valores')
    plt.title('Métricas de Saúde ao Longo do Tempo')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()

# Menu interativo
while True:
    print("\nMenu:")
    print("1. Inserir paciente")
    print("2. Inserir métricas de saúde")
    print("3. Exibir todos os pacientes")
    print("4. Exibir métricas de saúde de um paciente")
    print("5. Importar dados de Excel")
    print("6. Exportar dados para Excel")
    print("7. Visualizar métricas de saúde")
    print("0. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        inserir_paciente()
    elif escolha == '2':
        inserir_metricas()
    elif escolha == '3':
        exibir_pacientes()
    elif escolha == '4':
        exibir_metricas()
    elif escolha == '5':
        importar_excel()
    elif escolha == '6':
        exportar_excel()
    elif escolha == '7':
        visualizar_metricas()
    elif escolha == '0':
        print("Saindo...")
        break
    else:
        print("Opção inválida, tente novamente.")

# Fechar o cursor e a conexão
cursor.close()
conn.close()
