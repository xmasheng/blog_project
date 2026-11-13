
from app.database.session import SessionLocal
from app.models import User, Space, Post

db = SessionLocal()

try:
    # 查詢測試會員
    user = db.query(User).filter(
        User.username == "relationship_demo"
    ).first()

    # 如果不存在，就建立測試資料
    if user is None:
        user = User(
            username="relationship_demo",
            email="relationship@example.com",
            password_hash="demo_hash_not_for_login"
        )

        # 建立個人空間
        user.space = Space(
            title="我的測試空間",
            theme="default"
        )

        # 建立兩篇日誌
        user.posts = [
            Post(
                title="我的第一篇日誌",
                content="這是我的第一篇測試文章。"
            ),
            Post(
                title="我的 Python 學習紀錄",
                content="今天學習 SQLAlchemy Relationship。"
            )
        ]

        db.add(user)
        db.commit()
        print("測試會員與相關資料建立成功！")

    else:
        print("測試會員已存在，直接讀取資料。")

    # 重新讀取會員資料
    db.refresh(user)

    print("\n===== 會員資料 =====")
    print("帳號：", user.username)

    print("\n===== 個人空間 =====")
    print("空間名稱：", user.space.title)
    print("樣板：", user.space.theme)

    print("\n===== 日誌文章 =====")

    for post in user.posts:
        print("文章標題：", post.title)
        print("文章內容：", post.content)
        print("--------------------")

except Exception as e:
    db.rollback()
    print("發生錯誤：", e)

finally:
    db.close()

