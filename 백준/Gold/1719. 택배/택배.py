import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, time = map(int, input().rstrip().split())
    graph[start].append((time, end))
    graph[end].append((time, start))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for time, node in graph[now]:
            if dist + time >= distance[node]:
                continue
            distance[node] = dist + time
            route[node] = now
            heapq.heappush(q, (distance[node], node))

for i in range(1, n+1):  
    distance = [INF for _ in range(n+1)]
    route = [-1 for _ in range(n+1)]
    route[i] = i
    dijkstra(i)
    answer = ['-' for _ in range(n+1)]
    for j in range(1, n+1):
        if i == j:
            continue

        now = j
        while True:
            if route[now] == i:
                answer[j] = now
                break
            else:
                now = route[now]
    print(" ".join(map(str, answer[1:])))