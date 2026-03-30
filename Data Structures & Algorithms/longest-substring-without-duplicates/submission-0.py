class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = 0
        max_length = 0
        result = []

        for char in s:
            while char in result:
                result.pop(0)

            result.append(char)
            max_length = max(max_length,len(result))

        return max_length