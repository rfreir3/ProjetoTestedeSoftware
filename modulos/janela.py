import customtkinter as ctk

from tkinter import *

from tkinter import messagebox

from register import insert_into_database as insert_database

janela = ctk.CTk()

class Application():
    def __init__(self):
        self.janela = janela 
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()

    #definição do tema da janela inicial

    def tema(self):    
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    #definição do tamanho, título e desativação de redimensionar a janela

    def tela(self):
        janela.geometry("430x370")
        janela.title("Minha Biblioteca")
        janela.maxsize(700, 800)
        janela.minsize(300, 200)
        janela.resizable(FALSE, FALSE)

    #função responsável por definir o conteúdo da janela de login    
        
    def tela_login(self):

        #função de ação para quando o botão de cadastro for apertado
        def clique_register():
            #apaga o frame de login
            login_frame.pack_forget()

            #adiciona frame de cadastro 
            register_frame= ctk.CTkFrame(janela)
            register_frame.pack(padx= 10, pady= 10)
            label= ctk.CTkLabel(register_frame, text= "Preencha corretamente todos os campos abaixos\n com as informações solicitadas ", font= ("Roboto", 15))
            label.pack(padx= 10, pady= 10)
            
            #adiciona campos de login, email e senha
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

            def save_user():
                #verifica se as duas senhas são iguais
                if(senha_entry.get() == confirmar_senha.get()):
                    insert_database(str(login_entry.get()), str(email_entry.get()), str(senha_entry.get()))
                    messagebox.showinfo(title= "Estado do Cadastro", message= "Usuário cadastrado com sucesso.")
                else:
                    messagebox.showinfo(title= "Estado do Cadastro", message= "Senhas não compatíveis. Por favor, tente novamente")
                    
            save_button= ctk.CTkButton(register_frame, text= "Cadastrar-se", command= save_user)
            save_button.pack(padx= 10, pady= 7)

            def back():
                register_frame.pack_forget()
                login_frame.pack()

            back_button= ctk.CTkButton(register_frame, text= "Voltar à área de login", command= back)
            back_button.pack(padx= 10, pady= 7)
            
        #adiciona um frame na janela para que sirva de suporte para os botões, labels, entradas e etc.

        login_frame = ctk.CTkFrame(janela)
        login_frame.place(x=10, y=60)
        login_frame.configure(width= 300, height= 50)
            
        #adiciona label
        texto = ctk.CTkLabel(login_frame, text= "Entre na sua conta BookPy!", font=("Roboto", 15))
        texto.pack(padx= 10, pady= 10)
            
        #adiciona a caixa de entrada para login, senha e checkbox "lembre-se de mim"
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
    
        #função de ação para quando o botão para logar for apertado
        def clique_login():
            print("funcionando")

        #adiciona o botão
        login_button = ctk.CTkButton(login_frame, text= "Login", command= clique_login)
        login_button.place(x=10, y=190)
        login_button.configure(width=100, height=35)   
Application()