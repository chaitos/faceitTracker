from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "postgresql+asyncpg://user:password@localhost:5432/dbname"


engine = create_async_engine(DATABASE_URL, echo=True)
