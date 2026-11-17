
from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models import User, Post

router = APIRouter()

templates = Jinja2Templates(directory="templates")


# 顯示發表日誌頁面
@router.get("/u/{username}/posts/new")
def new_post_page(
    request: Request,
    username: str,
    db: Session = Depends(get_db)
):
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

    if not user.space:
        raise HTTPException(
            status_code=404,
            detail="這個會員尚未建立個人空間"
        )

    return templates.TemplateResponse(
        request=request,
        name="post_new.html",
        context={
            "username": username
        }
    )


# 接收表單並新增日誌
@router.post("/u/{username}/posts/new")
def create_post(
    username: str,
    title: str = Form(..., max_length=100),
    content: str = Form(...),
    db: Session = Depends(get_db)
):
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

    if not user.space:
        raise HTTPException(
            status_code=404,
            detail="這個會員尚未建立個人空間"
        )

    post = Post(
        space_id=user.space.id,
        title=title,
        content=content
    )

    db.add(post)
    db.commit()

    return RedirectResponse(
        url=f"/u/{username}",
        status_code=303
    )


# 顯示編輯日誌頁面
@router.get("/u/{username}/posts/{post_id}/edit")
def edit_post_page(
    request: Request,
    username: str,
    post_id: int,
    db: Session = Depends(get_db)
):
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

    post = (
        db.query(Post)
        .filter(
            Post.id == post_id,
            Post.space_id == user.space.id
        )
        .first()
    )

    if not post:
        raise HTTPException(
            status_code=404,
            detail="找不到這篇日誌"
        )

    return templates.TemplateResponse(
        request=request,
        name="post_edit.html",
        context={
            "username": username,
            "post": post
        }
    )


# 接收修改資料並更新日誌
@router.post("/u/{username}/posts/{post_id}/edit")
def update_post(
    username: str,
    post_id: int,
    title: str = Form(..., max_length=200),
    content: str = Form(...),
    db: Session = Depends(get_db)
):
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

    post = (
        db.query(Post)
        .filter(
            Post.id == post_id,
            Post.space_id == user.space.id
        )
        .first()
    )

    if not post:
        raise HTTPException(
            status_code=404,
            detail="找不到這篇日誌"
        )

    post.title = title
    post.content = content

    db.commit()

    return RedirectResponse(
        url=f"/u/{username}",
        status_code=303
    )

# 刪除日誌
@router.post("/u/{username}/posts/{post_id}/delete")
def delete_post(
    username: str,
    post_id: int,
    db: Session = Depends(get_db)
):
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

    post = (
        db.query(Post)
        .filter(
            Post.id == post_id,
            Post.space_id == user.space.id
        )
        .first()
    )

    if not post:
        raise HTTPException(
            status_code=404,
            detail="找不到這篇日誌"
        )

    db.delete(post)
    db.commit()

    return RedirectResponse(
        url=f"/u/{username}",
        status_code=303
    )
