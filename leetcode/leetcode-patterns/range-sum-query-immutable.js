/**
 * @param {number[]} nums
 */
var PrefixSumNumArray = function (nums) {
  this.nums = [];
  let prefixSum = 0;
  for (let num of nums) {
    prefixSum += num;
    this.nums.push(prefixSum);
  }
};

/**
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
PrefixSumNumArray.prototype.sumRange = function (left, right) {
  if (left > 0 && right > 0) {
    return this.nums[right] - this.nums[left - 1];
  } else {
    return this.nums[left || right];
  }
};

/**
 * @param {number[]} nums
 */
var NumArray = function (nums) {
  this.storage = {};
  for (let i = 0; i < nums.length; i++) {
    let sum = 0;
    for (let j = i; j < nums.length; j++) {
      sum += nums[j];
      this.storage[[i, j]] = sum;
    }
  }
};

/**
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
NumArray.prototype.sumRange = function (left, right) {
  return this.storage[[left, right]];
};
