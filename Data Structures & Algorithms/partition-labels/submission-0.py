class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for index, char in enumerate(s):
            lastIndex[char] = index

        result = []
        sub_string_size = 0
        sub_string_end = 0

        for index, char in enumerate(s):
            sub_string_size += 1

            if lastIndex[char] > sub_string_end:
                sub_string_end = lastIndex[char]

            if index == sub_string_end:
                result.append(sub_string_size)
                sub_string_size = 0

        return result