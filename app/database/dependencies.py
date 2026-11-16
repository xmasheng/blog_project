#資料庫依賴注入模式
from app.database.session import SessionLocal


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
