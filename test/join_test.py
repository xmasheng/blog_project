
from app.database.session import SessionLocal
from app.models import User, Post

db = SessionLocal()

try:
    results = (
        db.query(User, Post)
        .join(Post, User.id == Post.user_id)
        .all()
    )

    for user, post in results:
        print("會員：", user.username)
        print("文章：", post.title)
        print("--------------------")

finally:
    db.close()
