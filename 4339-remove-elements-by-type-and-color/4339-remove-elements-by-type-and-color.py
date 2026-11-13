class Solution:
    def canRemoveAll(self, types: list[int], colors: list[int], groupSize: list[int]) -> bool:
        s=[]
        for t,c in zip(types, colors):
            if s and s[-1][0]==t and s[-1][1]==c:
                s[-1][2]+=1
            else:
                s.append([t, c, 1])

            if s[-1][2]==groupSize[t]:
                s.pop()

        return len(s)==0