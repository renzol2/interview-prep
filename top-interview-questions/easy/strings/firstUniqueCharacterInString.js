/**
 * @param {string} s
 * @return {number}
 */
 var firstUniqChar = function(s) {
  outerLoop: for (let i = 0; i < s.length; i++) {
    for (let j = 0; j < s.length; j++) {
      if (i == j) continue;
      if (s[i] == s[j]) continue outerLoop;
    }
    return i;
  }
  return -1;
};