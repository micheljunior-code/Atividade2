from pydantic import BaseModel

class TarefaBase(BaseModel):
    titulo: str
    descricao: str
    completa: bool = False

class TarefaCreate(TarefaBase):
    pass

class Tarefa(TarefaBase):
    id: int

    class Config:
        orm_mode = True
