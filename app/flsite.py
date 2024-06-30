from flask import Flask, render_template, url_for, request, flash


app = Flask(__name__)
app.config["SECRET_KEY"] = "nikita_master"

menu = (
    {"name": "Установка", "url": "install-flask"},
    {"name": "Первое приложение", "url": "first-app"},
    {"name": "Обратная связь", "url": "contact"},
)


@app.route("/")
def index():
    return render_template("index.html", menu=menu, title="Index")


@app.route("/about")
def about_page():
    return render_template("about.html", menu=menu, title="About")


@app.route("/profile/<int:username>")
def user_page(username):
    return f"Профиль пользователя {username}"


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        print(request.form)
        if len(request.form["username"]) > 2:
            flash("Сообщение отправлено успешно", category="success")
        else:
            flash("Ошибка отправки данных", category="error")

    return render_template("contact.html", title="Обратная связь", menu=menu)


@app.errorhandler(404)
def pageNotFound(error):
    return render_template(template_name_or_list="page404.html", title="Страница не найдена", menu=menu), 404


# with app.test_request_context():
#     print(url_for("index"))
#     print(url_for("about_page"))
#     print(url_for("user_page", username="11"))

if __name__ == "__main__":
    app.run(debug=True)
