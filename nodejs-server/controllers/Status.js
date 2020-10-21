'use strict';

var utils = require('../utils/writer.js');
var Status = require('../service/StatusService');

module.exports.ping = function ping(req, res, next) {
  Status.ping()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
