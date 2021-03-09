from flask_restx import Api
from namespaces.ping import ping_ns


api = Api(
    title="Flask_restx API",
    version="1.0",
    description="testing",
)
api.add_namespace(ping_ns)
