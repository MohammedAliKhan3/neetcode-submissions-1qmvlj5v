class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper = {}
        for i in range(len(nums)):
            if nums[i] in mapper:
                mapper[nums[i]] += 1
            else:
                mapper[nums[i]] = 1

        result = sorted(mapper, key=mapper.get, reverse=True)[:k]
        return result

            