import os

def exibir_nome_do_programa():
    print('''
    Lista 🛒 Compras Inteligente
    ''')

class ListaDeCompras:
    def __init__(self):
        self.itens = []  # Lista para armazenar itens
        self.categorias = {}  # Dicionário para categorizar itens
        self.orcamento = 0.0  # Orçamento inicial
        self.gastos = 0.0  # Gastos totais

    def definir_orcamento(self, valor):
        self.orcamento = valor
        print(f"Orçamento definido como: R$ {self.orcamento:.2f}")

    def adicionar_item(self, item, preco, categoria=None):
        self.itens.append({'nome': item, 'preco': preco, 'categoria': categoria})
        self.gastos += preco
        print(f"Item '{item}' adicionado à lista por R$ {preco:.2f}.")
        if categoria:
            if categoria not in self.categorias:
                self.categorias[categoria] = []
            self.categorias[categoria].append(item)

        # Verificar se ultrapassou o orçamento
        if self.gastos > self.orcamento:
            print("⚠️ Atenção: você ultrapassou o orçamento!")

    def remover_item(self, item):
        for i, obj in enumerate(self.itens):
            if obj['nome'] == item:
                self.gastos -= obj['preco']
                self.itens.pop(i)
                if obj['categoria']:
                    self.categorias[obj['categoria']].remove(item)
                print(f"Item '{item}' removido da lista.")
                return
        print(f"Item '{item}' não encontrado na lista.")

    def listar_itens(self):
        if self.itens:
            print('Itens na lista de compras: ')
            for obj in self.itens:
                categoria = obj['categoria'] if obj['categoria'] else 'Sem categoria'
                print(f"- {obj['nome']} (R$ {obj['preco']:.2f}) - Categoria: {categoria}")
        else:
            print('A lista de compras está vazia.')

    def listar_por_categoria(self):
        if self.categorias:
            print("Itens organizados por categoria:")
            for categoria, itens in self.categorias.items():
                print(f"{categoria}: {', '.join(itens)}")
        else:
            print("Nenhuma categoria definida.")

    def exibir_resumo(self):
        print("\nResumo da lista:")
        print(f"Orçamento: R$ {self.orcamento:.2f}")
        print(f"Gastos: R$ {self.gastos:.2f}")
        print(f"Saldo restante: R$ {self.orcamento - self.gastos:.2f}")
        print("Itens na lista: ")
        self.listar_itens()


def main():
    exibir_nome_do_programa()
    lista = ListaDeCompras()

    while True:
        print("\nMenu:")
        print("1. Definir orçamento")
        print("2. Adicionar item")
        print("3. Remover item")
        print("4. Listar itens")
        print("5. Listar itens por categoria")
        print("6. Exibir resumo")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            try:
                valor = float(input("Digite o valor do orçamento: R$ "))
                lista.definir_orcamento(valor)
            except ValueError:
                print("⚠️ Por favor, insira um número válido.")

        elif escolha == "2":
            item = input("Digite o nome do item: ")
            try:
                preco = float(input(f"Digite o preço de '{item}': R$ "))
                categoria = input("Digite a categoria do item (ou deixe em branco): ")
                categoria = categoria if categoria.strip() else None
                lista.adicionar_item(item, preco, categoria)
            except ValueError:
                print("⚠️ Por favor, insira um preço válido.")

        elif escolha == "3":
            item = input("Digite o nome do item a ser removido: ")
            lista.remover_item(item)

        elif escolha == "4":
            lista.listar_itens()

        elif escolha == "5":
            lista.listar_por_categoria()

        elif escolha == "6":
            lista.exibir_resumo()

        elif escolha == "7":
            print("Saindo da aplicação. Até mais!")
            break

        else:
            print("⚠️ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
