import psycopg2
from psycopg2 import sql
from contratodb import Vendas
import streamlit as st
from dotenv import load_dotenv
import os

#carregar variaveis
load_dotenv()

#configuração do banco de dados PostgreSQL
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

#funcao para salva ros dados validados no PostgreSQL
def save_postgres(dados: Vendas):
    """
    Função para salvar no Postgres
    """
    
    
    try:
        conn = psycopg2.connect(
            host = DB_HOST,
            database = DB_NAME,
            user = DB_USER,
            password = DB_PASS
        )
        cursor = conn.cursor()
        
        #inserção dos dados na tabela de vendas
        insert_query = sql.SQL(
            """
            INSERT INTO vendas (email, data, valor, quantidade, produto)
            VALUES(%s, %s, %s, %s, %s )
            """
        )
        cursor.execute(insert_query, (
            dados.email,
            dados.data,
            dados.valor,
            dados.qtd,
            dados.produto.value
        ))
        conn.commit()
        cursor.close()
        st.success("Registro foi salvo com sucesso no banco de dados")
        
    except Exception as e: 
        st.error(f"Erro ao salvar no banco de dados: {e}")
        
        