class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range (len(nums)-2):
            for j in range (i+1, len(nums)-1):
                if 0-nums[i]-nums[j] in nums[j+1:]:
                    sort = sorted([nums[i], nums[j], nums[nums.index(0-nums[i]-nums[j])]])
                    if sort not in result:
                        result.append(sort)
        return result