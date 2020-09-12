from flask import Flask, render_template, request, redirect

app = Flask(__name__)

notes = ["eat", "sleep", "play"]
edits_counter = 0


@app.route('/', methods=["GET", "POST"])
def base():
    if request.method == "POST":
        notes.remove(request.form["delete_button"])
        global edits_counter
        edits_counter += 1
        return redirect("/")
    return render_template("base.html", notes = notes, edits_counter = edits_counter)

@app.route("/note", methods=["GET", "POST"])
def note():
    if request.method == "POST":
        global edits_counter
        edits_counter += 1
        notes.append(request.form["edit_note"])
        return redirect("/")

    return render_template("note.html")



if __name__ == '__main__':
    app.run()
