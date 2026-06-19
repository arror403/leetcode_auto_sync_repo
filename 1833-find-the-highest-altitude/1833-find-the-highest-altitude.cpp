class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        vector<int> res={0};
        int x=0;
        for (int i=0; i<gain.size(); i++){
            res.push_back(x+gain[i]);
            x+=gain[i];
        }
        return *max_element(res.begin(), res.end());
    }
};