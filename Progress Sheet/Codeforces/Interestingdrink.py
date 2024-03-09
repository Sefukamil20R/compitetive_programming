from bisect import bisect_right

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

queries = int(input())

def binary(arr, q):
    idx = bisect_right(arr, q)
    
    return idx
ans = []
for i in range(queries):
    s = int(input())
    ans.append(s)

for x in ans:
    val = binary(arr, x)
    print(val)