class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1
        zero_count = nums.count(0)

        for x in nums:
            if x != 0:
                product *= x

        for x in nums:
            if zero_count > 1:
                result.append(0)

            elif zero_count == 1:
                if x == 0:
                    result.append(product)
                else:
                    result.append(0)

            else:
                result.append(product//x)

        
        return result
