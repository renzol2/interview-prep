/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function (p, q) {
  if (p === null && q === null) {
    return true;
  } else if (p === null && q !== null) {
    return false;
  } else if (p !== null && q === null) {
    return false;
  }

  const pstack = [p];
  const qstack = [q];

  while (pstack.length > 0 && qstack.length > 0) {
    const currentP = pstack.pop();
    const currentQ = qstack.pop();

    if (currentP.val !== currentQ.val) {
      return false;
    }

    if (currentP.left && currentQ.left) {
      pstack.push(currentP.left);
      qstack.push(currentQ.left);
    } else if (
      (currentP.left && !currentQ.left) ||
      (!currentP.left && currentQ.left)
    ) {
      return false;
    }

    if (currentP.right && currentQ.right) {
      pstack.push(currentP.right);
      qstack.push(currentQ.right);
    } else if (
      (currentP.right && !currentQ.right) ||
      (!currentP.right && currentQ.right)
    ) {
      return false;
    }
  }

  return true;
};
