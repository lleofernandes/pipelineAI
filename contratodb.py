from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "ZapFlow com Gemini"
    produto2 = "ZapFlow com ChatGPT"
    produto3 = "ZapFlow com LIamma3.0"

class Model(BaseModel):
    email: EmailStr #valida o email


class Vendas(BaseModel):
    """
    Modelo ed dados para as vendas
    
    Args:
        email (EmailStr): email do comprador
        data (datetime): data da compra
        valor (PositiveFloat): Valor da compra
        qtd (PositiveInt): qtd de produtos
        produto (ProdutoEnum): categoria do produto
    """
    
    
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    qtd: PositiveInt
    produto: ProdutoEnum
    

    
    