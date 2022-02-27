# -*- coding: utf-8 -*-
from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request
import db
from models import User, Task


app = FastAPI(
    title='FastAPIでつくるtoDoアプリケーション',
    description='FastAPIチュートリアル：FastAPI(とstarlette)でシンプルなtoDoアプリを作りましょう．',
)



templates = Jinja2Templates(directory="templates")
jinja_env = templates.env


def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

def admin(request: Request):
    return templates.TemplateResponse(
        "admin.html",
        {
            "request": request,
        }
    )
