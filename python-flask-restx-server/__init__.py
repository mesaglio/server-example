import json
from flask import Flask

from namespaces.__init__ import api


def create_app():
    app = Flask(__name__)

    # accepts both /endpoint and /endpoint/ as valid URLs
    app.url_map.strict_slashes = False

    api.init_app(app)

    return app
