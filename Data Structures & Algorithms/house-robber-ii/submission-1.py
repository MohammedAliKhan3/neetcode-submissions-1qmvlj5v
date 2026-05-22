class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        elif len(nums) == 0:
            return []
        
        rob1, rob2 = 0, 0
        
        for i in range(1,len(nums)):
            temp = max(nums[i] + rob1 , rob2)
            rob1 = rob2
            rob2 = temp

        rob01, rob02 = 0, 0

        for j in range(len(nums)-1):
            temp = max(nums[j] + rob01 , rob02)
            rob01 = rob02
            rob02 = temp

        return max(rob2, rob02)