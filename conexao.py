import mysql.connector

class Conexao:
    @staticmethod
    def conectar():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="teste"
        )
