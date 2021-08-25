# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def averageOfLevels(self, root: TreeNode) -> List[float]:
    current_level = [root]
    averages = []
    while current_level:
      average = 0.0
      next_level = []
      for n in current_level:
        average += n.val
        if n.left:
          next_level.append(n.left)
        if n.right:
          next_level.append(n.right)
      average /= len(current_level)
      averages.append(average)
      current_level = next_level
    return averages
    
class Solution2:
  def averageOfLevels(self, root: TreeNode) -> List[float]:
    averages = []
    current_level = [root]
    self.bfs(current_level, averages)
    return averages
  
  def bfs(self, current_level: List[TreeNode], averages: List[float]) -> None:
    if not current_level:
      return
    
    average = 0.0
    next_level = []
    for n in current_level:
      average += n.val
      if n.left:
        next_level.append(n.left)
      if n.right:
        next_level.append(n.right)
    average /= len(current_level)
    averages.append(average)
    self.bfs(next_level, averages)
    
    
    
        