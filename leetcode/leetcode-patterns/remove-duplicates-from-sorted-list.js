/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
 var deleteDuplicates = function(head) {
  let dummy = new ListNode();
  let curr = head;
  let new_head = dummy;
  
  while (curr !== null) {
    if (curr.next == null || curr.val !== curr.next.val) {
      dummy.next = new ListNode(curr.val);
      dummy = dummy.next;
    }
    curr = curr.next;
  }
  
  return new_head.next;
};