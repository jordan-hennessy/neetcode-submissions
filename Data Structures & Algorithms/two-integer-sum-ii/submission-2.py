class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        setNums = set(numbers)

        for i, num in enumerate(numbers):
            newTarget = target - num
            if newTarget in setNums:
                j = numbers.index(newTarget)
                return [i + 1, j + 1]