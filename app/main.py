
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="My Diary",
    description="個人日誌空間網站",
    version="1.0.0"
)

# 靜態檔案
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# HTML 模板
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={}
    )


@app.get("/u/{username}")
async def personal_space(request: Request, username: str):

    # 暫時使用測試資料
    posts = [
        {
            "title": "我的第一篇日誌",
            "date": "2026-11-05",
            "content": "這是我的第一篇個人日誌，歡迎來到我的空間。"
        },
        {
            "title": "今天的生活",
            "date": "2026-11-04",
            "content": "今天開始建立自己的個人日誌網站。"
        }
    ]

    return templates.TemplateResponse(
        request=request,
        name="space.html",
        context={
            "username": username,
            "posts": posts
        }
    )


@app.get("/health")
async def health():
    return {"status": "online"}

