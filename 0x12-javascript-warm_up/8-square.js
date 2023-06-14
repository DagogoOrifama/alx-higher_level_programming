#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let me = 0; me < size; me++) {
    let col = '';
    for (let h = 0; h < size; h++) col += 'X';
    console.log(col);
  }
}
