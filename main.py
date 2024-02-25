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

@app.route('/random', methods=["POST"])
def randomize():
    # figure out how to pick a random value nested in a list within a dictionary
    # get a random number to choose the difficulty (switch scenario)

    # try random.choice()

    categories = ["medium", "theme", "technique", "color-palette", "emotion", "art-movement"]
    difficulties = ["beginner", "intermediate", "advanced"]

    random_catergory = random.choice(categories)
    random_difficulty = random.choice(difficulties)
    random_project = 100 #random_difficulty[random_catergory]

    if random_difficulty == "beginner":
        return render_template("home.html", category=random_catergory, difficulty=random_difficulty, project=random.choice(beginner_projects[random_catergory]))
    if random_difficulty == "intermediate":
        return render_template("home.html", category=random_catergory, difficulty=random_difficulty, project=random.choice(intermediate_projects[random_catergory]))
    if random_difficulty == "advanced":
        return render_template("home.html", category=random_catergory, difficulty=random_difficulty, project=random.choice(advanced_projects[random_catergory]))

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
