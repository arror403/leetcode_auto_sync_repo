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
        vector<int> m = LinkedToVec(head);
        int L = m.size();
        int res = INT_MIN;

        for (int i=0; i<L/2+1; i++)
        res = max(res, (m[i] + m[L-i-1]));

        return res;
    }

    vector<int> LinkedToVec(ListNode* head) {
        vector<int> x;
        while(head){
            x.push_back(head->val);
            head=head->next;
        }
        return x;
    }
};