# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals == []:
            return []
        intervals.sort(key=lambda x: x.start)
        result = []
        current = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i].start <= current.end:
                current.end = max(intervals[i].end, current.end)
            else:
                result.append(current)
                current = intervals[i]
        result.append(current)
        return result
