class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list1 = []
        for i in range(len(nums)):
            dummy = nums[i]
            for j in range(len(nums)):
                if (target - dummy) == nums[j] and j != i:
                    list1.append(i)
                    list1.append(j)
                    return list1

        return list1