class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = dict()

        for num in nums:
            count[num] = count.get(num, 0) + 1

        sorted_count = sorted(count.items(), key=lambda x:x[1], reverse=True)

        sol = []

        counter = 0

        while counter < k:
            sol.append(sorted_count[counter][0])
            counter += 1
        
        return sol