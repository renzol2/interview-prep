/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  let storage = {};
  for (let num of nums) {
    if (storage[num] === undefined) {
      storage[num] = true;
    } else {
      return true;
    }
  }
  return false;
};
