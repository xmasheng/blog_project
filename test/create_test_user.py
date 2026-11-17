
from app.database.session import SessionLocal
from app.models import User


# 建立資料庫 Session
db = SessionLocal()

try:
    # 檢查測試會員是否已存在
    existing_user = db.query(User).filter(
        User.username == "alice"
    ).first()

    if existing_user:
        print("會員已存在")
        print("會員 ID：", existing_user.id)

    else:
        # 建立會員物件
        new_user = User(
            username="alice",
            email="alice@example.com",
            password_hash="demo_hash_not_for_login"
        )

        # 加入待寫入清單
        db.add(new_user)

        # 正式寫入 PostgreSQL
        db.commit()

        # 重新取得資料庫產生的 ID
        db.refresh(new_user)

        print("會員建立成功！")
        print("會員 ID：", new_user.id)
        print("會員帳號：", new_user.username)
        print("會員 Email：", new_user.email)

except Exception as e:
    db.rollback()
    print("發生錯誤：", e)

finally:
    db.close()
