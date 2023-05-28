import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from models.gerenciadorProdutos import GerenciadorDeProdutos

class CadastrarProdutoWindow:
    def __init__(self):
        self.gerenciador = GerenciadorDeProdutos()

        self.window = tk.Toplevel()
        self.window.title("Cadastrar Produto")

        # Labels
        tk.Label(self.window, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        tk.Label(self.window, text="Preço de Venda:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        tk.Label(self.window, text="Preço de Custo:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        tk.Label(self.window, text="Estoque:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        tk.Label(self.window, text="Vendido:").grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

        # Entry fields
        self.nome_entry = tk.Entry(self.window)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=5)
        self.preco_venda_entry = tk.Entry(self.window)
        self.preco_venda_entry.grid(row=1, column=1, padx=10, pady=5)
        self.preco_custo_entry = tk.Entry(self.window)
        self.preco_custo_entry.grid(row=2, column=1, padx=10, pady=5)
        self.estoque_entry = tk.Entry(self.window)
        self.estoque_entry.grid(row=3, column=1, padx=10, pady=5)
        self.vendido_entry = tk.Entry(self.window)
        self.vendido_entry.grid(row=4, column=1, padx=10, pady=5)

        # Button
        cadastrar_button = ttk.Button(self.window, text="Cadastrar", command=self.adicionar_produto)
        cadastrar_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    def adicionar_produto(self):
        nome = self.nome_entry.get()
        preco_venda = self.preco_venda_entry.get()
        preco_custo = self.preco_custo_entry.get()
        estoque = self.estoque_entry.get()
        vendido = self.vendido_entry.get()

        if not nome or not preco_venda or not preco_custo or not estoque or not vendido:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        try:
            preco_venda = float(preco_venda)
            preco_custo = float(preco_custo)
            estoque = int(estoque)
            vendido = int(vendido)
        except ValueError:
            messagebox.showerror("Erro", "Valores inválidos. Certifique-se de digitar números nos campos corretos.")
            return

        result = self.gerenciador.adicionar_produto(nome, preco_venda, preco_custo, estoque, vendido)
        if result:
            messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
        else:
            messagebox.showerror("Erro", "O produto já existe!")

        self.window.destroy()
