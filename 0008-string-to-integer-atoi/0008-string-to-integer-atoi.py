class Solution:
    def myAtoi(self, s: str) -> int:
        i=0
        while i<len(s) and s[i]==' ':
            i+=1

        sign=1    
        if i<len(s) and (s[i]=='+' or s[i]=='-'):
            sign= -1 if s[i]=='-' else 1
            i+=1
        
        mini= -2**31
        maxi= 2**31-1
        num=0

        while i < len(s):
            if not s[i].isdigit():
                return sign*num
            
            num= num*10 + int(s[i])
            i+=1
            
            if num> maxi:
                return maxi if sign==1 else mini
        
        return sign*num