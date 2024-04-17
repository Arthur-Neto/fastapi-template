from typing import List
from fastapi import FastAPI, HTTPException
from usuarios import commands, models, queries

app = FastAPI()

@app.get("/usuarios/", response_model=List[models.UsuarioModel])
def buscar_usuarios(skip: int = 0, limit: int = 25):
    users = queries.buscar_usuarios(skip=skip, limit=limit)
    return users

@app.get("/usuarios/{id}", response_model=models.UsuarioModel)
def buscar_usuario_por_id(id: int):
    db_user = queries.buscar_usuario_por_id(id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return db_user

@app.post("/usuarios/", response_model=models.UsuarioModel)
def criar_usuario(usuario: models.CreateUsuarioCommand):
    return commands.criar_usuario(usuario)

@app.put("/usuarios/", response_model=models.UpdateUsuarioCommand)
def atualizar_usuario(usuario: models.UpdateUsuarioCommand):
    return commands.atualizar_usuario(usuario)

@app.delete("/usuarios/{id}")
def deletar_usuario(id: int):
    commands.deletar_usuario(id)
    return {}