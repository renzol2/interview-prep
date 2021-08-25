/**
 * @param {number[]} nums
 */
 var Solution = function(nums) {
  this.nums = nums;
};

/**
 * Resets the array to its original configuration and return it.
 * @return {number[]}
 */
Solution.prototype.reset = function() {
  return this.nums;
};

/**
 * Returns a random shuffling of the array.
 * @return {number[]}
 */
Solution.prototype.shuffle = function() {
  let shuffled = [];
  let unusedIndices = [];
  
  for (let i = 0; i < this.nums.length; i++) {
    unusedIndices.push(i);
  }
  
  for (let i = 0; i < this.nums.length; i++) {
    let randIndex = Math.floor(Math.random() * unusedIndices.length);
    let randNumber = this.nums[unusedIndices[randIndex]];
    unusedIndices.splice(randIndex, 1);
    shuffled.push(randNumber);
  }
  
  return shuffled;
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(nums)
 * var param_1 = obj.reset()
 * var param_2 = obj.shuffle()
 */
