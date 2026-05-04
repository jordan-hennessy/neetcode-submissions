class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = defaultdict()

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        return sorted(counter, key=lambda x : counter[x], reverse=True)[:k]