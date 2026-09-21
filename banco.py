import os 

import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def conectar():
    conexao = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return conexao


def salvar_consulta(cep, lograduro, bairro, cidade, uf):
    conexao = conectar()

    cursor = conexao.cursor()

    sql = """
    INSERT INTO consultas_cep
    (cep, logradouro, bairro, cidade, uf)
    VALUES (%s, %s, %s, %s, %s)
    """

    valores = (cep, lograduro, bairro, cidade, uf)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()