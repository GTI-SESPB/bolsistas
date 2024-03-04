from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from ..main.server import db


class Bolsistas(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    cpf: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    nome: Mapped[str]
    nome_mae: Mapped[str]
    pis_pasep: Mapped[str]
    rg: Mapped[str]
    nascimento: Mapped[datetime]
    dados_bancarios: Mapped[str]
    # endereco
    cep: Mapped[str]
    cidade: Mapped[str]
    logradouro: Mapped[str]
    numero: Mapped[str]
    complemento: Mapped[str]

