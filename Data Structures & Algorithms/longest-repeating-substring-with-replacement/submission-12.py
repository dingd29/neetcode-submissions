class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        current=0
        for i in range(len(s)):
            l=k
            j=i+1
            count=1
            while (j<len(s)) and (l>0 or s[j]==s[i]):
                if s[j] != s[i]:
                    l-=1
                count+=1
                j+=1
            if l>0:
                j=i-1
                while (j>=0) and (l>0 or s[j]==s[i]):
                    if s[j] != s[i]:
                        l-=1
                    count+=1
                    j-=1
            current = max(current, count)
        
        return current
                