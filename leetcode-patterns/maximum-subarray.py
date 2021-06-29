import sys
class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    max_sum = nums[0]
    current_sum = nums[0]
    for num in nums[1:]:
      if num < current_sum + num:
        # Add the number if it increases our sum
        current_sum += num
      else:
        # num >= current_sum + num
        # Leave our current sum and take the current
        current_sum = num
      
      # Check if this current sum is the best
      if current_sum > max_sum:
        max_sum = current_sum
    
    return max_sum