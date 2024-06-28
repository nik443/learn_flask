from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = (
    {"name": "Установка", "url": "install-flask"},
    {"name": "Первое приложение", "url": "first-app"},
    {"name": "Обратная связь", "url": "contact"},
)


@app.route("/")
def index():
    print(url_for("index"))
    return render_template("index.html", menu=menu, title="Index")


@app.route("/about")
def about_page():
    print(url_for("about_page"))
    return render_template("about.html", menu=menu, title="About")


@app.route("/profile/<int:username>")
def user_page(username):
    return f"Профиль пользователя {username}"

@app.route("/contact")
def contact():
    return render_template("contact.html")


# with app.test_request_context():
#     print(url_for("index"))
#     print(url_for("about_page"))
#     print(url_for("user_page", username="11"))

if __name__ == "__main__":
    app.run(debug=True)
