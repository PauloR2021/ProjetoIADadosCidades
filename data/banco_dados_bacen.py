""""
Desenvolvedor: Paulo Ricardo Soares
Data: 05/06/2025
Hora: 18:51

Criando conexão com o banco de dados
"""
import pyodbc
import os
from dotenv import load_dotenv


load_dotenv()

DB_SERVER = os.getenv("DB_SERVER")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def conectar_sql():

    try:
        driver = os.getenv("DRIVER")  # Nome do driver ODBC
        server = os.getenv("SERVER") # Nome ou IP do servidor SQL Server
        database = os.getenv("DATABASE")  # Nome do banco de dados
        username = os.getenv("USERNAME")  # Usuário SQL
        password = os.getenv("PASSWORD")  # Senha SQL
        
        conexao_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
        conexao = pyodbc.connect(conexao_string)
        print("✅ Conectado com sucesso ao SQL Server!")
        return conexao
    
    except Exception as e:
        print(f"Erro: {e}")

