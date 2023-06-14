#!/usr/bin/node

// A script that print arguments based on there number

const myVar = process.argv.length;
if (myVar > 3) {
  console.log('Arguments found');
} else if (myVar === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
