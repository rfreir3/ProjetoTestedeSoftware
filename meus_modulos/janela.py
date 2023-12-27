import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

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
        janela.resizable(False, False)
    
    def tela_login(self):
        login_frame = ctk.CTkFrame(janela)
        login_frame.pack(padx= 10, pady= 10)
        
        texto = ctk.CTkLabel(login_frame, text= "Bem vindo ao Sistema de Gerenciamento de Bibliotecas", font=("Roboto", 15))
        texto.pack(padx= 10, pady= 10)
        
        login_entry = ctk.CTkEntry(login_frame, placeholder_text= "Login")
        login_entry.pack(padx= 10, pady= 10) 

        senha_entry = ctk.CTkEntry(login_frame, placeholder_text= "Senha", show= "*")
        senha_entry.pack(padx= 10, pady=10)

        check_box= ctk.CTkCheckBox(login_frame, text= "Lembre-se de mim")
        check_box.pack(padx= 0, pady= 10)

        def clique_login():
            print("funcionando")

        login_button = ctk.CTkButton(login_frame, text= "Login", command= clique_login)
        login_button.pack(padx=10, pady=10)

        register_span = ctk.CTkLabel(login_frame, text= "Caso não tenha conta, cadastre-se")
        register_span.pack(padx= 10, pady= 10)

        def clique_register():
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

            if senha_entry != confirmar_senha:
                messagebox.showerror(title= "Estado do Cadastro", message= "Senha incorreta, tente novamente")    

            check_box= ctk.CTkCheckBox(register_frame, text= "Aceito todos os termos e condições")
            check_box.pack(padx= 10, pady= 7)

            def save_user():
                msg= messagebox.showinfo(title= "Estado do Cadastro", message= "Usuário cadastrado com sucesso.")

            save_button= ctk.CTkButton(register_frame, text= "Cadastrar-se", command= save_user)
            save_button.pack(padx= 10, pady= 7)

            def back():
                register_frame.pack_forget()
                login_frame.pack()

            back_button= ctk.CTkButton(register_frame, text= "Voltar à área de login", command= back)
            back_button.pack(padx= 10, pady= 7)

        register_button = ctk.CTkButton(login_frame, text= "Cadastre-se", command= clique_register)
        register_button.pack(padx= 10, pady= 7)

        

Application()