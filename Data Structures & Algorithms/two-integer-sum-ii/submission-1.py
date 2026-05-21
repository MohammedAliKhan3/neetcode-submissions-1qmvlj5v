class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            dummy = numbers[i]
            find = target - dummy

            found = self.binarySearch(find,numbers)

            if found is not None and  found != i:
                return [i+1 , found+1]

        return []


    def binarySearch(self,find,numbers):
        left = 0
        right = len(numbers) - 1

        while left <= right:
            mid = (left + right) // 2

            if numbers[mid] == find:
                return mid

            elif numbers[mid] > find:
                right = mid - 1

            else:
                left = mid + 1

        return None