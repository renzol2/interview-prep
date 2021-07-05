# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def middleNode(self, head: ListNode) -> ListNode:
    length = self.getLength(head)
    mid_length = (length // 2) + 1
    curr = head
    i = 0
    while curr is not None:
      i += 1
      if i == mid_length:
        return curr
      curr = curr.next
    return None
  
  def getLength(self, head: ListNode) -> int:
    length = 0
    curr = head
    while curr is not None:
      length += 1
      curr = curr.next
    return length
        