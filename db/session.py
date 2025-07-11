from sqlmodel import Session, create_engine, SQLModel

DATABASE_URL = "sqlite:///./tasks.db"

engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session
