from flask import Flask, render_template, request
from players import players

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    results = players
    
    if request.method == "POST":
        position = request.form.get("position")
        search_query = request.form.get("search_query")
        nationality = request.form.get("nationality")
        league = request.form.get("league")
        min_age = request.form.get("min_age")
        max_age = request.form.get("max_age")

        if position:
            results = [p for p in results if p["position"].lower() == position.lower()]

        if nationality:
            results = [p for p in results if p["nationality"].lower() == nationality.lower()]

        if league:
            results = [p for p in results if p["league"].lower() == league.lower()]

        if min_age:
            results = [p for p in results if p["age"] >= int(min_age)]

        if max_age:
            results = [p for p in results if p["age"] <= int(max_age)]

        if search_query:
            results = [p for p in results if search_query.lower() in p["name"].lower()]

    return render_template("index.html", results=results)

if __name__ == '__main__':
    app.run(debug=True)