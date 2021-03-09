from flask_restx import Namespace, Resource


ping_ns = Namespace("ping", description="API Health check endpoint")


@ping_ns.route("/")
class Ping(Resource):
    def get(self):
        return "pong", 200
