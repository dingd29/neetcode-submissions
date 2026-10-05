class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def contains(window: str, target:str) -> bool:
            wdict=defaultdict(int)
            tdict=defaultdict(int)
            for char in window:
                wdict[char]+=1
            for char in target: 
                tdict[char]+=1
            for char in tdict.keys():
                if char not in wdict.keys():
                    return False
                elif tdict[char]>wdict[char]:
                    return False
            return True

        if not contains(s,t):
            return ''
        res = s
        for i in range (len(s)+1):
            l=0
            while contains(s[l:i],t):
                if len(res)>(i-l):
                    res = s[l:i]
                l+=1
        return res