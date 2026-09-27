class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1=256*[0]
        m2=256*[0]
        n=len(s)

        for i in range(n):
            if m1[ord(s[i])]!=m2[ord(t[i])]:
                return False
            else:
                m1[ord(s[i])]=i+1
                m2[ord(t[i])]=i+1
        return True
        