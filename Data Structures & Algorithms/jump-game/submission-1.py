class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for x in range(len(nums)):

            if x > max_reach:
                return False

            max_reach = max(max_reach, x + nums[x])
            
            if max_reach >= len(nums):
                return True

        return True