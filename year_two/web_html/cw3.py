from flask import Flask

app = Flask(__name__)


@app.route("/")
def root() -> str:
    return "Миссия Колонизация Марса"


@app.route("/index")
def index() -> str:
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion() -> str:
    promotion = (
        "Человечество вырастает из детства.",
        "Человечеству мала одна планета.",
        "Мы сделаем обитаемыми безжизненные пока планеты.",
        "И начнем с Марса!",
        "Присоединяйся!",
    )
    return "</br>".join(promotion)


@app.route("/image_mars")
def image_mars() -> str:
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.png" alt="Марс">
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
