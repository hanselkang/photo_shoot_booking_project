from flask import Blueprint, Flask, redirect, render_template, request
from models.client import Client
import repositories.client_repository as client_repository

clients_blueprint = Blueprint("clients",__name__)

# index


@clients_blueprint.route("/main")
def clients_index():
    return render_template("client_index.html", clients=clients)

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


# new_then_booking
@clients_blueprint.route("/clients/new_client_byc")
def new_for_client():
    clients = client_repository.select_all()
    return render_template("clients/new_for_client.html", clients=clients)

# create
@clients_blueprint.route("/clients", methods=["POST"])
def create_client():
    name = request.form["name"]
    client_from = request.form["client_from"]
    email = request.form["email"]
    birthdate = request.form["birthdate"]
    contact = request.form["contact"]
    new_client = Client(name, client_from, email, birthdate,
                        contact)
    client_repository.save(new_client)
    return redirect("/clients")

# create from clients


@clients_blueprint.route("/new_byc", methods=["POST"])
def create_from_client():
    name = request.form["name"]
    client_from = request.form["client_from"]
    email = request.form["email"]
    birthdate = request.form["birthdate"]
    contact = request.form["contact"]
    new_client = Client(name, client_from, email, birthdate,
                        contact)
    client_repository.save(new_client)
    return redirect("/bookings/clients_booking_list")

# edit
@clients_blueprint.route("/clients/<id>/edit")
def edit_client(id):
    client = client_repository.select(id)
    return render_template('clients/edit.html', client=client)

# update
@clients_blueprint.route("/clients/<id>", methods=["GET","POST"])
def update_client(id):
    name = request.form["name"]
    client_from = request.form["client_from"]
    email = request.form["email"]
    birthdate = request.form["birthdate"]
    contact = request.form["contact"]
    edit_client = Client(name, client_from, email, birthdate,
                        contact, id)
    client_repository.update(edit_client)
    return redirect("/clients")

# delete
@clients_blueprint.route("/clients/<id>/delete", methods=['POST'])
def delete_client(id):
    client_repository.delete(id)
    return redirect('/clients')