from flask import Flask, render_template, url_for, request, flash, session, redirect, abort

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


@app.route("/profile/<username>")
def profile(username):
    if "userLogged" not in session or session["userLogged"] != username:
        abort(401)  # прерывание запроса с ошибкой 401 - нет доступа
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
    return render_template(template_name_or_list="page404.html", title="Страница не найдена", menu=menu)


@app.route(rule="/login", methods=["POST", "GET"])
def login():
    if "userLogged" in session:
        return redirect(url_for("profile", username=session["userLogged"]))
    elif request.form["username"] == "root" and request.form["password"] == "1111":
        session["userLogged"] = request.form["username"]
        return redirect(url_for("profile", username=session["userLogged"]))

    return render_template(template_name_or_list="login.html", title="Авторизация", menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
