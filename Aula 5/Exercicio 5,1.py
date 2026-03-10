import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Criar tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER,
    email TEXT UNIQUE NOT NULL
)
''')

# Inserir dados
cursor.execute('''
INSERT INTO usuarios (nome, idade, email) VALUES (?, ?, ?)
''', ('Alice', 30, 'alice@example.com'))

# Inserir múltiplos registros
usuarios = [
    ('Bob', 25, 'bob@example.com'),
    ('Carol', 27, 'carol@example.com'),
    ('Dave', 22, 'dave@example.com')
]
cursor.executemany('''
INSERT INTO usuarios (nome, idade, email) VALUES (?, ?, ?)
''', usuarios)



# Consultar dados
cursor.execute('SELECT * FROM usuarios')
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)


# Fechar o cursor e a conexão
cursor.close()
conn.close()

#.......................................Funções........................................
# Atualizar dados
cursor.execute('''
UPDATE usuarios
SET idade = ?
WHERE nome = ?
''', (28, 'Bob'))
conn.commit()

# Excluir dados
cursor.execute('''
DELETE FROM usuarios
WHERE nome = ?
''', ('Dave',))
conn.commit()

# Consultar valor
# (Condição) valor estabalecido na tabela exemplo = nome, idade, senha etc
# (Valor dado) que deseja acessar
query = f'SELECT * FROM usuarios WHERE {condicao} = ?'
cursor.execute(query, (valor,))

# Atualizar dados e confirmar a transação
cursor.execute('''
UPDATE usuarios
SET idade = ?
WHERE nome = ?
''', (28, 'Alice'))
conn.commit()
print("Dados atualizados e transação confirmada com sucesso.")

