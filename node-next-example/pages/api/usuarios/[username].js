var _ = require('lodash')
var _usuarios = require("../usuarios.js")
var usuarios = _usuarios.usuarios;

export default (req, res) => {
    const {
        query: { username },
    } = req
    if (req.method === 'GET') {
        var index = getUserIndex(username)
        if (index == -1) {
            res.statusCode = 404
            res.end()
        } else {
            res.json(usuarios[index])
            res.end()
        }
    }
    if (req.method === 'DELETE') {
        var index = getUserIndex(username)
        if (index == -1) {
            res.end()
        } else {
            deleteUser(username)
            res.end(usuarios[index])
        }
    }
    if (req.method === 'PATCH') {
        var index = getUserIndex(username)
        if (index == -1) {
            res.statusCode = 404
            res.end()
        } else {
            var user = _usuarios.getUserFromBody(req)
            if (_usuarios.haveAllProps(user)) {
                deleteUser(username)
                usuarios.push(user)
                res.statusCode = 200
                res.end()
            } else {
                res.statusCode = 400
                res.end()
            }
        }
    }
}

function getUserIndex(username) {
    var index = _.findIndex(usuarios, { 'username': username })
    return index
}

function deleteUser(username) {
    _.remove(usuarios, { 'username': username })
}