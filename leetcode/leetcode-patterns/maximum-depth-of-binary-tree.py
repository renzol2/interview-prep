class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
      return 0
    stack = [(1, root)]
    max_depth = 0

    while stack:
      depth, curr = stack.pop()
      
      if curr.left:
        stack.append((depth + 1, curr.left))
      if curr.right:
        stack.append((depth + 1, curr.right))
      if depth > max_depth:
        max_depth = depth
    return max_depth

class Solution2:    
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    max_depth = self.dfs(root, 1)
    return max_depth
        
  def dfs(self, node: TreeNode, curr_depth) -> None:      
    if not node.left and not node.right:
      return curr_depth
    
    lheight = rheight = 0
    if node.left:
      lheight = self.dfs(node.left, curr_depth + 1)
    if node.right:
      rheight = self.dfs(node.right, curr_depth + 1)
    
    return max(lheight, rheight)
