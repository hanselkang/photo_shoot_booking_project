from flask import Blueprint, Flask, redirect, render_template, request
from models.photographer import Photographer
import repositories.photographer_repository as photographer_repository

photographers_blueprint = Blueprint("photographers", __name__)

# index
@photographers_blueprint.route("/photographers")
def photographers():
    photographers = photographer_repository.select_all()
    return render_template("photographers/photographers.html", photographers=photographers)


# new
@photographers_blueprint.route("/photographers/new")
def new_photographer():
    photographers = photographer_repository.select_all()
    return render_template("photographers/new.html", photographers=photographers)

# create
@photographers_blueprint.route("/photographers", methods=["POST"])
def create_photographer():
    name = request.form["name"]
    email = request.form["email"]
    portfolio_address = request.form["portfolio_address"]
    new_photographer = Photographer(name, email,
                                    portfolio_address)
    photographer_repository.save(new_photographer)
    return redirect("/photographers")

# edit
@photographers_blueprint.route("/photographers/<id>/edit")
def edit_photographer(id):
    photographer = photographer_repository.select(id)
    return render_template('photographers/edit.html', photographer=photographer)

# update

@photographers_blueprint.route("/photographers/<id>", methods=["GET","POST"])
def update_photographer(id):
    name = request.form["name"]
    email = request.form["email"]
    portfolio_address = request.form["portfolio_address"]
    edit_photographer = Photographer(name, email,
                                    portfolio_address, id)
    photographer_repository.update(edit_photographer)
    return redirect("/photographers")


# delete
@photographers_blueprint.route("/photographers/<id>/delete", methods=['POST'])
def delete_photographer(id):
    photographer_repository.delete(id)
    return redirect('/photographers')
