class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1
        zero_count = nums.count(0)

        for n in nums:
            if n != 0:
                product *= n

        for n in nums:
            if zero_count > 1:
                result.append(0)

            elif zero_count == 1:
                if n == 0:
                    result.append(product)
                else:
                    result.append(0)

            else:
                result.append(product//n)

        return result