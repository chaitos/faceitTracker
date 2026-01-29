
from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "postgresql+psycopg2://postgres:0811@localhost:5432/faceitTrackerDB" #указываем адрес бд

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)



Base = declarative_base()

Base.metadata.create_all(bind=engine)



