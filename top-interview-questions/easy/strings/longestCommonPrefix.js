/**
 * @param {string[]} strs
 * @return {string}
 */
 var longestCommonPrefix = function(strs) {
  if (strs.length === 1) return strs[0];
  if (strs[0].length === 0) return '';
  
  let shortestIndex = 0;
  let hasZeroLength = false;
  strs.forEach((s, i) => {
    if (s.length == 0) hasZeroLength = true;
    if (s.length < strs[0].length) shortestIndex = i;
  });
  if (hasZeroLength) return '';
  
  let commonSubstring = '';
  for (let i = 1; i < strs[shortestIndex].length + 1; i++) {
    let nextSubstring = strs[shortestIndex].substring(0, i);
    for (let s of strs) {    
      let currentSubstring = s.substring(0, i);
      if (currentSubstring !== nextSubstring) {
        return commonSubstring;
      }
    }
    commonSubstring = nextSubstring;
  }
  
  // We reached shortest length
  // Must return either '' or shortest string
  
  return strs[shortestIndex];
};