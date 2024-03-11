from datetime import date, datetime
from typing import Optional, List
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import db


class Bolsista(db.Model):
    __tablename__ = "bolsista"

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
    bolsas: Mapped[List["RelacaoBolsaBolsista"]] = relationship(back_populates="bolsista")
    data_deletado: Mapped[Optional[datetime]]

    @property
    def bolsa_ativa(self) -> bool:
        for bolsa in self.bolsas:
            if bolsa.ativa:
                return True

        return False

    @property
    def bolsa_atual(self):
        for bolsa in self.bolsas:
            if bolsa.ativa:
                return bolsa.bolsa


class RelacaoBolsaBolsista(db.Model):
    __tablename__ = "rl_bolsa_bolsista"

    id: Mapped[int] = mapped_column(primary_key=True)
    bolsista_id: Mapped[int] = mapped_column(ForeignKey("bolsista.id"))
    bolsa_id: Mapped[int] = mapped_column(ForeignKey("bolsa.id"))
    ativa: Mapped[bool] = mapped_column(default=True)
    bolsista: Mapped["Bolsista"] = relationship(back_populates="bolsas")
    bolsa: Mapped["Bolsa"] = relationship(back_populates="bolsistas")


class Bolsa(db.Model):
    __tablename__ = "bolsa"

    id: Mapped[int] = mapped_column(primary_key=True)
    modalidade: Mapped[str]
    carga_horaria: Mapped[int]
    cargo: Mapped[str]
    valor: Mapped[float]
    edital_id: Mapped[int] = mapped_column(ForeignKey("edital.id"))
    bolsistas: Mapped["RelacaoBolsaBolsista"] = relationship(back_populates="bolsa")
    edital: Mapped["Edital"] = relationship(back_populates="bolsas")
    data_deletado: Mapped[Optional[datetime]]
    


class Edital(db.Model):
    __tablename__ = "edital"

    id: Mapped[int] = mapped_column(primary_key=True)
    numero: Mapped[str]
    data_assinatura: Mapped[date]
    duracao: Mapped[str]
    nucleo_responsavel: Mapped[str]
    bolsas: Mapped[List["Bolsa"]] = relationship(back_populates="edital")
    data_deletado: Mapped[Optional[datetime]]
