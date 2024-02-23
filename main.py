from flask import Flask, render_template, request
import random
import os
from art_projects import beginner_projects, intermediate_projects, advanced_projects

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def art_spark():
    errors = []
    if request.method =="POST":
        category = request.form.get("category")
        difficulty = request.form.get("difficulty")
        if not category:
            errors.append("Please choose a category.")
        if not difficulty:
            errors.append("Please choose a difficulty.")
        if category and difficulty:
            if difficulty == "beginner":
                return render_template("home.html", category=category, difficulty=difficulty, project=random.choice(beginner_projects[category]), errors=[])
            if difficulty == "intermediate":
                return render_template("home.html", category=category, difficulty=difficulty, project=random.choice(intermediate_projects[category]), errors=[])
            if difficulty == "advanced":
                return render_template("home.html", category=category, difficulty=difficulty, project=random.choice(advanced_projects[category]), errors=[])
    return render_template("home.html", category="", difficulty="", errors=errors)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
