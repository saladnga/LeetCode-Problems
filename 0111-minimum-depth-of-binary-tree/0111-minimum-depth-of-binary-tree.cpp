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
    int minDepth(TreeNode* root) {
        return dfs(root);
    }
    int dfs(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        if (root->left == nullptr) {
            return 1 + dfs(root->right);
        }
        if (root->right == nullptr) {
            return 1 + dfs(root->left);
        }
        if (root->left != nullptr && root->right != nullptr) {
            return 1 + min(dfs(root->left), dfs(root->right));
        }
        return 0;
    }
};