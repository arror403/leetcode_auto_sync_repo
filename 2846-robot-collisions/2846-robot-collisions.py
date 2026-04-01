class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        left,right=[],[]
        for i,_ in sorted(enumerate(positions), key=lambda x:x[1]):
            if directions[i]=='R': 
                right.append(i)
            else:
                while right and healths[right[-1]]<healths[i]:
                    right.pop()
                    healths[i]-=1
                if not right: 
                    left.append(i)
                elif healths[right[-1]]==healths[i]: 
                    right.pop()
                else: 
                    healths[right[-1]]-=1

        return [healths[i] for i in sorted(left+right)]