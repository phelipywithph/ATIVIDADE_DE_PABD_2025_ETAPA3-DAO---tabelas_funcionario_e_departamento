from dataclasses import dataclass, asdict
from datetime import datetime, date
from typing import Optional

@dataclass
class Departamento:

    _nome_do_departamento: str
    _data_de_abertura: date
    _endereco: str = 'Macau-Rn'
    _cpf_supervisor: Optional[str] = None
    _numero_departamento: Optional[int] = None
    _created_at: Optional[datetime] = None
    _updated_at: Optional[datetime] = None

    # Departamento -> JSON (dict)
    def to_dict(self) -> dict:
        return asdict(self)

    # JSON (dict) -> Departamento
    @classmethod
    def from_dict(self, data: dict) -> 'Departamento':
        return Departamento(
            data.get('nome_do_departamento'),
            data.get('data_de_abertura'),
            data.get('endereco'),
            data.get('data_nasc'),
            data.get('cpf_supervisor'),
            data.get('numero_departamento'),
            data.get('created_at'),
            data.get('updated_at')
        )
    def __str__(self) -> str:
        return (
            f'Departamento(numero_departamento={self._numero_departamento}'
            f'data_de_abertura={self._data_de_abertura}, endereco={self._endereco},'
            f'numero_departamento={self._numero_departamento}, '
            f'created_at={self._created_at}, updated_at={self._updated_at})'
        )
    @property
    def endereco(self) -> str:
        return self._endereco

    @endereco.setter
    def endereco(self, endereco: str):
        self._endereco = endereco
        self._updated_at = datetime.now()

    @property
    def sexo(self) -> str:
        return self._sexo

    @sexo.setter
    def sexo(self, sexo: str):
        self._sexo = sexo
        self._updated_at = datetime.now()

    @property
    def cpf_supervisor(self) -> Optional[str]:
        return self._cpf_supervisor

    @cpf_supervisor.setter
    def cpf_supervisor(self, cpf_supervisor: Optional[str]):
        self._cpf_supervisor = cpf_supervisor
        self._updated_at = datetime.now()

    @property
    def numero_departamento(self) -> Optional[int]:
        return self._numero_departamento

    @numero_departamento.setter
    def numero_departamento(self, numero_departamento: Optional[int]):
        self._numero_departamento = numero_departamento
        self._updated_at = datetime.now()

    @property
    def created_at(self) -> Optional[datetime]:
        return self._created_at

    @property
    def updated_at(self) -> Optional[datetime]:
        return self._updated_at