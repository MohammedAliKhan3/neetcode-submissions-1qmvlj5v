class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_cap = 0
        area = 0

        left = 0
        right = len(heights) - 1

        while right > left:
            area = min(heights[left],heights[right]) * (right - left)

            max_cap = max(max_cap,area)

            if heights[left] > heights[right]:
                right -= 1

            else:
                left += 1

        return max_cap