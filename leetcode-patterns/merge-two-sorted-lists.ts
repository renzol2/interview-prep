// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}
 

 function mergeTwoLists(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  if (l1 === null && l2 === null) return null;
  if (l1 === null) return l2;
  if (l2 === null) return l1;
  
  let dummy = new ListNode();
  
  let c1 = l1;
  let c2 = l2;
  let newCurrent = dummy;
  while (c1 !== null && c2 !== null) {
      if (c1.val <= c2.val) {
          newCurrent.next = c1;
          c1 = c1.next;
      } else {
          newCurrent.next = c2;
          c2 = c2.next;
      }
      newCurrent = newCurrent.next;
  }
  
  if (c1 === null) {
      newCurrent.next = c2;
  } else if (c2 === null) {
      newCurrent.next = c1;
  }
  
  return dummy.next;
};
