import tkinter as tk
from tkinter import messagebox
import sqlite3


#tarefa e: fazer uma segunda tela e nessa tela guardar suas anotaçoes por enquanto so isso!
#cd c:\Users\mathe\Documents\projeto_simples
# sempre passar, cd c:\Users\mathe\Documents\projeto_simples


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Login")
        
        # Configuração do tamanho da janela
        self.root.geometry("500x400")  # Janela maior (500x400 pixels)
        self.root.minsize(450, 350)    # Tamanho mínimo
        
        # Centralizar a janela
        self.centralizar_janela()
        
        # Conexão com o banco SQLite
        self.conn = sqlite3.connect('projeto_simples/usuarios.db')

        self.criar_tabela()
        
        # Frame principal para organização
        frame_principal = tk.Frame(root, padx=20, pady=20)
        frame_principal.pack(expand=True)
        
        # Elementos da interface
        tk.Label(frame_principal, text="Usuário:", font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.entry_usuario = tk.Entry(frame_principal, font=('Arial', 12), width=25)
        self.entry_usuario.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(frame_principal, text="Senha:", font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10, sticky='e')
        self.entry_senha = tk.Entry(frame_principal, show="*", font=('Arial', 12), width=25)
        self.entry_senha.grid(row=1, column=1, padx=10, pady=10)
        
        # Frame para os botões
        frame_botoes = tk.Frame(frame_principal)
        frame_botoes.grid(row=2, column=0, columnspan=2, pady=20)
        
        tk.Button(frame_botoes, text="Login", command=self.verificar_login, 
                 font=('Arial', 12), width=10, bg='#4CAF50', fg='white').pack(side='left', padx=10)
        tk.Button(frame_botoes, text="Cadastrar", command=self.cadastrar_usuario,
                 font=('Arial', 12), width=10, bg='#2196F3', fg='white').pack(side='left', padx=10)
    
    def centralizar_janela(self):
        """Centraliza a janela na tela"""
        self.root.update_idletasks()
        largura = self.root.winfo_width()
        altura = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.root.winfo_screenheight() // 2) - (altura // 2)
        self.root.geometry(f'+{x}+{y}')
    
    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL
            )
        ''')
        self.conn.commit()
    
    def verificar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
        resultado = cursor.fetchone()
        
        if resultado:
            messagebox.showinfo("Sucesso", f"Bem-vindo, {usuario}!")
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")
    
    def cadastrar_usuario(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        
        if not usuario or not senha:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha))
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Erro", "Usuário já existe!")
    
    def __del__(self):
        self.conn.close()

# Criar e rodar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()


