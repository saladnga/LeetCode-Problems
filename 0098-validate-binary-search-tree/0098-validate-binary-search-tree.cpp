/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return dfs(root, LONG_MIN, LONG_MAX);
    }
    bool dfs(TreeNode* node, long small, long large) {
            if (node == nullptr) {
                return true;
            }
            if (!(small < node->val && node->val < large)) {
                return false;
            }
            
            long left = dfs(node->left, small, node->val);
            long right = dfs(node->right, node->val, large);

            return left && right;
    }
};