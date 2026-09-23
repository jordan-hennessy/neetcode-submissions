class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # must sort first
        intervals.sort(key=lambda x: x[0])
        
        # -- Merge --

        newIntervals = []

        for interval in intervals:
            if not newIntervals or newIntervals[-1][1] < interval[0]:
                newIntervals.append(interval)
            else:
                newIntervals[-1] = [newIntervals[-1][0], max(interval[1], newIntervals[-1][1])]

        return newIntervals