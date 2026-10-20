from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/test_db"
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://training_omeb_user:9hFyKwH0YoyK2Ynelaa1WpXZd8FmZ5cC@dpg-dbbfgq3rjlhs73e3h1c0-a.oregon-postgres.render.com/training_omeb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()