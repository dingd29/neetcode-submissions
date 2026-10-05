class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        min = 0
        max = len(nums)-1
        while True:
            index = min+(max-min)//2
            if nums[index] == target:
                return index
            if nums[index] > target:
                max = index -1
            elif nums[index] < target:
                min = index+1
 