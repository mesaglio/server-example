import connexion
from flask_api import status
from swagger_server.models.usuario import Usuario

usuarios = []
def actualizar_usuario_by_username(body, username):
    body = Usuario.from_dict(connexion.request.get_json())
    if get_index_of_user(username) != -1:
        delete_user_by_username(username)
        usuarios.append(body)
        return 'Success',status.HTTP_200_OK
    return 'Not found',status.HTTP_404_NOT_FOUND


def crear_usuario(body):
    body = Usuario.from_dict(connexion.request.get_json())
    usuarios.append(body)
    return 'Success',status.HTTP_201_CREATED


def eliminar_usuario_by_username(username):
    delete_user_by_username(username)
    return 'Success',status.HTTP_200_OK


def obtener_usuario_by_username(username):
    index = get_index_of_user(username)
    if index != -1:
        return usuarios[index],status.HTTP_200_OK
    return 'User not found',status.HTTP_404_NOT_FOUND

def obtener_usuarios():
    return usuarios


# AUXILIAR
def get_index_of_user(username : str):
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