from flask import Blueprint, request, app, g
import json

from utils import dale_pepe_hace_lo_tuyo
from utils.decoretaors import log_enpoint_information

ping_blueprint = Blueprint("ping", __name__)


@ping_blueprint.route("/ping", methods=["GET"])
@log_enpoint_information
def ping():
    return "Pong", 200
