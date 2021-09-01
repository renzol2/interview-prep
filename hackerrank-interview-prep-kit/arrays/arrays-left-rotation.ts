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
 * Complete the 'rotLeft' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY a
 *  2. INTEGER d
 */

function rotLeft(a: number[], d: number): number[] {
  // Write your code here
  const numRotations = d % a.length;
  if (numRotations === 0) return a;

  const rotated: number[] = new Array(a.length);

  for (let i = 0; i < a.length; i++) {
    let newIndex = i - numRotations;
    if (newIndex < 0) newIndex += a.length;
    rotated[newIndex] = a[i];
  }

  return rotated;
}

function main() {
  const ws: WriteStream = createWriteStream(process.env['OUTPUT_PATH']);

  const firstMultipleInput: string[] = readLine()
    .replace(/\s+$/g, '')
    .split(' ');

  const n: number = parseInt(firstMultipleInput[0], 10);

  const d: number = parseInt(firstMultipleInput[1], 10);

  const a: number[] = readLine()
    .replace(/\s+$/g, '')
    .split(' ')
    .map((aTemp) => parseInt(aTemp, 10));

  const result: number[] = rotLeft(a, d);

  ws.write(result.join(' ') + '\n');

  ws.end();
}
