class Solution:
  def peakIndexInMountainArray(self, arr: List[int]) -> int:
    m = max(arr)
    i = arr.index(m)
    return i
  
class Solution2:
  def peakIndexInMountainArray(self, arr: List[int]) -> int:
    for i in range(len(arr)-1):
      if arr[i] > arr[i+1]:
        return i
    return -1

class Solution3:
  def peakIndexInMountainArray(self, arr: List[int]) -> int:
    if len(arr) == 3:
      return arr[1]
    return self.bs(0, len(arr)-1, arr)
    
  def bs(self, l, r, arr) -> int:
    mid = l + (r - l) // 2
    print(l, mid, r)
    
    mid_val = arr[mid]
    if arr[mid-1] < mid_val and mid_val > arr[mid+1]:
      return mid
    elif arr[mid-1] < mid_val and mid_val < arr[mid+1]:
      return self.bs(mid+1, r, arr)
    elif arr[mid-1] > mid_val and mid_val > arr[mid+1]:
      return self.bs(l, mid-1, arr)
  
    return -1