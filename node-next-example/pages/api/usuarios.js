import { every, functions } from "lodash"

var usuarios = [];
var _ = require('lodash')
function handler(req, res) {
    if (usuarios === undefined) {
        usuarios = []
    }
    if (req.method === 'GET') {
        res.json(usuarios)
        res.end()
    }
    if (req.method === 'POST') {
        var user = getUserFromBody(req)
        if (haveAllProps(user)) {
            usuarios.push(user)
            res.statusCode = 201
            res.end()
        } else {
            res.statusCode = 400
            res.end()
        }
    } else {
        res.statusCode = 404
        res.end()
    }

}

function haveAllProps(user) {
    return _.values(user).every((prop) => { return prop !== undefined })
}

function getUserFromBody(req) {
    var { username, documento, nombres, apellidos, genero, fechaNacimiento } = req.body
    return {
        'username': username,
        'documento': documento,
        'nombres': nombres,
        'apellidos': apellidos,
        'genero': genero,
        'fechaNacimiento': fechaNacimiento
    }
}
module.exports = {
    default: handler,
    usuarios: usuarios,
    haveAllProps: haveAllProps,
    getUserFromBody: getUserFromBody
}