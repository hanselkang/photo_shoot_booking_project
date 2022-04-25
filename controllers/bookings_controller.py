from controllers.booking_confrimations_controller import booking_confirmations
from flask import Blueprint, Flask, redirect, render_template, request
from models.booking import Booking

import repositories.client_repository as client_repository
import repositories.booking_repository as booking_repository
import repositories.service_repository as service_repository
import repositories.photographer_repository as photographer_repository

bookings_blueprint = Blueprint("bookings", __name__)

# index


@bookings_blueprint.route("/bookings")
def bookings():
    clients = client_repository.select_all()
    bookings = booking_repository.select_all()
    photographers = photographer_repository.select_all()
    return render_template("bookings/bookings.html", bookings=bookings, clients=clients, photographers=photographers)


# new
@bookings_blueprint.route("/bookings/new")
def new_booking():
    clients = client_repository.select_all()
    services = service_repository.select_all()
    photographers = photographer_repository.select_all()
    return render_template("bookings/new.html", clients=clients, services=services, photographers=photographers)

# create


@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
    name = request.form["name"]
    places = []
    if request.form.get("circuslane"):
        places.append("CircusLane ")
    if request.form.get("deanvillage"):
        places.append("DeanVillage ")
    if request.form.get("newtown"):
        places.append("NewTown ")
    if request.form.get("caltonhill"):
        places.append("CaltonHill ")
    if request.form.get("princesstreet"):
        places.append("PrincesStreetGarden ")
    if request.form.get("oldtown"):
        places.append("OldTown ")
    if request.form.get("grassmarket"):
        places.append("Grassmarket ")
    if request.form.get("holyroodpark"):
        places.append("HolyroodPark ")
    str_places = ''
    for place in places:
        str_places += place
    num_of_group = request.form["num_of_group"]
    photoshoot_start_time = request.form["photoshoot_start_time"]
    photoshoot_end_time = request.form["photoshoot_end_time"]

    client_id = request.form["client_id"]
    service_id = request.form["service_id"]
    photographer_id = request.form["photographer_id"]

    client = client_repository.select(client_id)
    service = service_repository.select(service_id)
    photographer = service_repository.select(photographer_id)
    new_booking = Booking(name, str_places, num_of_group, photoshoot_start_time,
                          photoshoot_end_time, client, service, photographer)
    booking_repository.save(new_booking)
    return redirect("/bookings")

# edit
@bookings_blueprint.route("/bookings/<id>/edit")
def edit_booking(id):
    booking = booking_repository.select(id)
    clients = client_repository.select_all()
    services = service_repository.select_all()
    photographers = photographer_repository.select_all()
    return render_template('bookings/edit.html', booking=booking, clients=clients, services=services, photographers=photographers)


# booking to confirmation form
@bookings_blueprint.route("/bookings/<id>/confirm")
def confirm_booking(id):
    booking = booking_repository.select(id)
    clients = client_repository.select_all()
    services = service_repository.select_all()
    booking_confirmation = booking_repository.select_all
    photographers = photographer_repository.select_all()
    return render_template('bookings/booking_to_confirmation.html', booking=booking, clients=clients, services=services, photographers=photographers, booking_confirmation=booking_confirmation)


# UPDATE
@bookings_blueprint.route("/bookings/<id>", methods=["GET", "POST"])
def update_booking(id):
    name = request.form["name"]
    places = []
    if request.form.get("circuslane"):
        places.append("CircusLane ")
    if request.form.get("deanvillage"):
        places.append("DeanVillage ")
    if request.form.get("newtown"):
        places.append("NewTown ")
    if request.form.get("caltonhill"):
        places.append("CaltonHill ")
    if request.form.get("princesstreet"):
        places.append("PrincesStreetGarden ")
    if request.form.get("oldtown"):
        places.append("OldTown ")
    if request.form.get("grassmarket"):
        places.append("Grassmarket ")
    if request.form.get("holyroodpark"):
        places.append("HolyroodPark ")
    str_places = ''
    for place in places:
        str_places += place
    num_of_group = request.form["num_of_group"]
    photoshoot_start_time = request.form["photoshoot_start_time"]
    photoshoot_end_time = request.form["photoshoot_end_time"]

    client_id = request.form["client_id"]
    service_id = request.form["service_id"]
    photographer_id = request.form["photographer_id"]
    client = client_repository.select(client_id)
    service = service_repository.select(service_id)
    photographer = service_repository.select(photographer_id)

    edit_booking = Booking(name, str_places, num_of_group, photoshoot_start_time,
                           photoshoot_end_time, client.id, service.id, photographer.id, id)
    booking_repository.update(edit_booking)
    return redirect("/bookings")


# delete
@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect('/bookings')


# delete all
# @bookings_blueprint.route("/bookings/delete", methods=['POST'])
# def delete_all_booking():
#     booking_repository.delete_all()
#     return redirect('/bookings')
