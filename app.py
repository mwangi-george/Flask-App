from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    title = "Goerge Mwangi's Portforlio"
    return render_template("index.html", title=title)


@app.route("/about")
def about():
    names = ["George", "Mark", "Ken", "Victoria", "Grace"]
    return render_template("about.html", names=names)
