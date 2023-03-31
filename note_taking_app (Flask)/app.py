
from flask import Flask, render_template, request, flash,redirect,url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note.strip() == "":
            flash("Note cannot be empty")
        elif note in notes:
            flash("Note already exists")
        else:
            notes.append(note)
    return render_template("home.html", notes=notes)

@app.route('/clear', methods=["GET"])
def clear_notes():
    global notes
    notes = []
    flash("Notes cleared")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


