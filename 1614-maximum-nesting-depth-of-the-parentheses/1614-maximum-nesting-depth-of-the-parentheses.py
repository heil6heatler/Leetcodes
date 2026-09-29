class Solution:
    def maxDepth(self, s: str) -> int:
        if s=='':
            return 0
        p=0
        maxi=0
        for ch in s:
            if ch=='(':
                p+=1
            elif ch==')':
                p-=1
            
            maxi=max(maxi, p)
        
        return maxi