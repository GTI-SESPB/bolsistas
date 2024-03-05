from datetime import date
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from ..main.server import app


class Bolsistas(app.db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    cpf: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    nome: Mapped[str]
    nome_mae: Mapped[str]
    pis_pasep: Mapped[str]
    rg: Mapped[str]
    nascimento: Mapped[date]
    dados_bancarios: Mapped[str]
    # endereco
    cep: Mapped[str]
    cidade: Mapped[str]
    logradouro: Mapped[str]
    numero: Mapped[str]
    complemento: Mapped[Optional[str]]
    #bolsa
    modalidade: Mapped[str]
    carga_horaria: Mapped[int]
    cargo: Mapped[str]
    valor: Mapped[float]

