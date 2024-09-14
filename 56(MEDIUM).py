intervals = [[1,3],[2,6],[8,10],[15,18]]
ans = []
intervals.sort(key = lambda interval: interval[0])

for interval in intervals:
    if not ans or ans[-1][1] < interval[0]:
        ans.append(interval)
    else:
        ans[-1] = [ans[-1][0], max(ans[-1][1], interval[1])]