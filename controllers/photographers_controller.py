from flask import Blueprint, Flask, redirect, render_template, request
from models.photographer import Photographer
import repositories.photographer_repository as photographer_repository
import repositories.client_repository as client_repository

photographers_blueprint = Blueprint("photographers", __name__)


# to password
@photographers_blueprint.route("/sign_in")
def photographers_sign_in():
    return render_template("photographer_index.html")



# index
@photographers_blueprint.route("/photographers")
def photographers():
    photographers = photographer_repository.select_all()
    return render_template("photographers/photographers.html", photographers=photographers)


# index for client
@photographers_blueprint.route("/photographers_client")
def photographers_client():
    photographers = photographer_repository.select_all()
    return render_template("photographers/photographers_client.html", photographers=photographers)

# show list of clients, services

@photographers_blueprint.route("/photographers/<id>")
def show_photographer(id):
    clients = photographer_repository.select_clients_of_photographer(id)
    services = photographer_repository.select_service_of_photographer(id)
    photographer = photographer_repository.select(id)
    return render_template("photographers/client_list.html", clients=clients, services=services, photographer=photographer)


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
