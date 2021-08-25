# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def hasCycle(self, head: ListNode) -> bool:
    storage = {}
    current = head
    while current is not None:
      if current in storage:
        return True
      storage[current] = True
      current = current.next
    return False

class Solution:
  def hasCycle(self, head: ListNode) -> bool:
    if head is None:
      return False
    
    first = head
    second = head.next
    
    while first is not None and second is not None:
      if first == second:
        return True
      
      first = first.next
      second = second.next
      
      if second is not None:
        second = second.next
    
    return False