class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        int L=nums.size();
        vector<int> res(L);
        int l = 0, r = accumulate(nums.begin(), nums.end(), 0);
        for (int i=0; i<L; i++){
            l += nums[i];
            res[i] = abs(l-r);
            r -= nums[i];
        }
        return res;
    }
};