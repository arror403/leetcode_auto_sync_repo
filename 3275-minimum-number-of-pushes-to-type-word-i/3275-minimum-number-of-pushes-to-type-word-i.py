class Solution:
    def minimumPushes(self, word: str) -> int:
        return [-1, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 42, 45, 48, 52, 56][len(word)]
        # L=len(word)
        # i=1
        # res=0
        # while L>=8:
        #     res+=i*8
        #     i+=1
        #     L-=8

        # if L: res+=L*i

        # return res