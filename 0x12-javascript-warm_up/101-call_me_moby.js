#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let me = 0; me < x; me++) theFunction();
};
