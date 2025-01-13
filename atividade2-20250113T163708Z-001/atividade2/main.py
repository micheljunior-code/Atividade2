from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Base, Tarefa
from database import engine, get_db
from schemas import TarefaCreate, Tarefa

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/tarefas/", response_model=Tarefa)
def create_tarefa(tarefa: TarefaCreate, db: Session = Depends(get_db)):
    db_tarefa = Tarefa(**tarefa.dict())
    db.add(db_tarefa)
    db.commit()
    db.refresh(db_tarefa)
    return db_tarefa

@app.get("/tarefas/{tarefa_id}", response_model=Tarefa)
def read_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    db_tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if not db_tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return db_tarefa

@app.put("/tarefas/{tarefa_id}", response_model=Tarefa)
def update_tarefa(tarefa_id: int, tarefa: TarefaCreate, db: Session = Depends(get_db)):
    db_tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if not db_tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    for key, value in tarefa.dict().items():
        setattr(db_tarefa, key, value)
    db.commit()
    db.refresh(db_tarefa)
    return db_tarefa

@app.delete("/tarefas/{tarefa_id}")
def delete_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    db_tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if not db_tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    db.delete(db_tarefa)
    db.commit()
    return {"message": "Tarefa deletada com sucesso"}
