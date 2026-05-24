from __future__ import annotations


class Pessoa:
    #Representa uma pessoa com nome e identidade.

    def __init__(self, nome: str, identidade: str) -> None:
        self.nome = nome
        self.identidade = identidade

    def __repr__(self) -> str:
        return f"Pessoa(nome={self.nome!r}, identidade={self.identidade!r})"
    
class PessoaBuilder:
    #Builder para criar uma instância de Pessoa.

    def __init__(self) -> None:
        self._nome: str | None = None
        self._identidade: str | None = None

    def set_nome(self, nome: str) -> PessoaBuilder:
        self._nome = nome
        return self

    def set_identidade(self, identidade: str) -> PessoaBuilder:
        self._identidade = identidade
        return self

    def build(self) -> Pessoa:
        if self._nome is None:
            raise ValueError("Não é possível construir Pessoa: nome não foi lido do banco")
        if self._identidade is None:
            raise ValueError("Não é possível construir Pessoa: identidade não foi lida do banco")

        return Pessoa(nome=self._nome, identidade=self._identidade)