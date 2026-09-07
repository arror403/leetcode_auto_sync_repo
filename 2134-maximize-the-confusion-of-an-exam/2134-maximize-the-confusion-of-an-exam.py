class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res=M=0
        d=Counter()

        for i in range(len(answerKey)):
            d[answerKey[i]]+=1
            M=max(M, d[answerKey[i]])
            if res-M < k:
                res+=1
            else:
                d[answerKey[i-res]]-=1


        return res