class Solution {
public:
    int countServers(vector<vector<int>>& grid) {
        vector<int> r,c;
        int tmp;

        for(auto x:grid){
            tmp=0;
            for(auto v:x) tmp+=v;
            r.push_back(tmp);
        }
        for(auto x:transpose(grid)){
            tmp=0;
            for(auto v:x) tmp+=v;
            c.push_back(tmp);
        }

        int g=0;
        for(int i=0; i<r.size(); i++){
            for(int j=0; j<c.size(); j++){
                if (r[i]==c[j] && c[j]==grid[i][j] && grid[i][j]==1)
                    g++;
            }
        }

        return accumulate(r.begin(), r.end(), 0) - g;
    }

    vector<vector<int>> transpose(const vector<vector<int>>& matrix){
        int rows = matrix.size();
        int cols = rows > 0 ? matrix[0].size() : 0;
        vector<vector<int>> result(cols, vector<int>(rows));

        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                result[j][i] = matrix[i][j];
            }
        }
        return result;
    }

};