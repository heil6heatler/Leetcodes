class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        freq=Counter(s)
        char=sorted(freq, key=lambda x: freq[x], reverse= True)
        result=''
        for ch in char:
            result+=ch*freq[ch]
        return result