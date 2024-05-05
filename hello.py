from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__, template_folder='templates')

# Create a route decorator
@app.route('/')
def index():
    first_name = "Anirudh"
    stuff = "This is <strong>Bold</strong> Test"

    some_list = ["Python", "Machine", "Learning", "SQL", 44, "Angular"]
    return render_template("index.html", first_name=first_name, stuff=stuff, lists=some_list)

# Dynamic route that accepts a 'name' parameter
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)


# Create custome Error Pages

#Invalid URL

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


#Internal Server Error

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500