# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    
    p_stack = [p]
    q_stack = [q]
    
    while p_stack and q_stack:
        p_node = p_stack.pop()
        q_node = q_stack.pop()
        
        if p_node.val != q_node.val:
            return False
        
        if p_node.left and q_node.left:
            p_stack.append(p_node.left)
            q_stack.append(q_node.left)
        elif p_node.left is not None and not q_node.left:
            return False
        elif not p_node.left and q_node.left is not None:
            return False
        
        if p_node.right and q_node.right:
            p_stack.append(p_node.right)
            q_stack.append(q_node.right)
        elif p_node.right is not None and not q_node.right:
            return False
        elif not p_node.right and q_node.right is not None:
            return False
    
    return True
