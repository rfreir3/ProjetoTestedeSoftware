import customtkinter as ctk
from tkinter import messagebox, simpledialog, BooleanVar

class Application():
    def __init__(self):
        self.janela = ctk.CTk()
        self.tema()
        self.tela()
        self.usuarios_cadastrados = []
        self.livros = []
        self.usuario_lembrado = self.carregar_usuario_lembrado()
        self.lembrar_usuario = BooleanVar(value=bool(self.usuario_lembrado))
        self.tela_atual = None
        self.limpar_tela()

         #definição do tema da janela inicial
        
        if self.usuario_lembrado:
            self.mostrar_menu()
        else:
            self.mostrar_login()

        self.janela.mainloop()

    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    #definição do tamanho, título e desativação de redimensionar a janela
        
    def tela(self):
        self.janela.geometry("430x370")
        self.janela.title("Minha Biblioteca")
        self.janela.resizable(False, False)

     #função responsável por definir o conteúdo da janela de login 
        
    def mostrar_login(self):
        self.limpar_tela()

    #adiciona um frame na janela para que sirva de suporte para os botões, labels, entradas e etc.
        login_frame = ctk.CTkFrame(self.janela)
        login_frame.pack(padx=10, pady=10)

    #adiciona label
        texto = ctk.CTkLabel(login_frame, text="Bem-vindo ao Sistema de Gerenciamento de Bibliotecas!", font=("Roboto", 15))
        texto.pack(padx=10, pady=10)

        usuario_label = ctk.CTkLabel(login_frame, text="Usuário:")
        usuario_label.pack()

        self.usuario_entry = ctk.CTkEntry(login_frame)
        self.usuario_entry.pack(pady=5)
        if self.usuario_lembrado:
            self.usuario_entry.insert(0, self.usuario_lembrado)

        senha_label = ctk.CTkLabel(login_frame, text="Senha:")
        senha_label.pack()

        self.senha_entry = ctk.CTkEntry(login_frame, show="*")
        self.senha_entry.pack(pady=5)

        lembrar_usuario_checkbox = ctk.CTkCheckBox(login_frame, text="Lembrar-se de mim.", variable=self.lembrar_usuario)
        lembrar_usuario_checkbox.pack(pady=5)

        login_button = ctk.CTkButton(login_frame, text="Login", command=self.verificar_login)
        login_button.pack(pady=10)

        cadastrar_button = ctk.CTkButton(login_frame, text="Cadastrar", command=self.cadastrar_usuario)
        cadastrar_button.pack(pady=10)

        self.tela_atual = login_frame

    def carregar_usuario_lembrado(self):
        try:
            with open("usuario_lembrado.txt", "r") as file:
                return file.read().strip()
        except FileNotFoundError:
            return None

    def salvar_usuario_lembrado(self, usuario):
        with open("usuario_lembrado.txt", "w") as file:
            file.write(usuario)

    def verificar_login(self):
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        if any(u['usuario'] == usuario and u['senha'] == senha for u in self.usuarios_cadastrados):
            messagebox.showinfo("Login", "Login bem-sucedido!")
            if self.lembrar_usuario.get():
                self.salvar_usuario_lembrado(usuario)
            self.mostrar_menu()
        else:
            messagebox.showerror("Login", "Credenciais inválidas.")

    def cadastrar_usuario(self):
        novo_usuario = self.usuario_entry.get()
        nova_senha = self.senha_entry.get()

        if any(u['usuario'] == novo_usuario for u in self.usuarios_cadastrados):
            messagebox.showwarning("Cadastro", "Usuário já cadastrado.")
        else:
            self.usuarios_cadastrados.append({'usuario': novo_usuario, 'senha': nova_senha})
            messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
            self.mostrar_menu()

    def mostrar_menu(self):
        self.limpar_tela()

        adicionar_exibir_frame = ctk.CTkFrame(self.janela)
        adicionar_exibir_frame.pack(padx=10, pady=10)

        adicionar_button = ctk.CTkButton(adicionar_exibir_frame, text="Adicionar Livro", command=self.adicionar_livro)
        adicionar_button.pack(pady=10)

        exibir_button = ctk.CTkButton(adicionar_exibir_frame, text="Exibir Livros", command=self.exibir_livros)
        exibir_button.pack(pady=10)

        inserir_descricao_button = ctk.CTkButton(adicionar_exibir_frame, text="Inserir Descrição", command=self.inserir_descricao)
        inserir_descricao_button.pack(pady=10)

        remover_button = ctk.CTkButton(adicionar_exibir_frame, text="Remover Livro", command=self.remover_livro)
        remover_button.pack(pady=10)

        voltar_login_button = ctk.CTkButton(adicionar_exibir_frame, text="Voltar ao Login", command=self.mostrar_login)
        voltar_login_button.pack(pady=10)

        self.tela_atual = adicionar_exibir_frame

    def limpar_tela(self):
        if self.tela_atual:
            self.tela_atual.destroy()

    def adicionar_livro(self):
        titulo = simpledialog.askstring("Adicionar Livro", "Digite o título do livro:")
        if titulo:
            self.livros.append({'titulo': titulo})
            messagebox.showinfo("Adicionar Livro", f"Livro '{titulo}' adicionado com sucesso!")

    def exibir_livros(self):
        if not self.livros:
            messagebox.showinfo("Exibir Livros", "Nenhum livro cadastrado.")
        else:
            lista_livros = "\n".join(livro['titulo'] for livro in self.livros)
            escolha = simpledialog.askstring("Exibir Livros", f"Livros cadastrados:\n{lista_livros}\n\nDigite o título do livro para ver a descrição:")
            if escolha:
                self.ver_descricao(escolha)

    def inserir_descricao(self):
        if not self.livros:
            messagebox.showinfo("Inserir Descrição", "Nenhum livro cadastrado.")
            return

        titulo = simpledialog.askstring("Inserir Descrição", "Digite o título do livro:")
        if titulo:
            livro = next((livro for livro in self.livros if livro['titulo'] == titulo), None)
            if livro:
                descricao = simpledialog.askstring("Inserir Descrição", f"Digite a descrição para o livro '{titulo}':")
                if descricao:
                    livro['descricao'] = descricao
                    messagebox.showinfo("Inserir Descrição", f"Descrição para o livro '{titulo}' inserida com sucesso!")
            else:
                messagebox.showinfo("Inserir Descrição", "Livro não encontrado.")

    def remover_livro(self):
        if not self.livros:
            messagebox.showinfo("Remover Livro", "Nenhum livro cadastrado.")
            return

        titulo = simpledialog.askstring("Remover Livro", "Digite o título do livro:")
        if titulo:
            livro = next((livro for livro in self.livros if livro['titulo'] == titulo), None)
            if livro:
                self.livros.remove(livro)
                messagebox.showinfo("Remover Livro", f"Livro '{titulo}' removido com sucesso!")
            else:
                messagebox.showinfo("Remover Livro", "Livro não encontrado.")

    def ver_descricao(self, titulo):
        livro = next((livro for livro in self.livros if livro['titulo'] == titulo), None)
        if livro:
            if 'descricao' in livro:
                messagebox.showinfo(f"Descrição do Livro '{titulo}'", livro['descricao'])
            else:
                messagebox.showinfo(f"Descrição do Livro '{titulo}'", "Nenhuma descrição cadastrada.")
        else:
            messagebox.showinfo("Ver Descrição", "Livro não encontrado.")

if __name__ == "__main__":
    Application()