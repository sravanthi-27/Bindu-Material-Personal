def insert_interval(intervals, newInterval):
    res = []
    i = 0
    n = len(intervals)

    # Add all intervals ending before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1

    # Merge all overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    res.append(newInterval)

    # Add remaining intervals
    while i < n:
        res.append(intervals[i])
        i += 1

    return res
#intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
