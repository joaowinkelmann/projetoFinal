import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from datetime import datetime
from collections import defaultdict
from models.salvaArquivo import ProdutoAcesso, VendaLog

def RelatorioWindow():
    vendas_data = VendaLog.carregar_vendas()
    produtos = ProdutoAcesso().carregar_produtos()

    sales_per_hour_per_product = defaultdict(lambda: defaultdict(int))
    product_ids = set()
    for venda in vendas_data:
        venda_dict = venda[0]
        timestamp = datetime.fromisoformat(venda_dict['timestamp'])
        hour = timestamp.hour
        product_id = venda_dict['codigo']
        product_ids.add(product_id)
        sales_per_hour_per_product[product_id][hour] += venda_dict['quantidade']


    product_names = {}
    for produto in produtos:
        product_id = produto.codigo
        product_names[product_id] = produto.nome

    products = list(product_ids)
    hours = list(range(24))
    sales_data = []
    for product_id in products:
        sales = [sales_per_hour_per_product[product_id][hour] for hour in hours]
        sales_data.append(sales)

    product_labels = [product_names[product_id] for product_id in products]

    root = tk.Tk()
    root.title("Sales Report")

    fig, ax = plt.subplots()

    for product_label, sales in zip(product_labels, sales_data):
        ax.plot(hours, sales, marker='o', linestyle='-', label=product_label)

    ax.set_xlabel("Hora")
    ax.set_ylabel("Vendas")
    ax.set_title("Vendas por Hora")
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    tk.mainloop()
