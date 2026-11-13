
from app.database.session import SessionLocal
from app.models import User


def update_user_email(user_id: int, new_email: str):
    db = SessionLocal()

    try:
        # 根據會員 ID 查詢會員
        user = db.query(User).filter(
            User.id == user_id
        ).first()

        if user is None:
            print("找不到會員")
            return

        # 修改 Email
        user.email = new_email

        # 提交修改
        db.commit()
        db.refresh(user)

        print("會員資料修改成功")
        print("會員 ID：", user.id)
        print("新 Email：", user.email)

    except Exception as e:
        db.rollback()
        print("修改失敗：", e)

    finally:
        db.close()


# 測試：修改 ID 為 1 的會員
update_user_email(
    user_id=1,
    new_email="alice_new@example.com"
)
