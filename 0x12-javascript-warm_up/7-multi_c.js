#!/usr/bin/node
const x = process.argv[2];
if (!isNaN(parseInt(x))) {
  const numAppears = parseInt(x);
  let count = 0;
  while (count < numAppears) {
    console.log('C is fun');
    count++;
  }
} else {
  console.log('Missing number of occurrences');
}
