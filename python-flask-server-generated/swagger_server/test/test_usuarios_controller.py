# coding: utf-8

from __future__ import absolute_import

from flask import json

from swagger_server.models.usuario import Usuario  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUsuariosController(BaseTestCase):

    def test_actualizar_usuario_by_username(self):
        body = Usuario()
        response = self.client.open(
            '/usuarios/{username}'.format(username='username_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_crear_usuario(self):
        body = Usuario()
        response = self.client.open(
            '/usuarios',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert201(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_eliminar_usuario_by_username(self):
        response = self.client.open(
            '/usuarios/{username}'.format(username='username_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_obtener_usuario_by_username(self):
        response = self.client.open(
            '/usuarios/{username}'.format(username='username_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_obtener_usuarios(self):
        response = self.client.open(
            '/usuarios',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
