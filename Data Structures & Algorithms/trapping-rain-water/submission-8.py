class Solution:
    def trap(self, height: List[int]) -> int:
        volume=0
        for i in range (len(height)):
            left_max= right_max = height[i]
            for j in range (i):
                left_max = max(left_max,height[j])
            for j in range (i+1, len(height)):
                right_max = max(right_max, height[j])
            if min(left_max, right_max)>height[i]:
                volume+=min(left_max,right_max) - height[i]
        return volume