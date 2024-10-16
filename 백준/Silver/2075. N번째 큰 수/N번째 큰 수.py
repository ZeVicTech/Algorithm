import sys
import heapq
input = sys.stdin.readline

n = int(input())

q = []

for _ in range(n):
    row = list(map(int, input().split()))
    for r in row:
        if len(q) < n:
            heapq.heappush(q, r)
        else:
            if q[0] < r:
                heapq.heappop(q)
                heapq.heappush(q, r)

print(q[0])