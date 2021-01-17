import flask
from blueprints.blueprint_ping import ping_blueprint
from blueprints.blueprint_usuarios import usuarios_blueprint
from models.usuario import JSONEncoder

ACTIVE_ENDPOINTS = [("/", ping_blueprint), ('/usuarios', usuarios_blueprint)]


def create_app():
    app = flask.Flask(__name__)

    app.url_map.strict_slashes = False

    for url, blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)

    app.json_encoder = JSONEncoder
    return app
