#!/usr/bin/node

function computeFactorial(num) {
  if (isNaN(num)) {
    return 1;
  } else if (num === 0) {
    return 1;
  } else {
    return num * computeFactorial(num - 1);
  }
}

const num = parseInt(process.argv[2]); // Get the integer argument from command line

console.log(computeFactorial(num));

