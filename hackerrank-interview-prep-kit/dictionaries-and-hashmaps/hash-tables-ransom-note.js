'use strict';

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

function createWordMap(strArray) {
  const map = {};
  for (const word of strArray) {
    if (map[word] === undefined) {
      map[word] = 0;
    }
    map[word] += 1;
  }
  return map;
}

/*
 * Complete the 'checkMagazine' function below.
 *
 * The function accepts following parameters:
 *  1. STRING_ARRAY magazine
 *  2. STRING_ARRAY note
 */
function checkMagazine(magazine, note) {
  // print Yes if he can replicate his ransom note exactly using whole words from the magazine
  // otherwise, print No.
  if (note.length > magazine.length) {
    console.log('No');
    return;
  }

  const magazineMap = createWordMap(magazine);
  const wordMap = createWordMap(note);

  for (const word of note) {
    if (magazineMap[word] === undefined) {
      console.log('No');
      return;
    } else {
      magazineMap[word] -= 1;
    }
  }

  // console.log(magazineMap);
  for (const word of Object.keys(magazineMap)) {
    if (magazineMap[word] < 0) {
      console.log('No');
      return;
    }
  }

  console.log('Yes');
}

function main() {
  const firstMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

  const m = parseInt(firstMultipleInput[0], 10);

  const n = parseInt(firstMultipleInput[1], 10);

  const magazine = readLine().replace(/\s+$/g, '').split(' ');

  const note = readLine().replace(/\s+$/g, '').split(' ');

  checkMagazine(magazine, note);
}
