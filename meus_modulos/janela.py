import customtkinter as ctk
from tkinter import *

janela = ctk.CTk()

class Application():
    def __init__(self):
        self.janela = janela 
        self.tema()
        self.tela()
        self.tela_login()
        self.clique()
        janela.mainloop()

    def tema(self):    
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def clique(self):
        print("Funcionando")

    def tela(self):
        janela.geometry("430x350")
        janela.title("Minha Biblioteca")
        #janela.resizable(False, False)

    def tela_login(self):
        texto = ctk.CTkLabel(janela, text= "Bem vindo ao Sistema de Gerenciamento de Bibliotecas", font=("Roboto", 15))
        texto.pack(padx=10, pady=10)

        login_entry = ctk.CTkEntry(janela, placeholder_text= "Login")
        login_entry.pack(padx= 10, pady= 10) 

        senha_entry = ctk.CTkEntry(janela, placeholder_text= "Senha", show= "*")
        senha_entry.pack(padx= 10, pady=10)

        check_box= ctk.CTkCheckBox(janela, text= "Lembre-se de mim")
        check_box.pack(padx= 0, pady= 10)

        login_button = ctk.CTkButton(janela, text= "Login", command= self.clique)
        login_button.pack(padx=10, pady=10)

        register_span = ctk.CTkLabel(janela, text= "Caso não tenha conta, cadastre-se")
        register_span.pack(padx= 10, pady= 10)
        
        def clique_register():
            janela_register= ctk.TopLevel()
            

        register_button = ctk.CTkButton(janela, text= "Cadastre-se", command= clique_register)
        register_button.pack(padx=10, pady=10)

Application()