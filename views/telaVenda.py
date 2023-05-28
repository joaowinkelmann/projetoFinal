import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from models.salvaArquivo import ProdutoAcesso

class VendaProdutoWindow(tk.Toplevel):
    def __init__(self, vender_produto_callback):
        super().__init__()
        self.title("Realizar Venda")
        self.vender_produto_callback = vender_produto_callback

        self.configure(background="#F0F0F0")

        self.produto_acesso = ProdutoAcesso()
        self.produtos = self.produto_acesso.carregar_produtos()

        # Labels
        tk.Label(self, text="Produto:", bg="#F0F0F0").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="Quantidade:", bg="#F0F0F0").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        # Product selection combobox
        self.produto_combobox = ttk.Combobox(self, values=[produto.nome for produto in self.produtos], state="readonly")
        self.produto_combobox.grid(row=0, column=1, padx=10, pady=5)
        self.produto_combobox.current(0)

        # Entry field for quantity
        self.quantidade_entry = tk.Entry(self)
        self.quantidade_entry.grid(row=1, column=1, padx=10, pady=5)

        # Button
        vender_button = tk.Button(self, text="Vender", command=self.realizar_venda, bg="#4CAF50", fg="white")
        vender_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        # Set focus on the quantity entry field
        self.quantidade_entry.focus()

        # Bind Enter key to the "Vender" button
        self.bind("<Return>", lambda event: vender_button.invoke())

    def realizar_venda(self):
        produto_nome = self.produto_combobox.get()
        quantidade = int(self.quantidade_entry.get())

        produto = next((p for p in self.produtos if p.nome == produto_nome), None)

        if produto:
            self.vender_produto_callback(produto.codigo, quantidade)
            self.destroy()
        else:
            messagebox.showerror("Erro", "Produto não encontrado!")
