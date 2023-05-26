import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from gerenciador import GerenciadorDeProdutos
from file_handler import FileHandler

gerenciador = GerenciadorDeProdutos()

class Produto:
    def __init__(self, codigo, nome, preco, quantidade, vendido):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.vendido = vendido
        self.proximo = None

class GerenciadorDeProdutos:
    # Remaining code from gerenciador.py

    file_handler = FileHandler()

def adicionar_produto():
    nome = nome_entry.get()
    preco = float(preco_entry.get())
    quantidade = int(quantidade_entry.get())
    codigo = int(codigo_entry.get())
    vendido = int(vendido_entry.get())
    if gerenciador.adicionar_produto(codigo, nome, preco, quantidade, vendido):
        messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
    else:
        messagebox.showerror("Erro", "Produto com código ou nome já existente.")

def buscar_produto():
    codigo = int(codigo_entry.get())
    produto = gerenciador.buscar_produto(codigo)
    if produto:
        messagebox.showinfo("Produto Encontrado", f"Nome: {produto.nome}\nPreço: {produto.preco}\nQuantidade: {produto.quantidade}")
    else:
        messagebox.showerror("Produto Não Encontrado", "Produto não encontrado!")

def vender_produto():
    codigo = int(codigo_entry.get())
    quantidade = int(quantidade_entry.get())
    if gerenciador.vender_produto(codigo, quantidade):
        messagebox.showinfo("Sucesso", "Venda realizada com sucesso!")
    else:
        messagebox.showerror("Erro", "Não foi possível realizar a venda. Verifique se o produto está cadastrado ou se há quantidade suficiente em estoque.")

def mostrar_todos_os_produtos():
    produtos = gerenciador.mostrar_todos_os_produtos()
    if produtos:
        messagebox.showinfo("Todos os Produtos", "\n".join([f"Nome: {produto.nome}, Preço: {produto.preco}, Quantidade: {produto.quantidade}" for produto in produtos]))
    else:
        messagebox.showinfo("Todos os Produtos", "Nenhum produto cadastrado.")

def mostrar_produtos_em_estoque():
    produtos_em_estoque = gerenciador.mostrar_produtos_em_estoque()
    if produtos_em_estoque:
        messagebox.showinfo("Produtos em Estoque", "\n".join([f"Nome: {produto.nome}, Preço: {produto.preco}, Quantidade: {produto.quantidade}" for produto in produtos_em_estoque]))
    else:
        messagebox.showinfo("Produtos em Estoque", "Nenhum produto em estoque.")

def alterar_estoque_do_produto():
    codigo = int(codigo_entry.get())
    quantidade = int(quantidade_entry.get())
    if gerenciador.alterar_estoque_do_produto(codigo, quantidade):
        messagebox.showinfo("Sucesso", "Estoque alterado com sucesso!")
    else:
        messagebox.showerror("Erro", "Produto não encontrado!")

def exportar_para_excel():
    gerenciador.exportar_para_excel()
    messagebox.showinfo("Sucesso", "Produtos exportados com sucesso!")

root = tk.Tk()
root.title("Sistema de Controle de Estoque")

# Labels
tk.Label(root, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
tk.Label(root, text="Preço:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
tk.Label(root, text="Quantidade:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
tk.Label(root, text="Código:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
tk.Label(root, text="Vendido:").grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

# Entry Fields
nome_entry = tk.Entry(root)
nome_entry.grid(row=0, column=1, padx=10, pady=5)
preco_entry = tk.Entry(root)
preco_entry.grid(row=1, column=1, padx=10, pady=5)
quantidade_entry = tk.Entry(root)
quantidade_entry.grid(row=2, column=1, padx=10, pady=5)
codigo_entry = tk.Entry(root)
codigo_entry.grid(row=3, column=1, padx=10, pady=5)
vendido_entry = tk.Entry(root)
vendido_entry.grid(row=4, column=1, padx=10, pady=5)

# Buttons
adicionar_produto_button = tk.Button(root, text="Adicionar Produto", command=adicionar_produto)
adicionar_produto_button.grid(row=5, column=0, padx=10, pady=5)
buscar_produto_button = tk.Button(root, text="Buscar Produto", command=buscar_produto)
buscar_produto_button.grid(row=5, column=1, padx=10, pady=5)
vender_produto_button = tk.Button(root, text="Vender Produto", command=vender_produto)
vender_produto_button.grid(row=5, column=2, padx=10, pady=5)
mostrar_todos_os_produtos_button = tk.Button(root, text="Mostrar Todos os Produtos", command=mostrar_todos_os_produtos)
mostrar_todos_os_produtos_button.grid(row=6, column=0, padx=10, pady=5)
mostrar_produtos_em_estoque_button = tk.Button(root, text="Mostrar Produtos em Estoque", command=mostrar_produtos_em_estoque)
mostrar_produtos_em_estoque_button.grid(row=6, column=1, padx=10, pady=5)
alterar_estoque_do_produto_button = tk.Button(root, text="Alterar Estoque do Produto", command=alterar_estoque_do_produto)
alterar_estoque_do_produto_button.grid(row=6, column=2, padx=10, pady=5)
exportar_para_excel_button = tk.Button(root, text="Exportar para Excel", command=exportar_para_excel)
exportar_para_excel_button.grid(row=7, column=1, padx=10, pady=5)

root.mainloop()
