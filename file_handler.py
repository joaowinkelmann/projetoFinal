import json

class FileHandler:
    def salvar_produtos(self, gerenciador):
        data = []
        for item in gerenciador.produtos:
            data.append({
                'codigo': item.codigo,
                'nome': item.nome,
                'preco': item.preco,
                'quantidade': item.quantidade,
                'vendido': item.vendido
            })

        with open('produtos.json', 'w') as file:
            json.dump(data, file)

    def carregar_produtos(self):
        try:
            with open('produtos.json', 'r') as file:
                data = json.load(file)

            produtos = []
            for item in data:
                codigo = item['codigo']
                nome = item['nome']
                preco = item['preco']
                quantidade = item['quantidade']
                vendido = item['vendido']
                produto = Produto(codigo, nome, preco, quantidade, vendido)
                produtos.append(produto)

            return produtos
        except FileNotFoundError:
            return []
