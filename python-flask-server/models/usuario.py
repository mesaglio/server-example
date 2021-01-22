from json import JSONEncoder


class Usuario:
    def __init__(self, data):
        self.username = data['username']
        self.documento = data['documento']
        self.nombres = data['nombres']
        self.apellidos = data['apellidos']
        self.genero = data['genero']
        self.fecha_nacimiento = data['fechaNacimiento']
