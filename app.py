import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env
from functools import wraps

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('login'))

    return wrap


@app.route("/browse")
def browse():
    query = request.args.get("query")
    if query:
        experiences = list(mongo.db.experiences.find(
            {"$text": {"$search": query}}))
    else:
        experiences = list(mongo.db.experiences.find())
    return render_template("browse.html", experiences=experiences)


@app.route("/discover")
def discover():
    regions = list(mongo.db.regions.find())
    return render_template("discover.html", regions=regions)


@app.route("/region")
def region():
    query = request.args.get("query")
    if query:
        regions = list(mongo.db.regions.find())
        experiences = list(mongo.db.experiences.find(
            {"$text": {"$search": query}}))
    else:
        regions = list(mongo.db.regions.find())
        experiences = list(mongo.db.experiences.find())
    return render_template(
        "region.html", regions=regions, experiences=experiences)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "user_image": request.form.get("user_image").lower(),
            "gender": request.form.get("gender").lower(),
            "nationality": request.form.get("nationality").lower(),
            "birthdate": request.form.get("birthdate").lower(),
            "email": request.form.get("email").lower(),
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})
    experiences = list(mongo.db.experiences.find())

    if session["user"]:
        return render_template(
            "profile.html", username=username, experiences=experiences)

    return redirect(url_for("login"))


@app.route("/edit_profile/<user_id>", methods=["GET", "POST"])
def edit_profile(user_id):
    if request.method == "POST":
        submit = {
            "username": request.form.get("username"),
            "password": generate_password_hash(request.form.get("password")),
            "user_image": request.form.get(
                "user_image"),
            "gender": request.form.get("gender"),
            "nationality": request.form.get(
                "nationality"),
            "birthdate": request.form.get("birthdate"),
            "email": request.form.get("email").lower(),
        }

        mongo.db.users.update({"_id": ObjectId(user_id)}, submit)
        flash("Profile Successfully Updated")

    username = mongo.db.users.find_one(
        {"username": session["user"]})

    return render_template("edit_profile.html", username=username)


@app.route("/delete_profile/<user_id>", methods=["GET"])
def delete_profile(user_id):
    mongo.db.users.remove({"_id": ObjectId(user_id)})
    flash("Profile Deleted")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("browse"))


@app.route("/add_experience", methods=["GET", "POST"])
def add_experience():
    if request.method == "POST":
        experience = {
            "category_name": request.form.get("category_name"),
            "experience_name": request.form.get("experience_name"),
            "region_name": request.form.get("region_name"),
            "location_name": request.form.get("location_name"),
            "experience_date": request.form.get("experience_date"),
            "experience_description": request.form.get(
                "experience_description"),
            "picture": request.form.get("picture"),
            "picture2": request.form.get("picture2"),
            "picture3": request.form.get("picture3"),
            "picture4": request.form.get("picture4"),
            "picture5": request.form.get("picture5"),
            "latitude": request.form.get("latitude"),
            "longitude": request.form.get("longitude"),
            "by": session["user"]
        }
        mongo.db.experiences.insert_one(experience)
        flash("New experience added!")
        return redirect(url_for("browse"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    regions = mongo.db.regions.find().sort("region_name", 1)
    return render_template(
        "add_experience.html", categories=categories,
        regions=regions)


@app.route("/view_experience/<experience_id>", methods=["GET"])
def view_experience(experience_id):
    experience = mongo.db.experiences.find_one(
        {"_id": ObjectId(experience_id)})
    return render_template("view_experience.html",
                           experience_id=experience)


@app.route("/edit_experience/<experience_id>", methods=["GET", "POST"])
def edit_experience(experience_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "experience_name": request.form.get("experience_name"),
            "region_name": request.form.get("region_name"),
            "location_name": request.form.get("location_name"),
            "experience_date": request.form.get("experience_date"),
            "experience_description": request.form.get(
                "experience_description"),
            "picture": request.form.get("picture"),
            "picture2": request.form.get("picture2"),
            "picture3": request.form.get("picture3"),
            "picture4": request.form.get("picture4"),
            "picture5": request.form.get("picture5"),
            "latitude": request.form.get("latitude"),
            "longitude": request.form.get("longitude"),
            "by": session["user"]
        }
        mongo.db.experiences.update({"_id": ObjectId(experience_id)}, submit)
        flash("Experience Successfully Updated")

    experience = mongo.db.experiences.find_one(
        {"_id": ObjectId(experience_id)})
    categories = mongo.db.categories.find().sort(
        "category_name", 1)
    regions = mongo.db.regions.find().sort("region_name", 1)
    return render_template(
        "edit_experience.html", experience=experience,
        categories=categories, regions=regions,)


@app.route("/delete_experience/<experience_id>", methods=["GET"])
def delete_experience(experience_id):
    mongo.db.experiences.remove({"_id": ObjectId(experience_id)})
    flash("Experience Deleted")
    username = mongo.db.users.find_one(
        {"username": session["user"]})
    return render_template("profile.html", username=username)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
