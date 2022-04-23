from flask import Blueprint, Flask, redirect, render_template, request
from models.booking import Booking
from models.client import Client

import repositories.client_repository as client_repository
import repositories.booking_repository as booking_repository

bookings_blueprint = Blueprint("bookings", __name__)


@bookings_blueprint.route("/bookings")
def bookings():
    clients = client_repository.select_all()
    bookings = booking_repository.select_all()
    return render_template("bookings/bookings.html", bookings=bookings, clients=clients)
