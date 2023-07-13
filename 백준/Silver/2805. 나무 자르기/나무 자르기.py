import sys
input = sys.stdin.readline

n,m = map(int,input().split())
tree = list(map(int,input().split()))

start = 0
end = max(tree)
mid = (start + end)//2

while start<=end:
    total = 0
    for t in tree:
        length = t-mid
        if length > 0:
            total += length

    if total > m:
        start = mid + 1
    elif total < m:
        end = mid - 1
    else:
        break

    mid = (start+end)//2

print(mid) 