from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base() # クラス定義が自動的にテーブル定義とひもづく
RDB_PATH = 'sqlite:///db.sqlite3'
ECHO_LOG = True

# create_engine：sqlarchemyの機能を提供するためのオブジェクト
engine = create_engine(
    RDB_PATH, echo=ECHO_LOG
)

# sessionの生成
Session = sessionmaker(bind=engine)
session = Session()
