class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        zero_count=0
        total = 1
        for num in nums:
            total *= num
            if num == 0:
                zero_count += 1
        for num in nums:
            if num != 0:
                result.append(int(total/num))
            else:
                if zero_count == 1:
                    total_no_zero =1
                    for num in nums:
                        if num != 0:
                            total_no_zero *= num
                    result.append(int(total_no_zero))
                else: 
                    result.append(0)
        return result