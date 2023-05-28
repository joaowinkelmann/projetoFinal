import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from models.gerenciadorProdutos import GerenciadorDeProdutos

from views.telaCadastrar import CadastrarProdutoWindow
from views.telaVenda import VendaProdutoWindow
from views.telaRelatorio import RelatorioWindow
from views.telaProdutos import ProdutosWindow

gerenciador = GerenciadorDeProdutos()

# Views INICIO
def open_cadastrar_window():
    cadastrar_window = CadastrarProdutoWindow()

def open_venda_window():
    venda_window = VendaProdutoWindow(vender_produto)

def open_mostrar_produtos_window():
    mostrar_produtos_window = ProdutosWindow(gerenciador)
# Views FIM


def adicionar_produto(nome, preco_venda, preco_custo, estoque, vendido):
    result = gerenciador.adicionar_produto(nome, preco_venda, preco_custo, estoque, vendido)
    if result:
        messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
    else:
        messagebox.showerror("Erro", "O produto já existe!")

def vender_produto(codigo, quantidade):
    if gerenciador.vender_produto(codigo, quantidade):
        messagebox.showinfo("Sucesso", "Venda realizada com sucesso!")
    else:
        messagebox.showerror("Erro", "Não foi possível realizar a venda. Verifique se o produto está cadastrado ou se há quantidade suficiente em estoque.")

root = tk.Tk()
root.title("Sistema de Controle de Estoque")

# Style
style = ttk.Style()
style.configure("TButton",
                font=("Helvetica", 16),
                padding=10,
                width=20)

# Labels
titulo_label = ttk.Label(root, text="Sistema de Controle de Estoque", font=("Helvetica", 18, "bold"))
titulo_label.pack(pady=20)

info_label = ttk.Label(root, text="Selecione uma opção:", font=("Helvetica", 16))
info_label.pack(pady=10)

# Buttons
button_frame = ttk.Frame(root)
button_frame.pack()

cadastrar_button = ttk.Button(button_frame, text="Cadastrar", command=open_cadastrar_window)
cadastrar_button.grid(row=0, column=0, padx=10, pady=10)

vender_produto_button = ttk.Button(button_frame, text="Vender Produto", command=open_venda_window)
vender_produto_button.grid(row=0, column=1, padx=10, pady=10)

mostrar_produtos_button = ttk.Button(button_frame, text="Mostrar Produtos", command=open_mostrar_produtos_window)
mostrar_produtos_button.grid(row=1, column=0, padx=10, pady=10)

sales_report_button = ttk.Button(button_frame, text="Gerar Relatório de Vendas", command=RelatorioWindow)
sales_report_button.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
