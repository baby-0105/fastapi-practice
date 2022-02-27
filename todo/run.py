from router import app

import uvicorn

# コマンドラインから直接呼ばれたかを判定する
if __name__ == "__main__":
    uvicorn.run(app=app)
