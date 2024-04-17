from sqlalchemy.orm import Session
from fastapi import HTTPException
from configurations.database import engine
from configurations.db_map import Usuario

from .models import CreateUsuarioCommand, UpdateUsuarioCommand

def criar_usuario(usuario: CreateUsuarioCommand):
    with Session(engine) as session:
        usuario_db = Usuario(
            email=usuario.email
        )
        session.add(usuario_db)
        session.commit()
        session.refresh(usuario_db)
        return usuario_db

def atualizar_usuario(usuario: UpdateUsuarioCommand):
    with Session(engine) as session:
        usuario_db = session.get(Usuario, usuario.id)
        if not usuario_db:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        usuario_db.sqlmodel_update(usuario)
        session.add(usuario_db)
        session.commit()
        session.refresh(usuario_db)
        return usuario_db

def deletar_usuario(id: int):
    with Session(engine) as session:
        usuario_db = session.get(Usuario, id)
        if not usuario_db:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        session.delete(usuario_db)
        session.commit()
