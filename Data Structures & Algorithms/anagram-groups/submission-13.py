class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            SortedS = "".join(sorted(s))
            if SortedS not in res.keys():
                res[SortedS] = [s]
                continue
            res[SortedS].append(s)
        return list(res.values())