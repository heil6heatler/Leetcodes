class Solution:
    def beautySum(self, s: str) -> int:
        n=len(s)
        total=0

        for i in range(n):
            freq=[0]*26

            for j in range(i, n):
                ind=ord(s[j])-ord('a')
                freq[ind]+=1

                maxi=0
                mini=float('inf')

                for f in freq:
                    if f>0:
                        maxi=max(maxi, f)
                        mini=min(mini, f)
                total+=(maxi-mini)
        
        return total
