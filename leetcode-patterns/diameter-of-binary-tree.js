/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

let diameter = 0;

/**
 * @param {TreeNode} root
 * @return {number}
 */
var diameterOfBinaryTree = function (root) {
  diameter = 0;
  heightOfBinaryTree(root);
  return diameter;
};

var heightOfBinaryTree = function (root) {
  if (root === null) {
    return -1;
  }

  const leftHeight = heightOfBinaryTree(root.left);
  const rightHeight = heightOfBinaryTree(root.right);

  diameter = Math.max(diameter, leftHeight + rightHeight + 2);

  return Math.max(leftHeight, rightHeight) + 1;
};
