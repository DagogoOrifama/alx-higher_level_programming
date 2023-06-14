#!/usr/bin/node
const zoom = Math.floor(Number(process.argv[2]));
console.log(isNaN(zoom) ? 'Not a number' : `My number: ${zoom}`);
