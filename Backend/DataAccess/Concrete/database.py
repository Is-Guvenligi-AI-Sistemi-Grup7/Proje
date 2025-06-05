from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from Core.Constants.Database import DATABASE_URL

# Engine oluştur
engine = create_engine(DATABASE_URL)

# Session maker oluştur
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base sınıfı (entity modellerin buradan kalıtım alacak)
Base = declarative_base()

# Dependency olarak kullanılmak için örnek (FastAPI için)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
