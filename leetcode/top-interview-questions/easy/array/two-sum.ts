function twoSum(nums: number[], target: number): number[] {
  const diffs = {};
  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    const diff = target - num;
    if (diff === num) {
      const duplicateIndex = nums.indexOf(num, i+1);
      if (duplicateIndex === -1) {
        continue;
      } else {
        return [i, duplicateIndex];
      }
    }
    diffs[num] = diff;
  }
    
  for (let i = 0; i < nums.length; i++) {
    const value = diffs[nums[i]];
    if (value !== undefined) {
      if (diffs[value] === nums[i]) {
        return [i, nums.indexOf(diffs[nums[i]])];      
      }
    }
  }
  
  return [-1, -1];
};

function twoSum2(nums: number[], target: number): number[] {
  const diffs = {};
  for (let i = 0; i < nums.length; i++) {
    diffs[target - nums[i]] = i;
  }
  
  for (let i = 0; i < nums.length; i++) {
    const j = diffs[nums[i]];
    if (j !== undefined) {
      if (i === j) {
        continue;
      }
      return [i, j];
    }
  }
  
  return [-1, -1];
};
