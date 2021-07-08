# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
  def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1: return n
    return self.searchBadVersion(1, n)
    
  def searchBadVersion(self, l, r):
    """
    @param l rightmost non-bad
    @param r leftmost bad
    """
    # print(l, r)
    
    # Base case: r = l
    if r == l: 
      return l
    
    # Edge case: r - l = 1
    if r - l == 1:
      if isBadVersion(l):
        return l
      else: 
        return r
    
    mid = l + ((r - l) // 2)
    
    if isBadVersion(mid):
      return self.searchBadVersion(l, mid)
    else:
      return self.searchBadVersion(mid + 1, r)
        