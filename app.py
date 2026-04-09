from flask import Flask, render_template, request, redirect

app = Flask(__name__)

notes = []

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/notes", methods=["GET","POST"])
def notes_page():

    if request.method == "POST":

        title = request.form["title"]
        content = request.form["content"]

        notes.append({
            "title": title,
            "content": content
        })

    return render_template("notes.html", notes=notes)


@app.route("/delete/<int:index>")
def delete(index):

    notes.pop(index)
    return redirect("/notes")


@app.route("/edit/<int:index>", methods=["GET","POST"])
def edit(index):

    note = notes[index]

    if request.method == "POST":

        note["title"] = request.form["title"]
        note["content"] = request.form["content"]

        return redirect("/notes")

    return render_template("edit.html", note=note, index=index)


app.run(debug=True)
