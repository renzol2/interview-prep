'use strict';

import { WriteStream, createWriteStream } from 'fs';
process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString: string = '';
let inputLines: string[] = [];
let currentLine: number = 0;

process.stdin.on('data', function (inputStdin: string): void {
  inputString += inputStdin;
});

process.stdin.on('end', function (): void {
  inputLines = inputString.split('\n');
  inputString = '';

  main();
});

function readLine(): string {
  return inputLines[currentLine++];
}

/*
 * Complete the 'arrayManipulation' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. 2D_INTEGER_ARRAY queries
 */

function arrayManipulation(n: number, queries: number[][]): number {
  const nums: number[] = [...Array(n)].fill(0);
  for (const [start, end, val] of queries) {
    nums[start - 1] += val;
    nums[end] -= val;
  }

  let max = 0;
  let accumulated = 0;
  for (const n of nums) {
    if (isNaN(n)) continue;
    accumulated += n;
    max = Math.max(accumulated, max);
  }
  return max;
}

function main() {
  const ws: WriteStream = createWriteStream(process.env['OUTPUT_PATH']);

  const firstMultipleInput: string[] = readLine()
    .replace(/\s+$/g, '')
    .split(' ');

  const n: number = parseInt(firstMultipleInput[0], 10);

  const m: number = parseInt(firstMultipleInput[1], 10);

  let queries: number[][] = Array(m);

  for (let i: number = 0; i < m; i++) {
    queries[i] = readLine()
      .replace(/\s+$/g, '')
      .split(' ')
      .map((queriesTemp) => parseInt(queriesTemp, 10));
  }

  const result: number = arrayManipulation(n, queries);

  ws.write(result + '\n');

  ws.end();
}
