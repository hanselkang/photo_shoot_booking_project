from flask import Blueprint, Flask, redirect, render_template, request
from models.service import Service

import repositories.service_repository as service_repository
import repositories.photographer_repository as photographer_repository

services_blueprint = Blueprint("services",__name__)


@services_blueprint.route("/services")
def services():
    services = service_repository.select_all()
    return render_template("services/services.html", services=services)

# index for clients


@services_blueprint.route("/service_public")
def services_public():
    services = service_repository.select_all()
    return render_template("services/services_public.html", services=services)

# new
@services_blueprint.route("/services/new")
def new_service():
    photographers = photographer_repository.select_all()
    return render_template("services/new.html")

# create
@services_blueprint.route("/services", methods=["POST"])
def create_service():
    photo_type = request.form["photo_type"]
    hours = request.form["hours"]
    price = request.form["price"]
    new_service = Service(photo_type, hours, price)
    service_repository.save(new_service)
    return redirect("/services")

# edit
@services_blueprint.route("/services/<id>/edit")
def edit_service(id):
    service = service_repository.select(id)
    return render_template('services/edit.html', service=service)

# update
@services_blueprint.route("/services/<id>", methods=["GET","POST"])
def update_service(id):
    photo_type = request.form["photo_type"]
    hours = request.form["hours"]
    price = request.form["price"]
    edit_service = Service(photo_type, hours, price, id)
    service_repository.update(edit_service)
    return redirect("/services")

# @services_blueprint.route("/photographer/<id>")
# def list_clients(id):
#     clients = photographer_repository.select_clients_by_photographer(id)
#     service = service_repository.select(id)

#     return render_template("photographers/client_list.html", clients=clients, service=service)

# delete
@services_blueprint.route("/services/<id>/delete", methods=['POST'])
def delete_service(id):
    service_repository.delete(id)
    return redirect('/services')
