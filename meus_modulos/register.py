from janela import login_entry, senha_entry, email_entry
import database


database.cursor.execute("""
    INSERT INTO users VALUES(login_entry, senha_entry, email_entry)
)""")

database.connect.commit()