class Solution:
    def numberOfStableArrays(self, z, o, l, MOD=10**9+7):
        # WTF!?
        S=lambda n,k:k and sum((-1)**j*comb(k,j)*comb(n-j*l-1,k-1) for j in range(k+1) if n >= k+j*l)
        return sum((S(o,k-1)+2*S(o,k)+S(o,k+1))*S(z,k) for k in range((min(z,o)+l-1)//l,z+1)) % MOD