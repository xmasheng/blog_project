
from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates

from app.database.dependencies import get_db
from app.models import User

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/u/{username}")
def personal_space(
    request: Request,
    username: str,
    db: Session = Depends(get_db)
):
    # 透過 username 查詢會員
    user = (
        db.query(User)
        .filter(User.username == username)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="找不到這個會員"
        )

    # 取得會員的個人空間
    space = user.space

    if not space:
        raise HTTPException(
            status_code=404,
            detail="這個會員尚未建立個人空間"
        )

    # 取得空間中的文章
    posts = sorted(
        space.posts,
        key=lambda post: post.created_at,
        reverse=True
    )

    # 整理模板需要的資料
    post_data = [
        {
            "title": post.title,
            "date": post.created_at.strftime("%Y-%m-%d"),
            "content": post.content
        }
        for post in posts
    ]

    return templates.TemplateResponse(
        request=request,
        name="space.html",
        context={
            "username": user.username,
            "space": space,
            "posts": post_data
        }
    )

