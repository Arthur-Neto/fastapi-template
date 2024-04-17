from sqlalchemy.orm import Session
from configurations.database import engine
from configurations.db_map import Usuario

def buscar_usuario_por_id(id: int):
    with Session(engine) as session:
        return session.query(Usuario).filter(Usuario.id == id).first()

def buscar_usuarios(skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        return (
            session.query(Usuario)
            .order_by(Usuario.id)
            .offset(skip)
            .limit(limit)
            .all()
        )
