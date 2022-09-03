from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    """ Landing Page """
    return render_template("index.html")

@app.route("/about")
def about():
    """ About us page """
    return render_template("about.html")

@app.route("/research")
def research():
    """ Psychological research page """
    return render_template("research.html")

@app.route("/primary")
def primary():
    """ Primary education tutoring page """
    return render_template("primary-education.html")

@app.route("/secondary")
def secondary():
    """ Secondary education tutoring page """
    return render_template("secondary-education.html")

@app.route("/training")
def training():
    """ Training page """
    return render_template("training.html")

@app.route("/apply")
def apply():
    """ Applicaiton page """
    return render_template("apply.html")

if __name__ == "__main__":
    app.run(debug=True)