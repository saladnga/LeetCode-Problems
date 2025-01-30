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
    int pairSum(ListNode* head) {
        // 1->2->3->4->5
        if (head == nullptr || head->next == nullptr) {
            return 0;
        }
        
        ListNode* fast = head;
        ListNode* slow = head;

        // Find the middle = 4
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* prev = nullptr;
        ListNode* curr = slow;
        ListNode* nextNode;

        // Reverse the second half
        // 4->5->nullptr = 5->4->nullptr
        while (curr != nullptr) {
            nextNode = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextNode;
        }


        ListNode* secondHalf = prev;

        // (1,5), (2, 4), (3, nullptr)
        int maxSum = 0;
        while (secondHalf != nullptr) {
            maxSum = max(maxSum, head->val + secondHalf->val);
            head = head->next;
            secondHalf = secondHalf->next;
        }
        return maxSum;
    }
};