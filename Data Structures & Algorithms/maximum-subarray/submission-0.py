class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        maximum_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], nums[i] + current_sum)
            maximum_sum = max(maximum_sum, current_sum)

        return maximum_sum