class Solution:
  def countBits(self, n: int) -> List[int]:
    # lookup[n] -> # of 1's in bin. rep. of n
    lookup = [0, 1, 1]
    
    if n < 3:
        return lookup[0:n+1]
    
    for i in range(3, n+1):
        num_ones_half = lookup[i // 2]
        if i % 2 != 0:
            num_ones_half += 1
        lookup.append(num_ones_half)
    
    return lookup

class Solution2:    
  def countBits(self, n: int) -> List[int]:
    ans = [0]
    for i in range(1, n+1):
      if i % 2 == 0:
        ans.append(ans[i // 2])
      else:
        ans.append(ans[i // 2] + 1)
    return ans