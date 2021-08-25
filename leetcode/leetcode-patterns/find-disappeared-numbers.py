class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
      # 1. Use dict to add frequencies of nums
      # 2. Iterate over [1, n] and add numbers 
      # to return array if they do not exist in dict
      
      frequencies = {}
      for n in nums:
        frequencies[n] = True
      
      return_list = []
      for i in range(1, len(nums) + 1):
        if i not in frequencies:
          return_list.append(i)
        
      return return_list

    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
      # Turn included indices negative
      for i in range(len(nums)):
        value = abs(nums[i])
        turn_negative = nums[value - 1]
        if turn_negative > 0:
          nums[value - 1] = -nums[value - 1]
      
      resultant = []
      for j in range(len(nums)):
        if nums[j] > 0:
          resultant.append(j + 1)
      
      return resultant
        