/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const letterFreqsToArray = {};
  for (const str of strs) {
    const letterFreq = convertStringToLetterFreqs(str);
    const stringified = JSON.stringify(letterFreq);
    if (letterFreqsToArray[stringified] === undefined) {
      letterFreqsToArray[stringified] = [str];
    } else {
      letterFreqsToArray[stringified].push(str);
    }
  }

  const groupedAnagrams = [];
  for (const letterFreq of Object.keys(letterFreqsToArray)) {
    groupedAnagrams.push(letterFreqsToArray[letterFreq]);
  }

  return groupedAnagrams;
};

var convertStringToLetterFreqs = function (str) {
  const map = {};
  const splitStr = str.split('');
  splitStr.sort();
  const sortedStr = splitStr.join('');
  for (const s of sortedStr) {
    if (map[s] === undefined) {
      map[s] = 1;
    } else {
      map[s] += 1;
    }
  }
  return map;
};
