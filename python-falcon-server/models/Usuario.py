class Usuario:

    def __init__(self, _username, _docuemnto, _nombres, _apellidos, _genero, _fechaNacimiento):
        self.username = _username
        self.documento = _docuemnto
        self.nombres = _nombres
        self.apellidos = _apellidos
        self.genero = _genero
        self.fechaNacimiento = _fechaNacimiento

    @staticmethod
    def validate_dict(obj):
        return all(['username' in obj, 'documento' in obj, 'nombres' in obj, 'apellidos' in obj, 'genero' in obj,
                    'fechaNacimiento' in obj])

    def encode(self):
        return self.__dict__
