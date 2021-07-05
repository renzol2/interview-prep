# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def isPalindrome(self, head: ListNode) -> bool:
    if head.next is None:
      return True
    
    length = self.getLength(head)
    
    if length % 2 == 0:
      return self.isPalindromeEven(head)
    else:
      return self.isPalindromeOdd(head, length)
  

  def isPalindromeOdd(self, head: ListNode, length: int) -> bool:
    middle_index = length // 2 + 1
    stack = []
    # .append()
    # .pop()
    # Top of stack index: -1 
    curr = head
    i = 0
    while curr is not None:
      i += 1
      
      # Skip middle index
      if i == middle_index:
        curr = curr.next
        continue
      
      if len(stack) != 0 and stack[-1] == curr.val:
        stack.pop()
      else:
        stack.append(curr.val)
      curr = curr.next
    return len(stack) == 0
    
  
  def isPalindromeEven(self, head: ListNode) -> bool:
    stack = []
    # .append()
    # .pop()
    # Top of stack index: -1 
    curr = head
    while curr is not None:
      if len(stack) != 0 and stack[-1] == curr.val:
        stack.pop()
      else:
        stack.append(curr.val)
      curr = curr.next
    return len(stack) == 0
  
  def getLength(self, head: ListNode) -> int:
    length = 0
    curr = head
    while curr is not None:
      length += 1
      curr = curr.next
    return length
  
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def isPalindrome(self, head: ListNode) -> bool:
    # Global variable for left pointer
    self.front_pointer = head
    
    def recursively_check(current=head) -> bool:
      # Current is the right pointer
      if current is not None:
        # Recursively iterate through list until done
        if not recursively_check(current.next):
          return False

        # Check that the l/r pointer are not equal
        if self.front_pointer.val != current.val:
          return False
        
        self.front_pointer = self.front_pointer.next

      # Returning true if current is none, OR if
      # left/right ARE equal
      return True
    
    return recursively_check()
  
      