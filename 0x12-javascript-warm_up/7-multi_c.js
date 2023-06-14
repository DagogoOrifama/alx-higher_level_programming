#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let me = 0; me < x; me++) {
    console.log('C is fun');
  }
}
