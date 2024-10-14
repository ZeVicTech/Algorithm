import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, d = map(int, input().split())
graph = [[] for _ in range(d + 1)]
distance = [INF for _ in range(d + 1)]

for i in range(d):
    graph[i].append((i + 1, 1))

for _ in range(n):
    start, end, dist = map(int, input().split())
    if end > d:
        continue
    graph[start].append((end, dist))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for node, value in graph[now]:
            if dist + value < distance[node]:
                distance[node] = dist + value
                heapq.heappush(q, (distance[node], node))

dijkstra(0)
print(distance[d])

