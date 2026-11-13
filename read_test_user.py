
from app.database.session import SessionLocal
from app.models import User

db = SessionLocal()

try:
    # 查詢所有會員
    users = db.query(User).all()

    print("===== 會員清單 =====")

    for user in users:
        print(f"ID：{user.id}")
        print(f"帳號：{user.username}")
        print(f"Email：{user.email}")
        print(f"註冊時間：{user.created_at}")
        print("--------------------")

    # 查詢指定會員
    alice = db.query(User).filter(
        User.username == "alice"
    ).first()

    if alice:
        print("找到 Alice！")
        print("會員 ID：", alice.id)
    else:
        print("找不到會員")

finally:
    db.close()

