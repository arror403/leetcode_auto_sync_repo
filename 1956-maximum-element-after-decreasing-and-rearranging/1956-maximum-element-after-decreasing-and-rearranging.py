class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        L=len(arr)
        arr[0]=1

        for i in range(L-1):
            if (arr[i+1]-arr[i])>0:
                arr[i+1]=arr[i]+1


        return arr[-1]