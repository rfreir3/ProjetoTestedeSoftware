import sqlite3

def insert_into_database(login, email, senha):
    try:
        # Conecta ao banco de dados
        with sqlite3.connect("modulos\\SistemaDeBiblioteca.db") as connection:
            # Cria um cursor a partir da conexão
            cursor = connection.cursor()

            # Executa a operação no banco de dados
            cursor.execute("INSERT INTO users (Username, Email, Password) VALUES (?, ?, ?)", (login, email, senha))

            # Executa uma consulta SQL
            cursor.execute("SELECT * FROM users")

            # Recupera todos os resultados da consulta
            resultados = cursor.fetchall()

            # Imprime os resultados
            for linha in resultados:
                print(linha)

            # Commit para salvar as alterações
            connection.commit()

    except sqlite3.Error as e:
        print(f"Erro ao inserir dados no banco de dados: {e}")