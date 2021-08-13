# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def __init__(self):
    self.d = 0
  
  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    self.height(root)
    return self.d
  
  def height(self, node: TreeNode) -> int:
    if node is None:
      return -1
    lh = self.height(node.left)
    rh = self.height(node.right)
    self.d = max(self.d, lh + rh + 2)
    return max(lh, rh) + 1
    
    
        