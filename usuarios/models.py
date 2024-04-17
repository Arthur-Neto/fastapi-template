from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True

class UsuarioModel(Usuario):
    id: int
    email: str

class CreateUsuarioCommand(BaseModel):
    email: str

class UpdateUsuarioCommand(Usuario):
    id: int
    email: str