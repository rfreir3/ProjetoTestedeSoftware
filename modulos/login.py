import sqlite3

def login(usuario, senha):
    try:
        with sqlite3.connect("modulos\\Bookpy.db") as connection:
            cursor = connection.cursor()

            cursor.execute("SELECT Username, Password FROM users")
            dados = cursor.fetchall()

            for linha in dados:
                if usuario == linha[0] and senha == linha[1]:    
                    connection.commit()
                    return "Usuário encontrado!"
                else:
                    continue

            connection.commit()
            return "Usuário não cadastrado"
    except sqlite3.Error as e:
        print(f"Erro ao inserir dados no banco de dados: {e}")
