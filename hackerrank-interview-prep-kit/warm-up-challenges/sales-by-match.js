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
 * Complete the 'sockMerchant' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER_ARRAY ar
 */

function sockMerchant(n, ar) {
  // Count number of socks
  const sockCount = {};
  for (const sock of ar) {
    if (sockCount[sock] === undefined) {
      sockCount[sock] = 0;
    }
    sockCount[sock] += 1;
  }

  // Count number of pairs
  let pairs = 0;
  for (const sock of Object.keys(sockCount)) {
    pairs += Math.floor(sockCount[sock] / 2);
  }
  return pairs;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const n = parseInt(readLine().trim(), 10);

  const ar = readLine()
    .replace(/\s+$/g, '')
    .split(' ')
    .map((arTemp) => parseInt(arTemp, 10));

  const result = sockMerchant(n, ar);

  ws.write(result + '\n');

  ws.end();
}
