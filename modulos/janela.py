import customtkinter as ctk

from tkinter import *

from tkinter import messagebox

from register import insert_into_database as insert_database

from login import login

janela = ctk.CTk()

class Application():
    def __init__(self):
        self.janela = janela 
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()

    def tema(self):    
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        janela.geometry("430x370")
        janela.title("Minha Biblioteca")
        janela.maxsize(700, 800)
        janela.minsize(300, 200)
        janela.resizable(FALSE, FALSE)
        
    def tela_login(self):
        def clique_register():
            def save_user():
                if(senha_entry.get() == confirmar_senha.get()):
                    result = insert_database(str(login_entry.get()), str(email_entry.get()), str(senha_entry.get()))

                    messagebox.showinfo(title= "Estado do Cadastro", message= result)
                    
                else:
                    messagebox.showinfo(title= "Estado do Cadastro", message= "Senhas não compatíveis. Por favor, tente novamente")
            
            def back():
                register_frame.pack_forget()
                login_frame.pack()

            login_frame.pack_forget()

            register_frame= ctk.CTkFrame(janela)
            register_frame.pack(padx= 10, pady= 10)
            label= ctk.CTkLabel(register_frame, text= "Preencha corretamente todos os campos abaixos\n com as informações solicitadas ", font= ("Roboto", 15))
            label.pack(padx= 10, pady= 10)
            
            login_entry= ctk.CTkEntry(register_frame, placeholder_text= "Nome de usuário")
            login_entry.pack(padx= 10, pady= 7)
            email_entry= ctk.CTkEntry(register_frame, placeholder_text= "E-mail")
            email_entry.pack(padx= 10, pady= 7)
            senha_entry= ctk.CTkEntry(register_frame, placeholder_text= "Senha", show= "*")
            senha_entry.pack(padx= 10, pady= 7)
            confirmar_senha= ctk.CTkEntry(register_frame, placeholder_text= "Confirmar senha", show= "*")
            confirmar_senha.pack(padx= 10, pady= 7) 

            check_box= ctk.CTkCheckBox(register_frame, text= "Aceito todos os termos e condições")
            check_box.pack(padx= 10, pady= 7)

                    
            save_button= ctk.CTkButton(register_frame, text= "Cadastrar-se", command= save_user)
            save_button.pack(padx= 10, pady= 7)

            back_button= ctk.CTkButton(register_frame, text= "Voltar à área de login", command= back)
            back_button.pack(padx= 10, pady= 7)

        login_frame = ctk.CTkFrame(janela)
        login_frame.place(x=10, y=60)
        login_frame.configure(width= 300, height= 50)
            
        texto = ctk.CTkLabel(login_frame, text= "Entre na sua conta BookPy!", font=("Roboto", 15))
        texto.pack(padx= 10, pady= 10)
            
        login_entry = ctk.CTkEntry(login_frame, placeholder_text= "Login")
        login_entry.pack(padx=10, pady=10)
        login_entry.configure(width= 400, height= 50)
        
        senha_entry = ctk.CTkEntry(login_frame, placeholder_text= "Senha", show= "*")
        senha_entry.pack(padx= 10, pady= 10)
        senha_entry.configure(width= 400, height= 50)
        
        check_box= ctk.CTkCheckBox(login_frame, text= "Lembre-se de mim")
        check_box.pack(padx=10, pady=10)

        register_button = ctk.CTkButton(login_frame, text= "Cadastre-se", command= clique_register)
        register_button.place(x=310, y= 190)
        register_button.configure(width=100, height=35)
    
        def clique_login():
            result = login(login_entry.get(), senha_entry.get())
            messagebox.showinfo(title= "Estado de Login", message= result)

        login_button = ctk.CTkButton(login_frame, text= "Login", command= clique_login)
        login_button.place(x=10, y=190)
        login_button.configure(width=100, height=35)   
Application()
