/**
 * @param {number[]} nums
 * @return {number}
 */
 var missingNumber = function(nums) {
  let sum = sumOfConsecutiveIntegers(nums.length);
  for (let num of nums) {
    sum -= num;
  }
  return sum;
};


/**
 * @param {number} n
 * @return {number}
 */
var sumOfConsecutiveIntegers = function(n) {
  let numerator = n * (n + 1);
  return Math.floor(numerator / 2);
}