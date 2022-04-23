from flask import Blueprint, Flask, redirect, render_template, request
from models.client import Client

import repositories.client_repository as client_repository

clients_blueprint = Blueprint("clients",__name__)

# index
@clients_blueprint.route("/clients")
def clients():
    clients = client_repository.select_all()
    return render_template("clients/clients.html", clients=clients)


# new
@clients_blueprint.route("/clients/new")
def new_client():
    clients = client_repository.select_all()
    return render_template("clients/new.html", clients=clients)

# creat
@clients_blueprint.route("/clients", methods=["POST"])
def create_client():
    name = request.form["name"]
    client_from = request.form["client_from"]
    email = request.form["email"]
    age = request.form["age"]
    contact = request.form["contact"]
    new_client = Client(name, client_from, email, age,
                        contact)
    client_repository.save(new_client)
    return redirect("/clients")
