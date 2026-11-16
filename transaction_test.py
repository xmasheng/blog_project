from app.database.session import SessionLocal
from app.models import User, Space

db = SessionLocal()

try:
    # 建立會員
    new_user = User(
        username="transaction_demo",
        email="transaction@example.com",
        password_hash="demo_hash"
    )

    db.add(new_user)

    # 先送出 SQL，取得會員 ID
    db.flush()

    # 建立會員個人空間
    new_space = Space(
        user_id=new_user.id,
        title="Transaction 測試空間",
        theme="default"
    )

    db.add(new_space)

    # 所有操作成功，正式提交
    db.commit()

    print("會員與個人空間建立成功！")

except Exception as e:
    # 發生錯誤，取消整筆交易
    db.rollback()

    print("交易失敗，已回復資料庫變更")
    print("錯誤原因：", e)

finally:
    db.close()
