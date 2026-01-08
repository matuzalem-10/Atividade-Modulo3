from conexao import Conexao

class ProdutoDAO:
    def inserir(self, nome, preco, id_categoria=None):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()
        sql = """INSERT INTO produto (nome, preco, id_categoria) 
                 VALUES (%s, %s, %s)"""
        try:
            cursor.execute(sql, (nome, preco, id_categoria))
            conexao.commit()
            print("Produto inserido com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao inserir produto: {err}")
        finally:
            cursor.close()
            conexao.close()

    def listar(self):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()
        sql = """SELECT p.id, p.nome, p.preco, c.nome AS categoria
                 FROM produto p
                 LEFT JOIN categoria c ON p.id_categoria = c.id
                 ORDER BY p.id"""
        try:
            cursor.execute(sql)
            produtos = cursor.fetchall()
            if not produtos:
                print("Nenhum produto cadastrado ainda.")
                return

            print("\n=====LISTA DE PRODUTOS=====")
            print(f"{'ID':<4} {'Nome':<30} {'Preço':<12} {'Categoria'}")
            print("-" * 70)
            for prod in produtos:
                categoria = prod[3] if prod[3] else "Sem categoria"
                print(f"{prod[0]:<4} {prod[1]:<30} R$ {prod[2]:<9.2f} {categoria}")
        except mysql.connector.Error as err:
            print(f"Erro ao listar produtos: {err}")
        finally:
            cursor.close()
            conexao.close()

    def buscar_por_id(self, id_produto):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()
        sql = """SELECT p.id, p.nome, p.preco, p.id_categoria, c.nome
                 FROM produto p
                 LEFT JOIN categoria c ON p.id_categoria = c.id
                 WHERE p.id = %s"""
        try:
            cursor.execute(sql, (id_produto,))
            produto = cursor.fetchone()
            return produto
        except mysql.connector.Error as err:
            print(f"Erro ao buscar produto: {err}")
            return None
        finally:
            cursor.close()
            conexao.close()

    def atualizar(self, id_produto, nome, preco, id_categoria=None):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()
        sql = """UPDATE produto 
                 SET nome = %s, preco = %s, id_categoria = %s 
                 WHERE id = %s"""
        try:
            cursor.execute(sql, (nome, preco, id_categoria, id_produto))
            if cursor.rowcount > 0:
                conexao.commit()
                print("Produto atualizado com sucesso!")
            else:
                print("Produto não encontrado.")
        except mysql.connector.Error as err:
            print(f"Erro ao atualizar produto: {err}")
        finally:
            cursor.close()
            conexao.close()

    def excluir(self, id_produto):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()
        sql = "DELETE FROM produto WHERE id = %s"
        try:
            cursor.execute(sql, (id_produto,))
            if cursor.rowcount > 0:
                conexao.commit()
                print("Produto excluído com sucesso!")
            else:
                print("Produto não encontrado.")
        except mysql.connector.Error as err:
            print(f"Erro ao excluir produto: {err}")
        finally:
            cursor.close()
            conexao.close()
