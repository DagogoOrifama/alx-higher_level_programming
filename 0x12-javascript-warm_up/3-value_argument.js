#!/usr/bin/node

// printing arguments

const myVar = process.argv;
if (myVar[2] !== undefined) {
  console.log(myVar[2]);
} else {
  console.log('No argument');
}
