#!/usr/bin/node

// printing 2 arguments

const myVar = process.argv;
if (myVar[2] !== undefined && myVar[3] !== undefined) {
  console.log(myVar[2] + ' is ' + myVar[3]);
} else if (myVar[3] === undefined && myVar[2] !== undefined) {
  console.log(myVar[2] + ' is ' + myVar[3]);
} else {
  console.log('undefined is undefined');
}
