import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('exemplo.db')

# Criar um cursor
cursor = conn.cursor()

# Criar uma tabela
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

# Consultar dados
cursor.execute('SELECT * FROM usuarios')
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)


# Fechar o cursor e a conexão
cursor.close()
conn.close()