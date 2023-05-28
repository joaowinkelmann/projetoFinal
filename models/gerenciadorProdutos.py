import hashlib
import time
import tkinter as tk
from tkinter import messagebox
from models.produto import Produto
from models.salvaArquivo import ProdutoAcesso, VendaLog

class GerenciadorDeProdutos:
    def __init__(self):
        self.produtos = []
        self.produto_acesso = ProdutoAcesso()
        self.produtos = self.produto_acesso.carregar_produtos()

    def adicionar_produto(self, nome, preco_venda, preco_custo, estoque, vendido):
            codigo = self.generate_codigo(nome)
            produto = self.buscar_produto(codigo)
            if produto:
                return False
            else:
                novo_produto = Produto(codigo, nome, preco_venda, preco_custo, estoque, vendido)
                self.produtos.append(novo_produto)
                self.produto_acesso.salvar_produtos(self)
                return True
        
    def generate_codigo(self, nome):
        string_to_hash = f"{nome}{time.time()}"
        codigo = hashlib.sha1(string_to_hash.encode()).hexdigest()
        return codigo


    def buscar_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def vender_produto(self, codigo, quantidade):
        produto = self.buscar_produto(codigo)
        if produto:
            if (produto.estoque - produto.vendido) >= quantidade:
                produto.vendido += quantidade
                venda_log = VendaLog(codigo, quantidade)  # Realiza o log da venda
                venda_log.salvar_venda()
                return True
        return False


    def mostrar_todos_os_produtos(self):
        if not self.produtos:
            messagebox.showinfo("Todos os Produtos", "Nenhum produto cadastrado.")
        else:
            produtos_info = ""
            for produto in self.produtos:
                produtos_info += f"Nome: {produto.nome}, Preço: {produto.preco}, Estoque: {produto.estoque}, Código: {produto.codigo}, Vendido: {produto.vendido}\n"

            messagebox.showinfo("Todos os Produtos", produtos_info)

    def mostrar_produtos_em_estoque(self):
        produtos_info = ""
        produtos_em_estoque = [produto for produto in self.produtos if produto.vendido < produto.estoque]
        if produtos_em_estoque:
            for produto in produtos_em_estoque:
                produtos_info += f"Nome: {produto.nome}, Preço: {produto.preco}, Estoque: {produto.estoque}, Código: {produto.codigo}, Vendido: {produto.vendido}\n"
        else:
            produtos_info = "Nenhum produto em estoque."

        messagebox.showinfo("Produtos em Estoque", produtos_info)

    def alterar_estoque_do_produto(self, codigo, estoque):
        produto = self.buscar_produto(codigo)
        if produto:
            produto.estoque = estoque
            self.produto_acesso.salvar_produtos(self)
            return True
        return False
