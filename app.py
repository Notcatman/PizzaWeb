from flask import Flask, render_template, redirect, url_for
from forms.Flaskform import RegistrForm

app = Flask(__name__)
app.secret_key = "Bunybn"

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrForm()
    if form.validate_on_submit():
        return redirect(url_for("submithome"))
    return render_template("register.html", form=form)

@app.route("/welcome")
def submithome():
    return render_template("submithome.html")

@app.route("/pizza")
def pizza():
    return render_template("pizza.html")


if __name__ == "__main__":
    app.run(debug=True, port=4444)

