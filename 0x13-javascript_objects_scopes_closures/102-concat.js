#!/usr/bin/node
const fs = require('fs');

const sourceFile1 = process.argv[2]; // File path of the first source file
const sourceFile2 = process.argv[3]; // File path of the second source file
const destinationFile = process.argv[4]; // File path of the destination file

// Read the contents of the first source file
fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) {
    console.error('Error reading the first source file:', err);
    return;
  }

  // Read the contents of the second source file
  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) {
      console.error('Error reading the second source file:', err);
      return;
    }

    // Concatenate the contents of the two source files
    const concatenatedData = data1 + data2;

    // Write the concatenated data to the destination file
    fs.writeFile(destinationFile, concatenatedData, 'utf8', (err) => {
      if (err) {
        console.error('Error writing to the destination file:', err);
        return;
      }

      console.log('Files concatenated successfully.');
    });
  });
});
