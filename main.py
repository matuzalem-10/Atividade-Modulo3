from produto import ProdutoDAO

class SistemaProduto:
    def __init__(self):
        self.dao = ProdutoDAO()

    def executar(self):
        while True:
            print("\n=====MENU PRINCIPAL=====")
            print("1 - Inserir Produto")
            print("2 - Listar produtos")
            print("3 - Buscar produto por ID")
            print("4 - Atualizar produto")
            print("5 - Excluir produto")
            print("0 - Sair")
            
            opcao = input("\nEscolha uma opção: ").strip()

            if opcao == "1":
                nome = input("Nome do Produto: ").strip()
                if not nome:
                    print("Nome obrigatório!")
                    continue
                try:
                    preco = float(input("Preço do Produto: "))
                    if preco < 0:
                        print("Preço não pode ser negativo.")
                        continue
                except ValueError:
                    print("Preço inválido.")
                    continue

                while True:
                    id_cat_input = input("ID da Categoria disponíveis:\n"
                                         "1 - Eletrônicos\n2 - Alimentos\n3 - Roupas\n"
                                         "4 - Livros\n5 - Informática\n6 - Brinquedos\n"
                                         "7 - Casa e Cozinha\n"
                                         "(deixe vazio para sem categoria): ").strip()
                    
                    if id_cat_input == "":
                        id_categoria = None
                        break
                    
                    try:
                        id_categoria = int(id_cat_input)
                        if 1 <= id_categoria <= 7:
                            break
                        else:
                            print("Erro: ID da categoria deve ser entre 1 e 7!\n")
                    except ValueError:
                        print("Erro: Digite um número válido ou deixe em branco.")
                
                self.dao.inserir(nome, preco, id_categoria)

            elif opcao == "2":
                self.dao.listar()

            elif opcao == "3":
                try:
                    id_prod = int(input("Digite o ID do produto: "))
                except ValueError:
                    print("ID inválido.")
                    continue
                produto = self.dao.buscar_por_id(id_prod)
                if produto:
                    cat = produto[4] if produto[4] else "Sem categoria"
                    print(f"\nProduto encontrado:")
                    print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R${produto[2]:.2f} | Categoria: {cat}")
                else:
                    print("Produto não encontrado.")

            elif opcao == "4":
                try:
                    id_prod = int(input("ID do produto que deseja atualizar: "))
                except ValueError:
                    print("ID inválido.")
                    continue
                produto = self.dao.buscar_por_id(id_prod)
                if not produto:
                    print("Produto não encontrado.")
                    continue

                print("\nDeixe em branco para manter o valor atual.")
                novo_nome = input(f"Nome ({produto[1]}): ").strip() or produto[1]
                preco_input = input(f"Preço (R${produto[2]:.2f}): ").strip()
                novo_preco = float(preco_input) if preco_input else produto[2]
                while True:
                    id_cat_input = input(f"ID Categoria (atual: {produto[3] or 'None'}): ").strip()
                    
                    if id_cat_input == "":
                        nova_categoria = produto[3]
                        break
                    
                    try:
                        temp_id = int(id_cat_input)
                        if 1 <= temp_id <= 7:
                            nova_categoria = temp_id
                            break
                        else:
                            print("Erro: ID da categoria deve ser entre 1 e 7!\n")
                    except ValueError:
                        print("Erro: Digite um número válido ou deixe em branco para manter o atual.")

                self.dao.atualizar(id_prod, novo_nome, novo_preco, nova_categoria)

            elif opcao == "5":
                try:
                    id_prod = int(input("ID do produto que deseja excluir: "))
                except ValueError:
                    print("ID inválido.")
                    continue
                confirm = input("Tem certeza que deseja excluir? (s/N): ").strip().lower()
                if confirm == "s":
                    self.dao.excluir(id_prod)

            elif opcao == "0":
                print("Saindo do sistema. Até logo!")
                break

            else:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    sistema = SistemaProduto()
    sistema.executar()
