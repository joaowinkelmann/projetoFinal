import datetime
import json
from models.produto import Produto
import os
from models.dbConn import connect

class ProdutoAcesso:
    def __init__(self):
        self.data_folder = "data"

        # Cria a pasta se ela não existe
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)

    def salvar_produto(self, produto):
        data = {
            'codigo': produto.codigo,
            'nome': produto.nome,
            'preco_venda': produto.preco_venda,
            'preco_custo': produto.preco_custo,
            'estoque': produto.estoque,
            'vendido': produto.vendido
        }

        file_path = os.path.join(self.data_folder, 'produtos.json')
        with open(file_path, 'r') as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = []

        existing_products = [item for item in existing_data if item['codigo'] != produto.codigo]
        existing_products.append(data)

        with open(file_path, 'w') as file:
            json.dump(existing_products, file)


    def salvar_produtos(self, gerenciador):
        data = []
        for item in gerenciador.produtos:
            data.append({
                'codigo': item.codigo,
                'nome': item.nome,
                'preco_venda': item.preco_venda,
                'preco_custo': item.preco_custo,
                'estoque': item.estoque,
                'vendido': item.vendido
            })

        file_path = os.path.join(self.data_folder, 'produtos.json')
        with open(file_path, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def carregar_produtos():
        file_path = os.path.join('data', 'produtos.json')

        try:
            with open(file_path, 'r') as file:
                try:
                    data = json.load(file)

                    if not data:
                        return []

                    produtos = []
                    for item in data:
                        codigo = item['codigo']
                        nome = item['nome']
                        preco_venda = item['preco_venda']
                        preco_custo = item['preco_custo']
                        estoque = item['estoque']
                        vendido = item['vendido']
                        produto = Produto(codigo, nome, preco_venda, preco_custo, estoque, vendido)
                        produtos.append(produto)

                    return produtos
                except json.JSONDecodeError:
                    return []
        except FileNotFoundError:
            return []

class VendaLog:
    def __init__(self, codigo, quantidade):
        self.codigo = codigo
        self.quantidade = quantidade
        self.timestamp = datetime.datetime.now().isoformat()
        self.file_path = os.path.join("data", "vendas.json")

    def salvar_venda(self):
        data = []
        data.append({
            'codigo': self.codigo,
            'quantidade': self.quantidade,
            'timestamp': self.timestamp
        })
        with open(self.file_path, 'a') as file:
            json.dump(data, file)
            file.write('\n')

    @staticmethod
    def carregar_vendas():
        vendas_data = []
        file_path = os.path.join("data", "vendas.json")
        with open(file_path, 'r') as file:
            for line in file:
                venda = json.loads(line)
                vendas_data.append(venda)
        return vendas_data

class QRLog:
    def salvar_qr_code(qr_code_data):
        file_path = os.path.join("data", "qrcode.json")
        
        # Load existing JSON data
        existing_data = []
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                existing_data = [json.loads(line) for line in file]
        
        # Check if qr_code_data is already present and update the flag
        for item in existing_data:
            if item[0] == qr_code_data:
                print("achou")
                item[1] = True
                break
        
        # Write the updated data back to the JSON file
        with open(file_path, 'w') as file:
            for item in existing_data:
                json.dump(item, file)
                file.write('\n')

    @staticmethod
    def carregar_qr_codes():
        # Load QR codes from the file
        file_path = os.path.join("data", "qrcode.json")
        qrcodes = []

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                qrcodes = [json.loads(line) for line in file]

        return qrcodes