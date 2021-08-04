/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var minDepth = function (root) {
  if (root === null) {
    return 0;
  }

  let currentLevel = [root];
  let depth = 1;
  while (currentLevel.length > 0) {
    let nextLevel = [];
    for (const node of currentLevel) {
      if (node.left === null && node.right === null) {
        return depth;
      }
      if (node.left) {
        nextLevel.push(node.left);
      }
      if (node.right) {
        nextLevel.push(node.right);
      }
    }
    depth++;
    currentLevel = nextLevel;
  }

  return depth;
};
