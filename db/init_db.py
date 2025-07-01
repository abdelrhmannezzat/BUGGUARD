from db.session import engine
from sqlmodel import SQLModel


def init_db():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    init_db()
