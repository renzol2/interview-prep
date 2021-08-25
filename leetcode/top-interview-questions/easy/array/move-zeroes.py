class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    ans = []
    for num in nums:
      if num != 0:
        ans.append(num)
    for i in range(len(nums) - len(ans)):
      ans.append(0)
    for i in range(len(nums)):
      nums[i] = ans[i]
