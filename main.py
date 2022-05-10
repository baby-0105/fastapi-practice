from typing import Optional, Set, Dict

from fastapi import Body, FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights
