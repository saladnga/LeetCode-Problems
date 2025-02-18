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
    vector<int> largestValues(TreeNode* root) {
        if (root == nullptr) {
            return vector<int>{};
        }
        vector<int> ans;
        queue<TreeNode*> queue;
        queue.push(root);

        while (queue.empty() == false) {
            int cur_max = INT_MIN;
            int cur_length = queue.size();
            for (int i = 0; i < cur_length; i++) {
                TreeNode* node = queue.front();
                queue.pop();
                cur_max = max(cur_max, node->val);
                if (node->left) {
                    queue.push(node->left);
                }
                if (node->right) {
                    queue.push(node->right);
                }
            }
            ans.push_back(cur_max);
        }
        return ans;
    }
};