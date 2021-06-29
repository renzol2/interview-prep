/**
 * @param {number[]} nums
 */
 var NumArray = function(nums) {
  this.nums = []
  let prefixSum = 0;
  for (let num of nums) {
    prefixSum += num;
    this.nums.push(prefixSum);
  }
  console.log(this.nums);
};

/** 
 * @param {number} left 
 * @param {number} right
 * @return {number}
 */
NumArray.prototype.sumRange = function(left, right) {
  if (left > 0 && right > 0) {
    return this.nums[right] - this.nums[left - 1];
  } else {
    return this.nums[left || right];
  }
};

/** 
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */