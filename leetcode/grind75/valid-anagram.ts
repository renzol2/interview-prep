function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) return false;
  
  let charFreqsS = {};
  for (let c of s) {
      if (charFreqsS[c] === undefined) {
          charFreqsS[c] = 0;
      }
      charFreqsS[c] += 1;
  }
  
  for (let c of t) {
      if (charFreqsS[c] === undefined) {
          return false;
      }
      
      charFreqsS[c] -= 1;
      
      if (charFreqsS[c] === 0) {
          delete charFreqsS[c];
      }
  }
  
  return Object.keys(charFreqsS).length === 0;
};

