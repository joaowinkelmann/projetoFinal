import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from models.gerenciadorProdutos import GerenciadorDeProdutos
from models.geradorTickets import SalesTicketGenerator

from views.telaCadastrar import CadastrarProdutoWindow
from views.telaVenda import VendaProdutoWindow
from views.telaRelatorio import RelatorioWindow
from views.telaProdutos import ProdutosWindow
from views.leitorQRCode import QRCodeReader


gerenciador = GerenciadorDeProdutos()

# Views INICIO
def open_cadastrar_window():
    cadastrar_window = CadastrarProdutoWindow()

def open_venda_window():
    venda_window = VendaProdutoWindow(vender_produto)

def open_mostrar_produtos_window():
    mostrar_produtos_window = ProdutosWindow(gerenciador)

def open_qrcode_reader_window():
    qrcode_reader = QRCodeReader(verify_and_add_sale)
    qrcode_reader.start_qr_code_reading()


# Views FIM

def generate_sales_tickets(codigo, quantidade):
    ticket_generator = SalesTicketGenerator()
    ticket_generator.generate_sales_tickets(codigo, quantidade)
    messagebox.showinfo("Sucesso", "Tickets de venda gerados com sucesso!")

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

def verify_and_add_sale(qrcode_data):
    # Extract the product ID and index from the QR code data
    product_id, index = qrcode_data.split("-")

    # Verify the product ID and index
    if gerenciador.verificar_produto_vendido(product_id, int(index)):
        # Add the sale using the GerenciadorDeProdutos class
        gerenciador.adicionar_venda(product_id, int(index))
        messagebox.showinfo("Sucesso", "Venda realizada com sucesso!")
    else:
        messagebox.showerror("Erro", "Código QR inválido!")


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

qrcode_reader_button = ttk.Button(button_frame, text="QR Code Reader", command=open_qrcode_reader_window)
qrcode_reader_button.grid(row=1, column=2, padx=10, pady=10)

root.mainloop()
