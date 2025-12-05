'''
  *** BaseDAO ***
  Classe abstrata base para DAOs (Data Access Objects)
  Operações CRUD genéricas
'''

from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic
from supabase import Client

# TypeVar - tornar a classe genérica
T = TypeVar('T')

class BaseDAO(ABC, Generic[T]):

  def __init__(self, client: Client, table_name: str):
    self._client = client
    self._table_name = table_name


  # Do formato JSON (dict) para modelo de dados (T)
  @abstractmethod
  def to_model(self, data: dict) -> T:
    pass #os filhos devem decidir como será feito a implementação

  # Do modelo de dados (T) para formato JSON (dict)
  @abstractmethod
  def to_dict(self, model: T) -> dict:
    pass #os filhos devem decidir como será feito a implementação

  ### Create - função para criar algo na tabela:
  def create(self, model: T) -> Optional[T]: #recebe um modelo genérico T
        #Tratamento de erros
        try:
            data = self.to_dict(model) #conversão para dicionario
            response = self.client.table(self.table_name).insert(data).execute() #comando para SUPABASE
            if response.data: 
                return self.to_model(response.data[0]) #Retornando do formato JSON (dict) para modelo de dados (T)
            return None #retorna
        #Caso de errado
        except Exception as e:
            print(f"Erro ao criar registro: {e}") #mensagem de erro
            return None #retorna nada
    
  ### Read
  def read_id(self, pk: str, value: T) -> Optional[T]:
    try:
      response = self._client.table(self._table_name).select('*').eq(pk,value).execute()
      if response.data and len(response.data) > 0:
        return self.to_model(response.data[0])
      return None 
    except Exception as e:
      print(f'Erro ao buscar todos os registros: {e}')
      return None
  
  # Retorna todos os valores de uma tabela
  def read_all(self) -> List[T]:
    #Tratamento de erros
    try:
      response = self._client.table(self._table_name).select('*').execute() #Comando SUPABASE.
      if response.data: #Caso a conexão seja bem sucedida
        return [self.to_model(item) for item in response.data] #Retornando do formato JSON (dict) para modelo de dados (T)
      return [] #retornando vazio
    #Caso de erro
    except Exception as e:
      print(f'Erro ao buscar todos os registros: {e}') #Mensagem de erro
      return [] #Retorna vazio
    
  ### Update
  def update(self, key: T, model: T) -> Optional[T]:
        #Tratamento de erros
        try:
            data = self.to_dict(model) # Do modelo de dados (T) para formato JSON (dict)
            response = self._client.table(self._table_name).update(data).eq(key).execute() #
            if response.data: #conexão com SUPABASE
                return self.to_model(response.data[0]) #Retornando do formato JSON (dict) para modelo de dados (T)
            return None #retorna nada
        #caso de erro
        except Exception as e:
            print(f"Erro ao atualizar registro: {e}") #mensagem de erro
            return None #retorna nada
  
  ### Delete
  def delete(self, key: T) -> bool: #deve retornar valores lógicos (True ou False)
    #tratamento de erros
    try: 
      response = self._client.table(self._table_name).delete().eq(key).execute() #tá pedindo o que retorne o nome da tabela e delete o que tiver com aquele ID. 
      return bool(response.data) #retorna verdadeiro se o registro for deletado
    #caso de erro
    except Exception as e:
      print(f"Erro ao deletar registro: {e}") #mensagem de erro
      return False #retorna falso