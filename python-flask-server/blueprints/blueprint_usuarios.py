from models.usuario import Usuario
from flask import request, Blueprint, jsonify

usuarios = []

usuarios_blueprint = Blueprint("usuarios", __name__)


@usuarios_blueprint.route('/', methods=['POST'])
def crear_usuario():
    try:
        body = Usuario(request.json)
        usuarios.append(body)
        return '', 201
    except Exception as e:
        return '', 400


@usuarios_blueprint.route('/', methods=['GET'])
def obtener_usuarios():
    return jsonify([o.__dict__ for o in usuarios]), 200


@usuarios_blueprint.route('/<username>', methods=['GET'])
def obtener_usuario_by_username(username):
    index = get_index_of_user(username)
    if index != -1:
        return jsonify(usuarios[index].__dict__), 200
    return '', 404


@usuarios_blueprint.route('/<username>', methods=['PATCH'])
def actualizar_usuario_by_username(username):
    body = Usuario(request.json)
    if get_index_of_user(username) != -1:
        delete_user_by_username(username)
        usuarios.append(body)
        return '', 200
    return '', 404


@usuarios_blueprint.route('/<username>', methods=['DELETE'])
def eliminar_usuario_by_username(username):
    delete_user_by_username(username)
    return '', 200


# AUXILIAR
def get_index_of_user(username: str):
    index = 0
    for _user in usuarios:
        if _user.username == username:
            return index
        index += 1
    return -1


def delete_user_by_username(username: str):
    index = get_index_of_user(username)
    if index != -1:
        usuarios.pop(index)
