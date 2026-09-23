class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        n = len(intervals)

        intervals.sort(key=lambda x: x[0])

        newIntervals = []

        prevEnd = float('inf')

        for interval in intervals:
            if not newIntervals or newIntervals[-1][1] <= interval[0]:
                newIntervals.append(interval)
                prevEnd = interval[1]
            else:
                if interval[1] < newIntervals[-1][1]:
                    newIntervals[-1] = interval
        
        return n - len(newIntervals)


    # sort by start

    # prevEnd = ???

    # for each interval:
    #     if it doesn't overlap:
    #         keep it
    #     else:
    #         remove one
    #         make sure prevEnd is the SMALLER ending point


