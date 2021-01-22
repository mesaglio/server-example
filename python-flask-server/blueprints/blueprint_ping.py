from flask import Blueprint

ping_blueprint = Blueprint("ping", __name__)


@ping_blueprint.route("/ping", methods=['GET'])
def ping():
    return "Pong", 200
