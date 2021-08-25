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

class Solution2:
  def removeElements(self, head: ListNode, val: int) -> ListNode:
    dummy = ListNode()
    
    curr = head
    new_curr = dummy
    while curr is not None:
      # print(new_curr)
      if curr.val != val:
        new_curr.next = ListNode(curr.val, None)
        new_curr = new_curr.next 
      curr = curr.next
      
    return dummy.next

class Solution3:
  def removeElements(self, head: ListNode, val: int) -> ListNode:
    while head is not None and head.val == val:
      head = head.next
    curr = head
    while curr is not None:
      next_node = curr.next
      while next_node is not None and next_node.val == val:
        next_node = next_node.next
      curr.next = next_node
      curr = curr.next
    return head