from flask import Flask, render_template, jsonify, json, abort, request, redirect, url_for
from model import db, load_db, save_db
db = load_db()
app = Flask(__name__) # global consturctor which represents our application
m = "Welcome to our first Flask application!"
f = "Akaash"
l = "Sharma"
@app.route("/")
def welcome(): #view function
    return render_template("home.html",
                            questions = db) #jinja variable passing
@app.route("/questions/<int:index>")
def questions_view(index):
    try:    
        questions_db = db[index]
        return render_template("quiz.html",
                                index=index,
                                  question=questions_db,
                                  max_index=len(db) - 1)
    except IndexError:
        abort(404, description="Question not found")
new_question = {}
@app.route("/add_new_question", methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        new_question = {
            "question": request.form['question'],
            "answer": request.form['answer'],
        }
        db.append(new_question)
        save_db()
        return redirect(url_for("questions_view", index=len(db)-1))
    else:
         return render_template("add_question.html")
#Remove question functionality
@app.route("/remove_a_question/<int:index>", methods=['GET', 'POST'])
def remove_question(index):
    try:
        question = db[index]
        if request.method == 'POST':
            del db[index]
            save_db()
            return redirect(url_for("welcome"))
        else:
            return render_template("remove_question.html",
                                    index=index,
                                    question= db[index])
    except IndexError:
        abort(404, description="Question not found")
# Creating a REST API for our Full-Stack multi page application
@app.route("/api/questions")
def api_questions_list():
    return jsonify(db)
@app.route("/api/questions/<int:index>")
def api_questions_detail(index):
    try:
        question = db[index]
        return jsonify(question)
    except IndexError:
        abort(404, description="Question not found")


if __name__ == "__main__":
    app.run(debug=True)
