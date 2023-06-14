#!/usr/bin/node
const fs = require('fs');
const as = fs.readFileSync(process.argv[2], 'utf8');
const bs = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], as + bs);
