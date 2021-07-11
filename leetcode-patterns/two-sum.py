class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    storage = {}
    for i, num in enumerate(nums):
      storage[target - num] = i
    
    for j, num in enumerate(nums):
      if num not in storage:
        continue
      i = storage[num]
      if i == j:
        continue
      if num + nums[i] == target:
        return [i, j]
    return [-1, -1]
