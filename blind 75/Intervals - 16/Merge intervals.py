from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        preend = intervals[0][1]
        start = intervals[0][0]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= preend:
                # Overlapping; update preend to the max end
                preend = max(preend, intervals[i][1])
            else:
                # No overlap; append previous merged interval
                res.append([start, preend])
                start = intervals[i][0]
                preend = intervals[i][1]
            

        # Append the last interval
        res.append([start, preend])
        return res
