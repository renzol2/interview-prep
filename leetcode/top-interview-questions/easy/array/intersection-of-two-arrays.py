class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # Turn nums1 into a dict mapping each value to its frequency
    storage = {}
    for num in nums1:
      if num not in storage:
        storage[num] = 0
      storage[num] += 1
    
    # For each num in nums2, check that it's in storage
    # If it's in storage, add it to intersection
    # But also, decrease its frequency in storage
    # If the frequency of a num in storage hits 0, remove it from storage
    intersection = []
    for num in nums2:
      if num in storage:
        intersection.append(num)
        storage[num] -= 1
        if storage[num] == 0:
          storage.pop(num)
    
    return intersection
        