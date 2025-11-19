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