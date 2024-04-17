from typing import Optional

from sqlmodel import Field, SQLModel

class Usuario(SQLModel, table=True):
    __tablename__ = "Usuarios"

    id: Optional[int] = Field(default=None, primary_key=True)
    email: str