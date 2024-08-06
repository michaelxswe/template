import contextlib
from app.database.core import Base, engine
from app.api import router as v1_router
from fastapi import FastAPI


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)
    print("Shutting down...")


app = FastAPI(lifespan=lifespan)

app.include_router(router=v1_router)
