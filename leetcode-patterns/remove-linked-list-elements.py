# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def removeElements(self, head: ListNode, val: int) -> ListNode:
    curr = head
    while curr is not None:
      # print(curr.val)
      if head == curr and head.val == val:
        head = head.next
        curr = head
      else:
        while curr.next is not None and curr.next.val == val:
          curr.next = curr.next.next
        curr = curr.next
    return head
