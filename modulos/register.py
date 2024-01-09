from modulos.janela import login_entry, senha_entry, email_entry
import modulos.database as database


database.cursor.execute("""
    INSERT INTO users VALUES(login_entry, senha_entry, email_entry)
)""")

database.connect.commit()