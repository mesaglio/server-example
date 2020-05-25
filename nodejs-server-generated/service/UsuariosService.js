'use strict';
const _ = require('lodash');

var users = [];
/**
 * Actualizar usuario por username
 *
 * body Usuario Usuario
 * username String 
 * returns Usuario
 **/
exports.actualizarUsuarioByUsername = function(body,username) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    var usuario = obtenerUsuarioPorUsername(username);
    if (usuario === -1) {
      examples['error'] = 'Usuario no ecnonctrado.';
      reject(examples);
    };
    var indice = _.findIndex(users, { 'username': username });
    users[indice] = body;
    examples['application/json'] = users[indice];
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Crear usuario
 *
 * body Usuario Usuario
 * no response value expected for this operation
 **/
exports.crearUsuario = function(body) {
  return new Promise(function (resolve, reject) {
    users.push(body);
    resolve();
  });
}


/**
 * Eliminar usuario por username
 *
 * username String 
 * no response value expected for this operation
 **/
exports.eliminarUsuarioByUsername = function(username) {
  return new Promise(function (resolve, reject) {
    var usuario = obtenerUsuarioPorUsername(username);
    if (usuario === -1) {
      examples['error'] = 'Usuario no ecnonctrado.';
      reject(examples);
    }
    users = _.remove(users, function (user) {
      user.username === username;
    });
    resolve();
  });
}


/**
 * Obtener usuario por username
 *
 * username String 
 * returns Usuario
 **/
exports.obtenerUsuarioByUsername = function(username) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    var usuario = obtenerUsuarioPorUsername(username);
    if (usuario === -1) {
      examples['error'] = 'Usuario no ecnonctrado.';
      reject(examples);
    }
    examples['application/json'] = usuario;
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Todos los usuario
 *
 * returns List
 **/
exports.obtenerUsuarios = function() {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = users;
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}

function obtenerUsuarioPorUsername(username) {
  var index = _.findIndex(users, { 'username': username })
  if (index != -1) {
    return users[index];
  }
  return -1;
}