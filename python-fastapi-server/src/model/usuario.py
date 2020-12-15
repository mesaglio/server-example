from pydantic import BaseModel


class Usuario(BaseModel):
    documento: str
    username: str
    nombres: str
    apellidos: str
    genero: str
    fechaNacimiento: str

    def __eq__(self, other):
        self.__dict__.get('username') == other.get('username')
