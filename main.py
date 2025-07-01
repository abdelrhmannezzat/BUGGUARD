from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlmodel import SQLModel
from db.session import engine

from Controller.TaskManagmentController import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(
    title="Task Management API",
    description="Manage your tasks with create, read, update, delete operations.",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(router)


@app.get("/", tags=["Root"])
def root():
    return {
        "api": app.title,
        "version": app.version,
        "endpoints": [
            {"path": route.path, "methods": list(route.methods - {"HEAD", "OPTIONS"})}
            for route in app.router.routes
            if getattr(route, "include_in_schema", False)
        ]
    }


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
