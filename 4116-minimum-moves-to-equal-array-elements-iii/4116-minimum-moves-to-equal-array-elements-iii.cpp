class Solution {
public:
    int minMoves(vector<int>& nums) {
        auto M=max_element(nums.begin(), nums.end()); // M is vector<int>::iterator
        int L=nums.size();
        int S=accumulate(nums.begin(), nums.end(), 0);

        return (*M)*L-S;
    }
};