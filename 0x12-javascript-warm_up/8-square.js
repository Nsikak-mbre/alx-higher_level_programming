#!/usr/bin/node
const size = parseInt(process.argv[2], 10);
if (isNaN(size) || size <= 0) {
  console.log('Missing size');
  process.exit(1);
}
for (let count = 0; count < size; count++) {
  let row = '';
  for (let col = 0; col < size; col++) {
    row += 'X';
  }
  console.log(row);
}
