from typing import List


class Solution:
  def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    # Comparator function
    def sortStartTime(interval):
      return interval[0]
    
    # Sort intervals by start time
    intervals.sort(key=sortStartTime)

    # For an element in the intervals,
    # if the end time of the current interval is greater than
    # the start of the next interval, return False

    # Skip last element
    for i in range(len(intervals) - 1):
      current_interval = intervals[i]
      next_interval = intervals[i + 1]
      if current_interval[1] > next_interval[0]:
        return False
    
    return True

s = Solution()

# Example 1
intervals1 = [[0, 30], [5, 10], [15, 20]]
result1 = s.canAttendMeetings(intervals1)
expected1 = False
print('Result 1: ', result1)
print(result1 == expected1)

# Example 2
intervals2 = [[7, 10], [2, 4]]
result2 = s.canAttendMeetings(intervals2)
expected2 = True
print('Result 2: ', result2)
print(result2 == expected2)
