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
 * Complete the 'hourglassSum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

const DIMENSION = 6;
const HOURGLASS_LENGTH = 3;
const MIN = -9;
function hourglassSum(arr: number[][]): number {
  const hourglassAreaLength = DIMENSION - 2;
  const start = 0;
  const end = start + hourglassAreaLength;
  let maxHourglassSum = MIN * 7;

  for (let i = start; i < end; i++) {
    for (let j = start; j < end; j++) {
      const currSum = singleHourglassSum(arr, i, j);
      console.log(currSum);
      if (currSum > maxHourglassSum) {
        maxHourglassSum = currSum;
      }
    }
  }

  return maxHourglassSum;
}

/**
 * Returns the hourglass sum of a 2D array, starting from the upper LH corner x, y
 */
function singleHourglassSum(arr: number[][], x: number, y: number): number {
  let sum = 0;
  for (let i = x; i < x + HOURGLASS_LENGTH; i++) {
    for (let j = y; j < y + HOURGLASS_LENGTH; j++) {
      // Skip middles of hourglass
      if (i === x + 0 && j === y + 1) {
        continue;
      } else if (i === x + 2 && j === y + 1) {
        continue;
      }

      // Otherwise, add value to sum
      const curr = arr[j][i];
      sum += curr;
    }
  }
  return sum;
}

function main() {
  const ws: WriteStream = createWriteStream(process.env['OUTPUT_PATH']);

  let arr: number[][] = Array(6);

  for (let i: number = 0; i < 6; i++) {
    arr[i] = readLine()
      .replace(/\s+$/g, '')
      .split(' ')
      .map((arrTemp) => parseInt(arrTemp, 10));
  }

  const result: number = hourglassSum(arr);

  ws.write(result + '\n');

  ws.end();
}
