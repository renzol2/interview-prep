class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1_copy = nums1[:m]
    i = j = 0
    new_idx = 0
    while i < m and j < n:
      val1 = nums1_copy[i]
      val2 = nums2[j]
      if val1 < val2:
        nums1[new_idx] = val1
        i += 1
      else:
        nums1[new_idx] = val2
        j += 1
      new_idx += 1
    
    if i == m:
      while j < n:
        nums1[new_idx] = nums2[j]
        new_idx += 1
        j += 1
    elif j == n:
      while i < m:
        nums1[new_idx] = nums1_copy[i]
        new_idx += 1
        i += 1