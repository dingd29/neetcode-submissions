class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = defaultdict(int)
        for num in nums:
            result[num]+=1
        result = sorted(result.items(), key = lambda item: item[1], reverse=True)
        return [item[0] for item in result[:k]]