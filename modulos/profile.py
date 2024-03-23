import customtkinter as ctk

from tkinter import messagebox

from tkinter.filedialog import askopenfilename

import requests

import json

import sqlite3

from PIL import Image, ImageTk

janela = ctk.CTk()

class User():
    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.password = password
        self.email = email
        self.posts = []

class Profile():
    def __init__(self):
        self.janela = janela
        self.image = ""
        self.tema()
        self.tela_resolucao()
        self.tela_user()
        janela.mainloop()

    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela_resolucao(self, tamanho = "700x500"):
        janela.geometry(tamanho)
        janela.title("BookPy")
        janela.maxsize(700, 800)
        janela.minsize(300, 200)
        janela.resizable(True, True)   

    def tela_user(self):
        def add_image():
            filepath = askopenfilename(filetypes=[("Imagem", "*.png"), ("Imagem", "*.jpg"), ("Imagem", "*.jpeg")])

            if filepath :
                self.image = filepath

                my_image = Image.open(filepath)
                my_image = my_image.resize((200, 200))
                
                my_image = ImageTk.PhotoImage(my_image)
                
                image_frame = ctk.CTkFrame(post_here_frame, height= 30, fg_color= "transparent")
                image_frame.pack(side="top", padx= 10, pady= 10)  

                local_image = ctk.CTkLabel(image_frame, image=my_image, text="")
                local_image.image = my_image
                local_image.pack(padx= 10, pady= 10)

                adress_image = ctk.CTkLabel(image_frame, text= self.image, font= ("Roboto", 10))
                adress_image.pack(padx= 10, pady= 10)
            
            else:
                 messagebox.showinfo(title= "Erro ao selecionar imagem", message= "Você precisa selecionar uma imagem")
        
        def get__current_date(api_key):
            response = requests.get(f"https://api.abstractapi.com/v1/timezone?api_key={api_key}")
            data = response.json()
            return data['datetime']
        
        def add_post(self, content):
            
            post = {
                "content": content,
                "image": self.image,
                "date": get__current_date("https://ipgeolocation.abstractapi.com/v1?ip_address=200.137.6.63"),
                "author": self.username,
                "likes": 0,
                "comments": []
            }
            self.posts.append(post)

        user_frame = ctk.CTkFrame(janela)
        user_frame.pack(padx= 10, pady= 10)

        side_bar_frame = ctk.CTkFrame(user_frame, width= 100)
        side_bar_frame.pack(side= "left", padx= 10, pady= 10)

        titulo = ctk.CTkLabel(side_bar_frame, text= "BookPy", font= ("Roboto", 20))
        titulo.pack(padx= 10, pady= 10)

        perfil_button = ctk.CTkButton(side_bar_frame, text= "Perfil", font= ("Roboto", 15), fg_color= "#363636", hover_color="#4F4F4F")
        perfil_button.pack(padx= 10, pady= 10)
        
        main_frame = ctk.CTkFrame(user_frame, width= 800)
        main_frame.pack(side= "right", padx= 10, pady= 10)

        post_here_frame = ctk.CTkFrame(main_frame)
        post_here_frame.pack(side= "top", padx= 10, pady= 10)

        post_here_entry = ctk.CTkEntry(post_here_frame, placeholder_text= "Escreva aqui o seu post", width= 500, height= 40)
        post_here_entry.pack(padx= 10, pady= 10)

        buttons_frame = ctk.CTkFrame(post_here_frame, fg_color= "transparent")
        buttons_frame.pack(side= "bottom",padx= 10, pady= 10)

        post_button = ctk.CTkButton(buttons_frame, text= "Postar", font= ("Roboto", 15), width= 100, fg_color= "#363636", hover_color="#4F4F4F", command= lambda: add_post(self, 
        post_here_entry.get(), self.image))
        post_button.pack(side="left", padx= 10, pady= 10)

        spacer = ctk.CTkFrame(buttons_frame, width= 160, height=1)
        spacer.pack(side="left", padx= 10, pady= 10)
        
        add_image_button = ctk.CTkButton(buttons_frame, text= "Buscar imagem", font= ("Roboto", 15), fg_color= "#363636", hover_color="#4F4F4F", command= lambda: add_image())
        add_image_button.pack(side="left", padx= 10, pady= 10)

    def remove_post(self, title):
        for post in self.posts:
            if post["title"] == title:
                self.posts.remove(post)
                return "Post removido com sucesso"
        return "Post não encontrado"

    def edit_post(self, title, new_title, new_book, new_content):
        for post in self.posts:
            if post["title"] == title:
                post["title"] = new_title
                post["book"] = new_book
                post["content"] = new_content
                return "Post editado com sucesso"
        return "Post não encontrado"   
Profile()     