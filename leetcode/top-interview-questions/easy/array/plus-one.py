class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      num = ''
      for digit in digits: num += str(digit)
      num = str(int(num) + 1)
      
      plus_one = []
      for digit in num: plus_one.append(digit)
      return plus_one
    