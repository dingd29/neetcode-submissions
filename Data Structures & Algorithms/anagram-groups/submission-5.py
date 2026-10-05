class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        while(len(strs)>0):
            temp = [strs[0]]
            j=1
            while j<=len(strs)-1:
                if sorted(strs[0])==sorted(strs[j]):
                    temp.append(strs[j])
                    del strs[j]
                    j-=1
                j+=1
            result.append(temp)
            del strs[0]
        return result


        