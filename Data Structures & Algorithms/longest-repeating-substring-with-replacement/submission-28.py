class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set()
        res=0
        for char in s:
            chars.add(char)
        for char in chars:
            count=l=0
            for i in range (len(s)):
                if s[i]==char:
                    count+=1
                while (i-l+1)>count+k:
                    if s[l] == char:
                        count -=1
                    l+=1
                res = max(res,i-l+1)
        return res
