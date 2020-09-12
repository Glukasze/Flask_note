from flask import Flask, render_template, request

app = Flask(__name__)

ideas = ["eat", "sleep", "play"]

@app.route('/')
def base():
    return render_template("base.html", ideas = ideas)

@app.route('/add')
def add():
    return render_template("add.html")

@app.route('/delete')
def delete():
    return render_template("delete.html", ideas = ideas)

@app.route('/edit')
def edit():
    return render_template("edit.html", ideas = ideas)


if __name__ == '__main__':
    app.run()
