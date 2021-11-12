function lengthOfLongestSubstring(s: string): number {
  if (s.length < 2) return s.length;

  const usedChars = {};
  let max = 0;

  let left = 0;
  for (let right = 0; right < s.length; right++) {
    const c = s[right];
    if (usedChars[c] !== undefined) {
      left = Math.max(left, usedChars[c] + 1);
    }
    usedChars[c] = right;
    max = Math.max(max, right - left + 1);
  }

  return max;
}
