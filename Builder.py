from __future__ import annotations


class Pessoa:
    #Representa uma pessoa com nome e identidade.

    def __init__(self, nome: str, identidade: str) -> None:
        self.nome = nome
        self.identidade = identidade

    def __repr__(self) -> str:
        return f"Pessoa(nome={self.nome!r}, identidade={self.identidade!r})"