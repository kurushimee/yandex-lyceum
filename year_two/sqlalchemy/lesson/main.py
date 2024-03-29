from flask import Flask

from year_two.sqlalchemy.lesson.data import db_session

app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"


def main():
    db_session.global_init("db/blogs.db")
    app.run()


if __name__ == "__main__":
    main()
