class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower() 
        i=0
        w=len(s)-1
        while i<w:
            while i<w and not s[i].isalnum():
                i+=1
            while w>i and not s[w].isalnum():
                w-=1
            if s[i] != s[w]:
                return False
            i+=1
            w-=1
        return True