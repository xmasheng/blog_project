
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routers import spaces

app = FastAPI(
    title="Blog Project",
    description="個人日誌網站",
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
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={}
    )


# 註冊個人空間 Router
app.include_router(spaces.router)


@app.get("/health")
def health():
    return {"status": "online"}


