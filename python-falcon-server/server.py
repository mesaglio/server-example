import falcon


class Ping:
    def on_get(self,req,res):
        res.body = 'Pong'
        res.status = falcon.HTTP_200

class Users:
    users = []

    def on_post(self,req,res):
        res.body = 'Pong'
        res.status = falcon.HTTP_200

    def on_get(self,req,res):
        res.media = self.users

    def on_delete(self,req,res):
        res.body = 'delete'

def map_routes(api):
    api.add_route('/ping',Ping())
    api.add_route('/usuarios',Users())

api = falcon.API()
map_routes(api)
#gunicorn server:api --reload
