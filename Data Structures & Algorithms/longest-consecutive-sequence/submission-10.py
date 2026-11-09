class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
        max = 0
        for num in s:
            if (num-1) not in s:
                i=1
                while True:
                    if num+i in s:
                        i+=1
                        continue
                    else:
                        break
                if i>max:
                    max = i
        return max
