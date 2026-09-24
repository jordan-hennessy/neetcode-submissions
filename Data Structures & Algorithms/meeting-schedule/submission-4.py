"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        sortIntervals = sorted(intervals, key=lambda x: x.start)


        newIntervals = []

        for interval in sortIntervals:
            if not newIntervals:
                newIntervals.append(interval)
            elif newIntervals[-1].end > interval.start:
                return False
            else:
                newIntervals.append(interval)



        return True