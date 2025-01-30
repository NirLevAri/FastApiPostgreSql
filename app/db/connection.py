import asyncpg
from typing import Optional
from app.db.config import settings

DB_POOL: Optional[asyncpg.Pool] = None

async def connect_to_db():
    global DB_POOL
    if DB_POOL is None:
        DB_POOL = await asyncpg.create_pool(settings.DATABASE_URL, min_size=1, max_size=5)
    return DB_POOL

async def close_db_connection():
    global DB_POOL
    if DB_POOL is not None:
        await DB_POOL.close()
        DB_POOL = None

async def get_connection():
    global DB_POOL
    if DB_POOL is None:
        await connect_to_db()
    return DB_POOL.acquire()
