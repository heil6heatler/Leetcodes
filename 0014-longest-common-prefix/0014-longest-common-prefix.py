class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        strs.sort()
        f=strs[0]
        l=strs[len(strs)-1]
        ans=''

        for i in range(min(len(f), len(l))):
            if f[i]!=l[i]:
                break
            else:
                ans+=f[i]
        return ans