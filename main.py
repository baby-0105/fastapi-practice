from datetime import date
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

def main(user_id: str):
    return user_id

class User(BaseModel):
    id: int
    name: str
    joined: date

my_user: User = User(id=3, name="John Doe", joined="2018-07-19")

second_user_data = {
    "id": 4,
    "name": "Mary",
    "joined": "2018-11-30",
}

my_second_user: User = User(**second_user_data)
