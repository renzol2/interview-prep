class CachedNumArray:
  def __init__(self, nums: List[int]):
    self.storage = []
    prefix_sum = 0
    for num in nums:
      prefix_sum += num
      self.storage.append(prefix_sum)

  def sumRange(self, left: int, right: int) -> int:
    # Brute: O(n)
    # Cache: O(1) because hash-map
    if left > 0 and right > 0:
      return self.storage[right] - self.storage[left - 1]
    else:
      return self.storage[left or right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

class NumArray:
  def __init__(self, nums: List[int]):
    self.nums = nums

  def sumRange(self, left: int, right: int) -> int:
    return sum(self.nums[left:right+1])