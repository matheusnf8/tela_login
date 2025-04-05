import os
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Obter o caminho real do banco de dados
cursor.execute("PRAGMA database_list")
banco_ativo = cursor.fetchone()[2]

print(f"O banco de dados ativo está em: {banco_ativo}")

# Fechar conexão
conn.close()
