class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        counter = dict()

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        return sorted(counter, key=lambda x : counter[x], reverse=True)[:k]