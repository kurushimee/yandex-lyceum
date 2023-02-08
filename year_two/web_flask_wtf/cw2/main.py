from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<title>")
@app.route("/index/<title>")
def base(title: str) -> str:
    return render_template("base.html", title=title)


@app.route("/training/<profession>")
def training(profession: str) -> str:
    return render_template("training.html", profession=profession)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
