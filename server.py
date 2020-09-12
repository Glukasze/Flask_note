from flask import Flask, render_template, request

app = Flask(__name__)

ideas = ["eat", "sleep", "play"]


@app.route('/')
def base():
    return render_template("base.html", ideas = ideas)

@app.route("/note", methods=["GET", "POST"])
def note():
    return render_template("note.html")



if __name__ == '__main__':
    app.run()
