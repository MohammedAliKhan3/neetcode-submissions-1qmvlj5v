class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            x = stones.pop(stones.index(max(stones)))
            y = stones.pop(stones.index(max(stones)))

            if x < y:
                stones.append(y - x)

            else:
                stones.append(x - y)

        return stones[0]