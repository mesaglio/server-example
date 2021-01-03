import falcon
from wsgiref import simple_server
from router.Ping import Ping
from router.Users import Users


def map_routes(_api):
    _api.add_route('/ping', Ping())
    _api.add_route('/usuarios', Users())
    _api.add_route('/usuarios/{username}', Users())


if __name__ == '__main__':
    api = falcon.API()
    map_routes(api)
    print("Listening ...")
    httpd = simple_server.make_server('0.0.0.0', 8000, api)
    httpd.serve_forever()
