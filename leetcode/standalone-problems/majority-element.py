class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    freqs = {}
    for num in nums:
        if num not in freqs:
            freqs[num] = 0
        freqs[num] += 1
        if freqs[num] > floor(len(nums) / 2):
            return num
    return nums[0]
