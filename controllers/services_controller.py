from flask import Blueprint, Flask, redirect, render_template, request
from models.service import Service

import repositories.service_repository as service_repository
import repositories.photographer_repository as photographer_repository

services_blueprint = Blueprint("services",__name__)


@services_blueprint.route("/services")
def services():
    services = service_repository.select_all()
    return render_template("services/services.html", services=services)


# new
@services_blueprint.route("/services/new")
def new_service():
    photographers = photographer_repository.select_all()
    return render_template("services/new.html", photographers=photographers)

# creat


@services_blueprint.route("/services", methods=["POST"])
def create_service():
    photo_type = request.form["photo_type"]
    hours = request.form["hours"]
    price = request.form["price"]
    
    photographer_id = request.form["photographer_id"]

    photographer = photographer_repository.select(photographer_id)

    new_service = Service(photo_type, hours, price, photographer.id)
    service_repository.save(new_service)
    return redirect("/services")
