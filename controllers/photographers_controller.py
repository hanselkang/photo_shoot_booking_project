from flask import Blueprint, Flask, redirect, render_template, request
from models.photographer import Photographer

import repositories.photographer_repository as photographer_repository

photographers_blueprint = Blueprint("photographers",__name__)


@photographers_blueprint.route("/photographers")
def photographers():
    photographers = photographer_repository.select_all()
    return render_template("photographers/photographers.html",photographers=photographers)
