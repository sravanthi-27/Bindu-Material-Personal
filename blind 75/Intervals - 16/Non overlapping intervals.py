intervals = [(1,2),(2,3),(3,4),(1,3)]
ans = 0
intervals.sort(key=lambda x:x[1])
start, end = intervals[0]
for i in range(1,len(intervals)):
    if intervals[i][0] < end:
        ans+=1
    else:
        end = intervals[i][1]
print(ans)