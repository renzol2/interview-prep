class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    l = 0
    r = len(nums) - 1
    lb = hb = -1
    
    while l <= r:
      mid = l + (r - l) // 2
      
      if nums[mid] == target:
        # Find bounds
        lb = mid
        hb = mid
        while lb > 0 and nums[lb - 1] == target:
          lb -= 1
        while hb + 1 < len(nums) and nums[hb + 1] == target:
          hb += 1
        break
      
      if nums[mid] < target:
        l = mid + 1
      elif nums[mid] > target:
        r = mid - 1
    
    return [lb, hb]