/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
 var isAnagram = function(s, t) {
  if (s.length !== t.length) return false;
  
  const letterCounts = {};
  for (let i = 0; i < s.length; i++) {
    const sc = s[i];
    const tc = t[i];
    
    if (letterCounts[sc] === undefined) {
      letterCounts[sc] = 0;
    }
    if (letterCounts[tc] === undefined) {
      letterCounts[tc] = 0;
    }
    
    letterCounts[sc] += 1;
    letterCounts[tc] -= 1;
  }
  
  const isAnagram = !Object.keys(letterCounts).some((key) => letterCounts[key] !== 0);
  return isAnagram;
};
