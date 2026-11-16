
from app.database.session import SessionLocal
from app.models import User, Space, Post

db = SessionLocal()

try:
    # 1. 查詢會員
    user = db.query(User).filter(
        User.username == "relationship_demo"
    ).first()

    if not user:
        print("找不到測試會員")
    else:
        # 2. 透過 User 找到 Space
        space = user.space

        print("會員：", user.username)

        if space:
            print("個人空間：", space.title)

            # 3. 透過 Space 找到所有文章
            print("\n會員空間中的文章：")

            for post in space.posts:
                print("文章標題：", post.title)
                print("文章內容：", post.content)
                print("--------------------")

            # 4. 從文章反向找到 Space 和 User
            if space.posts:
                first_post = space.posts[0]

                print("\n反向關聯測試：")
                print("文章：", first_post.title)
                print("所屬空間：", first_post.space.title)
                print("文章作者：", first_post.space.user.username)

        else:
            print("這個會員還沒有個人空間")

finally:
    db.close()
