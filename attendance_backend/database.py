from sqlmodel import create_engine, Session
from contextlib import contextmanager

DATABASE_URL = "postgresql://postgres:root@localhost/erp_db"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
