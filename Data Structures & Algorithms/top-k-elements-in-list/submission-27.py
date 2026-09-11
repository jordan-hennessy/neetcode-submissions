class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = dict()

        for i in nums:
            counter[i] = counter.get(i, 0) + 1

        # nums = [1,2,2,2,3,3,3], k = 2
        # counter = {1 : 1, 2 : 3, 3 : 3}

        return sorted(counter, key=lambda x: counter[x], reverse=True)[:k]