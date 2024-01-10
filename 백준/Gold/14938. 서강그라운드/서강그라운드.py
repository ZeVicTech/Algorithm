import sys
import heapq
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

n, m, r = map(int, input().split())
region = deque(map(int, input().split()))
region.appendleft(0)# 인덱스 번호가 지역의 위치 번호가 되도록 0번 인덱스에 더미값 추가
graph = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return distance

def calculate_item(start):

    distance = dijkstra(start)
    total = 0
    for index, dist in enumerate(distance):
        if index == 0 or dist > m:
            continue
        total += region[index]

    return total

result = 0
for i in range(1,n+1):
    result = max(calculate_item(i),result)

print(result)
