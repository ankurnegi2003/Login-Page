from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_URL = "sqlite:///./details.db"

engine = create_engine(
    db_URL, connect_args={'check_same_thread':False}
)
SessionLocal = sessionmaker(bind=engine,autoflush=False, autocommit=False)

Base = declarative_base()