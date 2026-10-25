class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = 0
        current_max = 0
        jump_count = 0

        for x in range(len(nums)-1):

            if x > max_reach:
                return False

            max_reach = max(max_reach, x + nums[x])

            if x == current_max:
                current_max = max_reach
                jump_count += 1

        
        return jump_count