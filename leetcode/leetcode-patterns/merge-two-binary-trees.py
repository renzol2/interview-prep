# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root1 and not root2:
      return None
    elif root1 and not root2:
      return root1
    elif not root1 and root2:
      return root2
    
    self.mergeDfs(root1, root2)
    return root1

  def mergeDfs(self, node1, node2):
    """
    Add node2 onto node1
    """
    
    if node1 is None:
      return node2
    if node2 is None:
      return node1
    
    node1.val += node2.val
    
    node1.left = self.mergeDfs(node1.left, node2.left)
    node1.right = self.mergeDfs(node1.right, node2.right)
    
    return node1
    
    
      