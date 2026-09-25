"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key=lambda x: x.start)
        
        rooms = []

        # each entry is a room and its time it is free from
        # e.g. [10, 20]
        # 10: if a meeting starts after 10, it can take that room
        # 20: if a meeting starts after 20, it can take that room

        for interval in intervals:
            if rooms and interval.start >= rooms[0]:
                heapq.heappop(rooms)

            heapq.heappush(rooms, interval.end)

        return len(rooms)
