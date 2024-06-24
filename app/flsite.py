from flask import Flask, render_template


app = Flask(__name__)

menu = ("Установка", "Приложение", "Обратная связь")


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", menu=menu, title="Index")


@app.route("/about")
def about_page():
    return render_template("about.html", menu=menu, title="About")


if __name__ == "__main__":
    app.run(debug=True)
