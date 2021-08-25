class Solution:
  def minDepth(self, root: TreeNode) -> int:
    if root is None:
      return 0
    
    depth = 1
    current_level = [root]
    while current_level:
      next_level = []
      for n in current_level:
        if not n.left and not n.right:
          return depth
        if n.left:
          next_level.append(n.left)
        if n.right:
          next_level.append(n.right)
      current_level = next_level
      depth += 1
    return depth

class Solution2:
  def minDepth(self, root: TreeNode) -> int:
    if root is None:
      return 0
    return self.inorder(root, 1)
  
  def inorder(self, node: TreeNode, depth: int) -> int:
    if node is None:
      return depth
    if node.left is None and node.right is None:
      return depth
    
    left_depth = right_depth = 100000
    if node.left:
      left_depth = self.inorder(node.left, depth+1)
    if node.right:
      right_depth = self.inorder(node.right, depth+1)
    
    return min(left_depth, right_depth)
