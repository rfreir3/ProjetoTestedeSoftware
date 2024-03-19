import customtkinter as ctk

from tkinter import Tk

from tkinter.filedialog import askopenfilename

import requests

import json

import sqlite3

from PIL import Image, ImageTk

janela = ctk.CTk()

class Profile():
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.posts = []

class User():
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela_resolucao()
        self.tela_user()
        janela.mainloop()

    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela_resolucao(self):
        janela.geometry("700x500")
        janela.title("BookPy")
        janela.maxsize(700, 800)
        janela.minsize(300, 200)
        janela.resizable(True, True)   

    def tela_user(self):
        def add_image(self):
            user_frame.pack_forget()

            image_frame = ctk.CTkFrame(janela)
            image_frame.pack(padx= 10, pady= 10)

            filepath = askopenfilename(filetypes=[("Imagem", "*.png"), ("Imagem", "*.jpg"), ("Imagem", "*.jpeg")])

            if filepath :
                image = Image.open(filepath)
                image = image.resize((300, 300), Image.ANTIALIAS)

                
                image = ImageTk.PhotoImage(image)

                image_label = ctk.CTkLabel(image_frame, image= image)
                image_label.image = image
                image_label.pack(padx= 10, pady= 10)

        def get__current_date(api_key):
            response = requests.get(f"https://api.abstractapi.com/v1/timezone?api_key={api_key}")
            data = response.json()
            return data['datetime']
        
        def add_post(self, content):
            post = {
                "content": content,
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

        add_image_button = ctk.CTkButton(post_here_frame, text= "Adicionar imagem", font= ("Roboto", 15), fg_color= "#363636", hover_color="#4F4F4F", command= lambda: add_image(self))
        add_image_button.pack(side="right", padx= 10, pady= 10)

        post_button = ctk.CTkButton(post_here_frame, text= "Postar", font= ("Roboto", 15), fg_color= "#363636", hover_color="#4F4F4F", command= lambda: add_post(self, 
        post_here_entry.get()))
        post_button.pack(side="left", padx= 10, pady= 10)

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
User()     