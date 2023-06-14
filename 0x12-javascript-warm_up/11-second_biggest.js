#!/usr/bin/node

const args = process.argv.slice(2); // Get the list of arguments, excluding the first two (node and script path)

// Check if no argument is passed or only one argument is provided
if (args.length === 0) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  const numbers = args.map(Number); // Convert arguments to numbers
  const sortedNumbers = numbers.sort((a, b) => b - a); // Sort numbers in descending order
  const secondLargest = sortedNumbers[1]; // Get the second element in the sorted list

  console.log(secondLargest);
}
