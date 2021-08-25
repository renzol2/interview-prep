class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    rotations = k % len(nums)
    if rotations == 0:
      return
    
    rotated = nums[len(nums) - rotations:] + nums[:-rotations]
    for i in range(len(nums)): nums[i] = rotated[i]