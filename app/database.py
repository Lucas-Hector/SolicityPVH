# import sqlite3

# def init_db():
#     try:
#         # Conecta (e cria) ao banco de dados 'solicity.db'
#         conn = sqlite3.connect('solicity.db')
#         cursor = conn.cursor()

#         # Cria a tabela 'usuarios'
#         cursor.execute('''
#         CREATE TABLE IF NOT EXISTS usuarios (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             nome TEXT NOT NULL,
#             email TEXT NOT NULL UNIQUE,
#             celular TEXT,
#             cpf TEXT NOT NULL UNIQUE,
#             senha TEXT NOT NULL,
#             genero INTEGER 
#         );
#         ''')
        
#         # Genero será armazenado como INTEGER:
#         # 1: Feminino
#         # 2: Masculino
#         # 3: Outros
#         # 4: Prefiro não dizer

#         conn.commit()
#         print("Banco de dados 'solicity.db' e tabela 'usuarios' criados com sucesso.")
    
#     except sqlite3.Error as e:
#         print(f"Erro ao inicializar o banco de dados: {e}")
    
#     finally:
#         if conn:
#             conn.close()

# if __name__ == '__main__':
#     init_db()