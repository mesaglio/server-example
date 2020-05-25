'use strict';

var utils = require('../utils/writer.js');
var Usuarios = require('../service/UsuariosService');

module.exports.actualizarUsuarioByUsername = function actualizarUsuarioByUsername (req, res, next, body, username) {
  Usuarios.actualizarUsuarioByUsername(body, username)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.crearUsuario = function crearUsuario (req, res, next, body) {
  Usuarios.crearUsuario(body)
    .then(function (response) {
      console.log(req.body());
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.eliminarUsuarioByUsername = function eliminarUsuarioByUsername (req, res, next, username) {
  Usuarios.eliminarUsuarioByUsername(username)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.obtenerUsuarioByUsername = function obtenerUsuarioByUsername (req, res, next, username) {
  Usuarios.obtenerUsuarioByUsername(username)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.obtenerUsuarios = function obtenerUsuarios (req, res, next) {
  Usuarios.obtenerUsuarios()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
