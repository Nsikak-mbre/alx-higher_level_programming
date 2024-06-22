#!/usr/bin/node
const args = process.argv;
if (args[2] === undefined || args[3] === undefined) {
  process.exit();
}
console.log(args[2], 'is', args[3]);
