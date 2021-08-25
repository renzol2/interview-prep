class Solution:
  def climbStairs(self, n: int) -> int:
    return self.climbStairsHelper(n)
          
  def climbStairsHelper(self, n: int) -> int:
    if n == 0:
      return 1
    
    ways = 0
    if n >= 1:
      ways += self.climbStairsHelper(n - 1)
    
    if n >= 2:
      ways += self.climbStairsHelper(n - 2)
    
    return ways
  
class Solution2:
  def climbStairs(self, n: int) -> int:
    storage = {}
    storage[1] = 1
    storage[2] = 2
    return self.climbStairsHelper(n, storage)
          
  def climbStairsHelper(self, n: int, storage: dict) -> int:
    if n not in storage:
      storage[n] = self.climbStairsHelper(n-1, storage) + self.climbStairsHelper(n-2, storage)
    return storage[n]
      
class Solution3:
    def climbStairs(self, n: int) -> int:
      if n == 1:
        return 1
      if n == 2:
        return 2
      
      storage = {}
      storage[1] = 1
      storage[2] = 2
      
      for i in range(3, n+1):
        storage[i] = storage[i-1] + storage[i-2]
      
      return storage[n]
