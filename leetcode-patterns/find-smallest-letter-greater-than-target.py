class Solution:
  def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    for letter in letters:
      if ord(letter) > ord(target):
        return letter
    
    return letters[0]
  
class Solution2:  
  def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    nums = [ord(letter) for letter in letters]
    target_num = ord(target)
    i = self.bs(0, len(nums)-1, nums, target_num) % len(nums)
    
    while nums[i] == target_num:
      i = (i + 1) % len(nums)
      
    return chr(nums[i])

  def bs(self, l, r, nums, target):
    if l <= r:
      mid = l + ((r - l) // 2)
      
      if nums[mid] == target:
        next_ch = mid + 1
        return next_ch
      
      elif nums[mid] < target:
        return self.bs(mid+1, r, nums, target)
      elif nums[mid] > target:
        return self.bs(l, mid-1, nums, target)
      
    return l