from models import *
import db
import os


if __name__ == "__main__":
    print(__name__)
    path = SQLITE3_NAME
    if not os.path.isfile(path):


        Base.metadata.create_all(db.engine)

    admin = User(username="admin", password="admin1234", mail="admin@co.com")
    db.session.add(admin)
    db.session.commit()

    task = Task(
        user_id=admin.id,
        content='〇〇の締め切り',
        deadline=datetime(2019, 12, 25, 12, 00, 00),
    )
    print(task)
    db.session.add(task)
    db.session.commit()

    db.session.close()
