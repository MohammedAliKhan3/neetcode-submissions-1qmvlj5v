class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            find = nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == find:
                    return find

        return False