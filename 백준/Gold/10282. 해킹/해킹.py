import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] == dist:
            for node in graph[now]:
                if distance[node[0]] <= node[1] + dist:
                    continue
                distance[node[0]] = node[1] + dist
                heapq.heappush(q, (distance[node[0]], node[0]))

t = int(input())

for _ in range(t):
    n, d, c = map(int, input().split())

    distance = [INF] * (n+1)
    # 그래프 작성
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    
    dijkstra(c)

    infect = 0
    time = 0

    for i in range(1,n+1):
        if distance[i] == INF:
            continue
        infect += 1
        time = max(distance[i], time)

    print(infect, time)
