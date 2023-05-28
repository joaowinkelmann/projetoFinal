import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from models.salvaArquivo import ProdutoAcesso

class ProdutosWindow(tk.Toplevel):
    def __init__(self, gerenciador):
        super().__init__()

        self.gerenciador = gerenciador

        self.title("Mostrar Produtos")
        self.geometry("500x450")

        self.search_label = tk.Label(self, text="Buscar Produto:")
        self.search_label.pack(pady=10)

        self.search_entry = tk.Entry(self)
        self.search_entry.pack(pady=5)

        self.products_listbox = tk.Listbox(self, width=40)
        self.products_listbox.pack(pady=10)

        self.details_frame = tk.Frame(self)
        self.details_frame.pack(pady=10)

        self.preco_label = tk.Label(self.details_frame, text="Preço:")
        self.preco_label.grid(row=0, column=0, sticky="w")

        self.vendido_label = tk.Label(self.details_frame, text="Vendidos:")
        self.vendido_label.grid(row=1, column=0, sticky="w")

        self.estoque_label = tk.Label(self.details_frame, text="Estoque:")
        self.estoque_label.grid(row=2, column=0, sticky="w")

        self.remaining_label = tk.Label(self.details_frame, text="Restante para Venda:")
        self.remaining_label.grid(row=3, column=0, sticky="w")

        self.profit_margin_label = tk.Label(self.details_frame, text="Margem de Lucro:")
        self.profit_margin_label.grid(row=4, column=0, sticky="w")

        self.preco_value = tk.Label(self.details_frame, width=20)
        self.preco_value.grid(row=0, column=1, sticky="w")

        self.vendido_value = tk.Label(self.details_frame, width=20)
        self.vendido_value.grid(row=1, column=1, sticky="w")

        self.estoque_value = tk.Label(self.details_frame, width=20)
        self.estoque_value.grid(row=2, column=1, sticky="w")

        self.remaining_value = tk.Label(self.details_frame, width=20)
        self.remaining_value.grid(row=3, column=1, sticky="w")

        self.profit_margin_value = tk.Label(self.details_frame, width=20)
        self.profit_margin_value.grid(row=4, column=1, sticky="w")

        self.alterar_estoque_button = tk.Button(self, text="Alterar Estoque", command=self.alterar_estoque)
        self.alterar_estoque_button.pack(pady=10)

        self.search_entry.bind("<KeyRelease>", self.search_product)
        self.products_listbox.bind("<<ListboxSelect>>", self.show_product_details)

        self.populate_product_list()

    def populate_product_list(self):
        self.products_listbox.delete(0, tk.END)
        products = self.gerenciador.produtos
        for produto in products:
            self.products_listbox.insert(tk.END, produto.nome)

    def search_product(self, event):
        search_term = self.search_entry.get().lower()
        self.products_listbox.delete(0, tk.END)
        products = self.gerenciador.produtos
        for produto in products:
            if search_term in produto.nome.lower():
                self.products_listbox.insert(tk.END, produto.nome)

    def show_product_details(self, event):
        selected_index = self.products_listbox.curselection()
        if not selected_index:
            return

        selected_product = self.gerenciador.produtos[selected_index[0]]
        self.preco_value.config(text=selected_product.preco_venda)
        self.vendido_value.config(text=selected_product.vendido)
        self.estoque_value.config(text=selected_product.estoque)

        remaining = selected_product.estoque - selected_product.vendido
        self.remaining_value.config(text=remaining)

        profit_margin = (selected_product.preco_venda - selected_product.preco_custo) / selected_product.preco_venda * 100
        self.profit_margin_value.config(text=f"{profit_margin:.2f}%")

    def alterar_estoque(self):
        selected_index = self.products_listbox.curselection()
        if not selected_index:
            return

        selected_product = self.gerenciador.produtos[selected_index[0]]
        new_stock = simpledialog.askinteger("Alterar Estoque", f"Digite o novo estoque para {selected_product.nome}:")

        if new_stock is not None:
            selected_product.estoque = new_stock
            self.estoque_value.config(text=selected_product.estoque)
            produto_acesso = ProdutoAcesso()
            produto_acesso.salvar_produto(selected_product)
            messagebox.showinfo("Sucesso", "Estoque alterado com sucesso!")
        else:
            messagebox.showinfo("Aviso", "Nenhum valor de estoque fornecido.")
