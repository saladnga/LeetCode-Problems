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
    ListNode* deleteMiddle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* current = head;
        if (head->next == nullptr) {
            return nullptr;
        }
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        while (head != nullptr && head->next != nullptr) {
            if (head->next == slow) {
                head->next = slow->next;
                slow->next = nullptr;
            }
            else {
                head = head->next;
            }
        }
        return current;

    }
};