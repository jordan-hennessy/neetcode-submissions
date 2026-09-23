class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        n = len(intervals)

        # -- Insert -- 
        for i in range(n):
            if newInterval[0] <= intervals[i][0]:
                intervals.insert(i, newInterval)
                break
            
        # If 'newInterval' doesn't get inserted, add to end
        if len(intervals) == n:
            intervals.append(newInterval)

        # -- Merge --

        re_intervals = []

        for interval in intervals:
            if not re_intervals or re_intervals[-1][1] < interval[0]:
                re_intervals.append(interval) 
            else:
                re_intervals[-1] = [re_intervals[-1][0], max(interval[1], re_intervals[-1][1])]
        
        return re_intervals