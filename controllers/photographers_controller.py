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

# creat


@photographers_blueprint.route("/photographers", methods=["POST"])
def create_photographer():
    name = request.form["name"]
    email = request.form["email"]
    portfolio_address = request.form["portfolio_address"]
    new_photographer = Photographer(name, email,
                                    portfolio_address)
    photographer_repository.save(new_photographer)
    return redirect("/photographers")
