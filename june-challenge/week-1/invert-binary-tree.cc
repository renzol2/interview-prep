#include <algorithm>

class Solution {
public:
  struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
  };

  /**
   * Invert a binary tree.
   * https://leetcode.com/problems/invert-binary-tree/
   */
  TreeNode* invertTree(TreeNode* root) {
    if (root == nullptr) return nullptr;
    branchSwap(root);
    return root;
  }
  
  void branchSwap(TreeNode* root) {
    std::swap(root->left, root->right);
    if (root->left != nullptr) branchSwap(root->left);
    if (root->right != nullptr) branchSwap(root->right);
  }  
};

int main() {
  // Put driver code here
  return 0;
}
