/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* one = head;
        ListNode* two = head;
        int count = 0;
        while (head != nullptr) {
            count++;
            head = head->next;
        }
        head = one;
        for (int i = 1; i < k; i++) {
            one = one->next;
        }
        for (int i = 1; i < count - k + 1; i++) {
            two = two->next;
        }
        int temp = one->val;
        one->val = two->val;
        two->val = temp;
        return head;
    }
};