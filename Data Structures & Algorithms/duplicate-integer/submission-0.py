class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            target = nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == target:
                    return True
            
        return False
