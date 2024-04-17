from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = (
    "mssql+pyodbc://localhost/fastapi"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)