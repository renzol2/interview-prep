function maxSubArray(nums: number[]): number {
  let currentSum = 0;
  let maxSum = nums[0];
  
  for (let num of nums) {
    currentSum = Math.max(num + currentSum, num)
    maxSum = Math.max(currentSum, maxSum);
  }
  
  return maxSum;
};
