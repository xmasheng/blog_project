
from app.database.session import SessionLocal
from app.models import User


def delete_user(user_id: int):
    db = SessionLocal()

    try:
        # 根據 ID 查詢會員
        user = db.query(User).filter(
            User.id == user_id
        ).first()

        if user is None:
            print("找不到會員")
            return

        print("準備刪除以下會員：")
        print("ID：", user.id)
        print("帳號：", user.username)
        print("Email：", user.email)

        # 二次確認
        confirmation = input("確定刪除？請輸入 DELETE：")

        if confirmation != "DELETE":
            print("已取消刪除")
            return

        db.delete(user)
        db.commit()

        print("會員刪除成功")

    except Exception as e:
        db.rollback()
        print("刪除失敗：", e)

    finally:
        db.close()


# 輸入要刪除的會員 ID
target_id = int(input("請輸入會員 ID："))

delete_user(target_id)
