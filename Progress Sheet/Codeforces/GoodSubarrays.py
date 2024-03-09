from collections import defaultdict


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input()))
    dist = defaultdict(int)
    dist[0] = 1
    total = 0
    ans = 0
    pre = []
    for i in range(len(arr)):
        total += arr[i]
        pre.append(total)
   
    for i in range(len(pre)):
        
        if (pre[i] - (i+1)) in dist:
            ans += dist[pre[i] - (i+1)]
        dist[pre[i] - (i+1)] += 1
    print(ans)