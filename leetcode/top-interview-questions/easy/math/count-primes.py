import math

class Solution:
  def countPrimes(self, n: int) -> int:
    """
    Sieve of Eratosthenes
    """
    nums = set([i for i in range(2, n)])
    
    top = math.ceil(math.sqrt(n))
    for i in range(2, top):
      # Remove multiples of i
      multiple = i*i
      while multiple < n:
        if multiple in nums:
          nums.remove(multiple)
        multiple += i
    
    return len(nums)
    