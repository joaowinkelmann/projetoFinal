class Produto:
    def __init__(self, codigo, nome, preco, quantidade, vendido):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.vendido = vendido
        self.proximo = None


class GerenciadorDeProdutos:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, codigo, nome, preco, quantidade, vendido):
        produto = self.buscar_produto(codigo)
        if produto:
            return False
        else:
            novo_produto = Produto(codigo, nome, preco, quantidade, vendido)
            self.produtos.append(novo_produto)
            return True

    def buscar_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def vender_produto(self, codigo, quantidade):
        produto = self.buscar_produto(codigo)
        if produto:
            if produto.quantidade >= quantidade:
                produto.quantidade -= quantidade
                produto.vendido += quantidade
                return True
        return False

    def mostrar_todos_os_produtos(self):
        for produto in self.produtos:
            print(f"Nome: {produto.nome}, Preço: {produto.preco}, Quantidade: {produto.quantidade}, Código: {produto.codigo}, Vendido: {produto.vendido}")

    def mostrar_produtos_em_estoque(self):
        for produto in self.produtos:
            if produto.quantidade > 0:
                print(f"Nome: {produto.nome}, Preço: {produto.preco}, Quantidade: {produto.quantidade}, Código: {produto.codigo}, Vendido: {produto.vendido}")

    def alterar_estoque_do_produto(self, codigo, quantidade):
        produto = self.buscar_produto(codigo)
        if produto:
            produto.quantidade = quantidade
            return True
        return False
