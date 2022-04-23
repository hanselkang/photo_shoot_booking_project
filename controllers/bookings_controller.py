from flask import Blueprint, Flask, redirect, render_template, request
from models.booking import Booking
from models.client import Client

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
    return render_template("bookings/bookings.html", bookings=bookings, clients=clients)

# new
@bookings_blueprint.route("/bookings/new")
def new_booking():
    clients = client_repository.select_all()
    services = service_repository.select_all()
    photographers = photographer_repository.select_all()
    return render_template("bookings/new.html", clients=clients, services=services, photographers=photographers)

# creat
@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
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
    photographer = photographer_repository.select(photographer_id)

    new_booking = Booking(name, address, num_of_group, photoshoot_start_time,
                          photoshoot_end_time, client.id, service.id, photographer.id)
    booking_repository.save(new_booking)
    return redirect("/bookings")
