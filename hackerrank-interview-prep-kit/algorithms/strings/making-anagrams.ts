'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function (inputStdin) {
  inputString += inputStdin;
});

process.stdin.on('end', function () {
  inputString = inputString.split('\n');

  main();
});

function readLine() {
  return inputString[currentLine++];
}

/*
 * Complete the 'makeAnagram' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. STRING a
 *  2. STRING b
 */

function makeAnagram(a, b) {
  // Write your code here
  const storage = {};
  for (const c of a) {
    if (storage[c] === undefined) storage[c] = 0;
    storage[c] += 1;
  }

  for (const c of b) {
    if (storage[c] === undefined) storage[c] = 0;
    storage[c] -= 1;
  }

  let chars = 0;
  for (const c of Object.keys(storage)) {
    chars += Math.abs(storage[c]);
  }
  return chars;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const a = readLine();

  const b = readLine();

  const res = makeAnagram(a, b);

  ws.write(res + '\n');

  ws.end();
}
