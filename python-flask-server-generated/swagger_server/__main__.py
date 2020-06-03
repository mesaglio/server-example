import connexion

from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'ABM de Usuarios'}, pythonic_params=True,options={"swagger_ui": False})
    app.run(port=8080)


if __name__ == '__main__':
    main()
