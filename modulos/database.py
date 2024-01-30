import sqlite3

with sqlite3.connect("modulos\\SistemaDeBiblioteca.db") as connect:
    cursor = connect.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(         
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Username TEXT NOT NULL,
        Email TEXT NOT NULL,
        Password TEXT NOT NULL     
    )""")
    print("Conexão feita com sucesso")
