class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sorted_nums = list(sorted(set(nums)))
        cb = 0
        count=1
        if len(sorted_nums)==1:
            return 1
        for i in range(len(sorted_nums)-1):
            if sorted_nums[i+1] - sorted_nums[i]==1:
                count+=1
            else:
                count = 1
            if count>cb:
                cb=count
        return cb