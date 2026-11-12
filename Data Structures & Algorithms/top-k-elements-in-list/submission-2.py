from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = defaultdict(list)

        for n in nums:
            key = n
            group[key].append(n)

        return sorted(group, key = lambda x : len(group[x]), reverse = True)[:k]