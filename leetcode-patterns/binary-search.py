from typing import List


class Solution:
  def search(self, nums: List[int], target: int) -> int:
    return self.bs(nums, target, 0, len(nums)-1)
  
  def bs(self, nums: List[int], target: int, l: int, r: int):
    if l <= r:
      mid_index = l + ((r - l) // 2)
      mid = nums[mid_index]

      if mid == target:
        return mid_index
      elif mid > target:
        return self.bs(nums, target, l, mid_index-1)
      else:
        return self.bs(nums, target, mid_index+1, r)
    
    return -1

s = Solution()

nums = [-1,0,3,5,9,12]

# Example 1
target = 9
result = s.search(nums, target)
expected = 4
print(result == expected)

# Example 2
target = 2
result = s.search(nums, target)
expected = -1
print(result == expected)
