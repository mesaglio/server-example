import falcon
from models.Usuario import Usuario
import json


class Users:
    users = []

    def on_post(self, req, res):
        user = req.media
        if not Usuario.validate_dict(user):
            res.status = falcon.HTTP_400
        else:
            self.users.append(self.body_to_user(user))
            res.status = falcon.HTTP_201

    def on_get(self, req, res, username=None):
        if username:
            user = self.find_user_by_username(username)
            if user:
                res.body = json.dumps(user, default=lambda o: o.encode(), indent=4)
            else:
                res.status = falcon.HTTP_404
        else:
            res.body = json.dumps(self.users, default=lambda o: o.encode(), indent=4)

    def on_delete(self, req, res, username=None):
        if not username:
            res.status = falcon.HTTP_200
        else:
            self.remove_user_by_username(username)

    def on_patch(self, req, res, username=None):
        user = req.media
        if not username:
            res.status = falcon.HTTP_404
        elif not Usuario.validate_dict(user):
            res.status = falcon.HTTP_400
        else:
            self.update_user(username, self.body_to_user(user))

    def find_user_by_username(self, username: str):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def remove_user_by_username(self, username: str):
        for user in self.users:
            if user.username == username:
                self.users.remove(user)

    def update_user(self, username, new_user: Usuario):
        for user in self.users:
            if user.username == username:
                user.documento = new_user.documento
                user.nombres = new_user.nombres
                user.apellidos = new_user.apellidos
                user.genero = new_user.genero
                user.fechaNacimiento = new_user.fechaNacimiento

    @staticmethod
    def body_to_user(user):
        return Usuario(user['username'], user['documento'], user['nombres'], user['apellidos'], user['genero'],
                       user['fechaNacimiento'])
