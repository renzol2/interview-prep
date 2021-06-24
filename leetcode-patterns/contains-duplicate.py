class Solution(object):
  def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return len(set(nums)) < len(nums)

  def containsDuplicate2(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    s = set()
    for n in nums:
      if n not in s:
        s.add(n)
      else:
        return True
    return False
        
        
        
        