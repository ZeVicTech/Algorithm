import sys
input = sys.stdin.readline

n, c = map(int, input().rstrip().split())
houses = [int(input()) for _ in range(n)]
houses.sort()
answer = 0

start, end = 1, houses[-1] - houses[0]
while start <= end:
    mid = (start + end)//2
    cur = houses[0]
    count = 1
    for i in range(1, n):
        dist = houses[i]-cur
        if dist < mid:
            continue
        cur = houses[i]
        count += 1

    if count >= c:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1
    
print(answer)