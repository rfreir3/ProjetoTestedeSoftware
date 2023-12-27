import sqlite3

connect = sqlite3.connect("meus_modulos\\SistemaDeBiblioteca.db")

cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(         
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL,
    Email TEXT NOT NULL,
    Password TEXT NOT NULL     
)""")

print("Conexão feita com sucesso")