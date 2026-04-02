class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        result = []

        for i in range(len(nums)):

            # remove out of window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # remove smaller elements
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # start recording after first window
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
        # result = []

        # for i in range(len(nums) - k + 1):
        #     window = nums[i:i+k]
        #     result.append(max(window))

        # return result