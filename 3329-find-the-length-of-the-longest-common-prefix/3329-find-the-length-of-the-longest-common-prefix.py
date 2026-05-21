class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        p=set()
        max_prefix=""
        
        for n in map(str, arr1):
            for i in range(len(n)):
                p.add(n[:i+1])
        
        for n in map(str, arr2):
            for i in range(len(n)):
                prefix = n[:i+1]
                if prefix in p and len(prefix)>len(max_prefix):
                    max_prefix=prefix
        

        return len(max_prefix)