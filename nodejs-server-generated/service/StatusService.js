'use strict';


/**
 * ping
 *
 * returns String
 **/
exports.ping = function() {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = "Pong";
    if (Object.keys(examples).length >= 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}

