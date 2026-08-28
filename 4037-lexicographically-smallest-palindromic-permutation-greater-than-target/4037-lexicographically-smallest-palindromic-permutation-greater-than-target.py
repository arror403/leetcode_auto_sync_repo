class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        def func(path, big, cnt, mid, n):
            nonlocal res
            if res: return True

            if len(path)==n//2:
                left=path
                right=path[::-1]
                pal=(left+mid+right if n%2 else left+right)
                if pal>target:
                    res=pal
                    return True
                
                return False
            
            i=len(path)
            for c in range(26):
                if cnt[c]==0: continue
                if (not big and c+97 < ord(target[i])): continue
                path+=chr(c+97)
                cnt[c]-=1
                newbig=(big or (c+97 > ord(target[i])))
                if func(path, newbig, cnt, mid, n): return True
                path=path[:-1]
                cnt[c]+=1

            return False


        res=""
        odd=0
        mid='0'
        cnt=[0]*26
        for c in s: cnt[ord(c)-97]+=1

        for i in range(26):
            if cnt[i]%2:
                odd+=1
                mid=chr(i+97)
            cnt[i]//=2
        
        if odd>1: return ""     

        func("", False, cnt, mid, len(s))
        

        return res    