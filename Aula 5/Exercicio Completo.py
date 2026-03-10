import sqlite3

# Conectar ao banco de dados e criar a tabela se não existir
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER,
    email TEXT UNIQUE NOT NULL
)
''')
conn.commit()


# Inserir um usuário
def inserir():
    nome = input("Digite o nome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    email = input("Digite o email do usuário: ")
    cursor.execute('''
    INSERT INTO usuarios (nome, idade, email) VALUES (?, ?, ?)
    ''', (nome, idade, email))
    conn.commit()
    print("Usuário adicionado com sucesso.")


# Atualizar um usuário
def atualizar():
    nome_antigo = input("Digite o nome do usuário a ser atualizado: ")
    novo_email = input("Digite o novo email do usuário: ")
    cursor.execute('''
    UPDATE usuarios
    SET email = ?
    WHERE nome = ?
    ''', (novo_email, nome_antigo))
    conn.commit()
    print("Usuário atualizado com sucesso.")


# Exibir todos os usuários
def exibir_todos_usuarios():
    cursor.execute('SELECT * FROM usuarios')
    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)


# Consultar usuários com uma condição
def consultar_usuarios(condicao, valor):
    query = f'SELECT * FROM usuarios WHERE {condicao} = ?'
    cursor.execute(query, (valor,))
    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)


# Atualizar qualquer campo do usuário
def atualizar_campo():
    escolha = input("Qual campo deseja atualizar? (nome, idade, email): ").lower()
    valor_antigo = input(f"Digite o {escolha} do usuário a ser atualizado: ")
    novo_valor = input(f"Digite o novo {escolha} do usuário: ")

    cursor.execute(f'''
    UPDATE usuarios
    SET {escolha} = ?
    WHERE {escolha} = ?
    ''', (novo_valor, valor_antigo))
    conn.commit()
    print("Usuário atualizado com sucesso.")
    exibir_todos_usuarios()  # Exibir novamente após a atualização


# Menu interativo
while True:
    print("\nMenu:")
    print("1. Inserir usuário")
    print("2. Atualizar usuário")
    print("3. Exibir todos os usuários")
    print("4. Consultar usuários")
    print("5. Atualizar qualquer campo do usuário")
    print("6. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        inserir()
    elif escolha == '2':
        atualizar()
    elif escolha == '3':
        exibir_todos_usuarios()
    elif escolha == '4':
        condicao = input("Digite o campo para a consulta (nome, idade, email): ")
        valor = input("Digite o valor para a consulta: ")
        consultar_usuarios(condicao, valor)
    elif escolha == '5':
        atualizar_campo()
    elif escolha == '6':
        print("Saindo...")
        break
    else:
        print("Opção inválida, tente novamente.")

# Fechar o cursor e a conexão
cursor.close()
conn.close()
