from flask import Blueprint, Flask, redirect, render_template, request
from models.service import Service

import repositories.service_repository as service_repository

services_blueprint = Blueprint("services",__name__)


@services_blueprint.route("/services")
def services():
    services = service_repository.select_all()
    return render_template("services/services.html", services=services)
