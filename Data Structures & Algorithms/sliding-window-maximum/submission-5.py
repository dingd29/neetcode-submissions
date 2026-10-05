class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()   # stores indices
        res = []

        for i in range(len(nums)):

            # remove out-of-window elements
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # maintain decreasing order
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

            # record result once window formed
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res