from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len = float('inf')
        
        missing = len(t)
        need = Counter(t)

        left = 0

        for right in range(len(s)):
            if need[s[right]] > 0:
                missing -= 1

            need[s[right]] -= 1

            while missing == 0:
                if right - left + 1 < min_len:
                    start = left
                    min_len = right - left + 1

                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1

                left += 1

        return "" if min_len == float('inf') else s[start : start + min_len]