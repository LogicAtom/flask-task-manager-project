""" import the os """
import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    """ def _tasks is the default site url."""
    tasks = list(mongo.db.tasks.find())
    return render_template("tasks.html", tasks=tasks)


@app.route("/search", methods=["GET", "POST"])
def search():
    """ def search to query mongodb tasks collection """
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    return render_template("tasks.html", tasks=tasks)


@app.route("/register", methods=["GET", "POST"])
def register():
    """ Register an account on mongodb tasks collection """

    if session and session["user"]:
        return redirect(url_for("get_tasks"))

    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """ def login function, to LogIn to the database to access CRUD """
    if session and session["user"]:
        return redirect(url_for("get_tasks"))

    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Password Entered")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username Entered")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    """ profile to grab the session users username from db """
    if not session and not session["user"]:
        return redirect(url_for("login"))

    # Write code here to show user tasks in the profile page

    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    user_tasks = list(mongo.db.tasks.find({"created_by": session["user"]}))

    return render_template(
        "profile.html", username=username, user_tasks=user_tasks)


@app.route("/logout")
def logout():
    """ logout to remove user from session cookie """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/task/add", methods=["GET", "POST"])
def add_task():
    """ add a task into the database """
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        task = {
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(task)
        flash("Task Successfully Added")
        return redirect(url_for("get_tasks"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_task.html", categories=categories)


@app.route("/task/<task_id>/edit", methods=["GET", "POST"])
def edit_task(task_id):
    """ CRUD update aka edit a task """
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }
        mongo.db.tasks.update({"_id": ObjectId(task_id)}, submit)
        flash("Task Successfully Updated")

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_task.html", task=task, categories=categories)


@app.route("/task/<task_id>/delete")
def delete_task(task_id):
    """ CRUD delete a task from database """
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("get_tasks"))


@app.route("/categories")
def get_categories():
    """ Search database for category name """
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/category/add", methods=["GET", "POST"])
def add_category():
    """ Admin method to create new categories in the db """
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/category/<category_id>/edit", methods=["GET", "POST"])
def edit_category(category_id):
    """ CRUD update category by id """
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/category/<category_id>/delete")
def delete_category(category_id):
    """ Admin CRUD delete category by id """
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)