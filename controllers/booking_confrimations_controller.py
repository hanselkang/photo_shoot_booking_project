from flask import Blueprint, Flask, redirect, render_template, request
from models.booking_confirmation import BookingConfirmation

import repositories.client_repository as client_repository
import repositories.booking_confirmation_repository as booking_confirmation_repository
import repositories.service_repository as service_repository
import repositories.photographer_repository as photographer_repository

booking_confirmations_blueprint = Blueprint("booking_confirmations", __name__)

# index

@booking_confirmations_blueprint.route("/booking_confirmations")
def booking_confirmations():
    clients = client_repository.select_all()
    booking_confirmations = booking_confirmation_repository.select_all()
    photographers = photographer_repository.select_all()
    return render_template("booking_confirmations/booking_confirmations.html", booking_confirmations=booking_confirmations, clients=clients, photographers=photographers)

# client index
@booking_confirmations_blueprint.route("/bookings/clients_booking_list")
def bookings_list_for_clients():
    clients = client_repository.select_all()
    booking_confirmations = booking_confirmation_repository.select_all()
    photographers = photographer_repository.select_all()
    hidden_part = '***'
    return render_template("bookings/clients_see_booking_list.html", booking_confirmations=booking_confirmations, clients=clients, photographers=photographers, hidden_part = hidden_part)
    

# new
@booking_confirmations_blueprint.route("/booking_confirmations/new")
def new_booking_confirmation():
    clients = client_repository.select_all()
    services = service_repository.select_all()
    photographers = photographer_repository.select_all()
    return render_template("booking_confirmations/new.html", clients=clients, services=services, photographers=photographers)
    
    
# create
@booking_confirmations_blueprint.route("/booking_confirmations", methods=["POST"])
def create_booking_confirmation():
    name = request.form["name"]
    address = request.form["address"]
    num_of_group = request.form["num_of_group"]
    photoshoot_start_time = request.form["photoshoot_start_time"]
    photoshoot_end_time = request.form["photoshoot_end_time"]

    client_id = request.form["client_id"]
    service_id = request.form["service_id"]
    photographer_id = request.form["photographer_id"]

    client = client_repository.select(client_id)
    service = service_repository.select(service_id)
    photographer = service_repository.select(photographer_id)

    new_booking_confirmation = BookingConfirmation(name, address, num_of_group, photoshoot_start_time,
                          photoshoot_end_time, client, service, photographer)
    booking_confirmation_repository.save(new_booking_confirmation)
    return redirect("/booking_confirmations")

# edit
@booking_confirmations_blueprint.route("/booking_confirmations/<id>/edit")
def edit_booking_confirmation(id):
    booking_confirmation = booking_confirmation_repository.select(id)
    clients = client_repository.select_all()
    services = service_repository.select_all()
    photographers = photographer_repository.select_all()
    return render_template('booking_confirmations/edit.html', booking_confirmation=booking_confirmation, clients=clients, services = services, photographers= photographers)

# UPDATE
@booking_confirmations_blueprint.route("/booking_confirmations/<id>", methods=["GET", "POST"])
def update_booking_confirmation(id):
    name = request.form["name"]
    address = request.form["address"]
    num_of_group = request.form["num_of_group"]
    photoshoot_start_time = request.form["photoshoot_start_time"]
    photoshoot_end_time = request.form["photoshoot_end_time"]

    client_id = request.form["client_id"]
    service_id = request.form["service_id"]
    photographer_id = request.form["photographer_id"]

    client = client_repository.select(client_id)
    service = service_repository.select(service_id)
    photographer = service_repository.select(photographer_id)

    edit_booking_confirmation = BookingConfirmation(name, address, num_of_group, photoshoot_start_time,
                          photoshoot_end_time, client.id, service.id, photographer.id, id)
    booking_confirmation_repository.update(edit_booking_confirmation)
    return redirect("/booking_confirmations")


# delete 
@booking_confirmations_blueprint.route("/booking_confirmations/<id>/delete", methods=['POST'])
def delete_booking_confirmation(id):
    booking_confirmation_repository.delete(id)
    return redirect('/booking_confirmations')


# delete all
# @booking_confirmations_blueprint.route("/booking_confirmations/delete", methods=['POST'])
# def delete_all_booking_confirmation():
#     booking_confirmation_repository.delete_all()
#     return redirect('/booking_confirmations')
