class Solution(object):
  def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sorted_nums = nums
    sorted_nums.sort()
    
    if sorted_nums[0] != 0:
      return 0
    
    for i in range(0, len(sorted_nums) - 1):
      if sorted_nums[i] + 1 < sorted_nums[i + 1]:
        return sorted_nums[i] + 1
    
    return sorted_nums[-1] + 1
          