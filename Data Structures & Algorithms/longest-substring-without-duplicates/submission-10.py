class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            current=1
            j=i+1
            while (j<len(s)) and (s[j] not in s[i:j]):
                current+=1
                j+=1
            if current>res:
                res=current
        return res

