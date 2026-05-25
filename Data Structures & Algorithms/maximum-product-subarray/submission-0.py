class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curMax = nums[0]
        curMin = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]

            tempMax = max( n , n * curMax , n * curMin) 
            curMin = min( n , n * curMax , n * curMin) 
            curMax = tempMax

            res = max(res, curMax)

        return res