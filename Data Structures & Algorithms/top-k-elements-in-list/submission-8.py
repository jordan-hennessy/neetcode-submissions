class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        return sorted(counter, key=lambda x : counter[x], reverse=True)[:k]