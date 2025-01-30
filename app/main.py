from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.db.connection import connect_to_db, close_db_connection
from app.routes import api, issue, apis_issues_association


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_db()

    yield

    await close_db_connection()


app = FastAPI(lifespan=lifespan)

app.include_router(api.router)
app.include_router(issue.router)
app.include_router(apis_issues_association.router)
