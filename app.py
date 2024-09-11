import streamlit as st
from datetime import datetime, time
from pydantic import ValidationError

import pandas as pd
import numpy as np

from contratodb import Vendas
from database import save_postgres

def main():
    st.title("Sistema de CRM e Vendas")
    email = st.text_input("Email", value="contato@leonardofernandes.com.br")
    data = st.date_input("Data da venda", datetime.now())
    hora = st.time_input("Hora da venda", value=time(9, 0)) #valor padrão 09:00
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    qtd = st.number_input("Quantidade de produtos", min_value=1, step=1, format="%d")
    produto = st.selectbox("Produto", ["ZapFlow com Gemini", "ZapFlow com ChatGPT", "ZapFlow com LIamma3.0"])
    
    
    if st.button("Salvar"):
        try:     
            data_hora = datetime.combine(data, hora)            
            venda = Vendas(
                email = email,
                data = data_hora, 
                valor = valor,
                qtd = qtd,
                produto = produto
            )                                                
            st.write(venda)
            save_postgres(venda)
            
        except ValidationError as e: 
            st.error(f"erro: {e}")
    

    

if __name__ == "__main__" :
    main()