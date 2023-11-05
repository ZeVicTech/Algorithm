import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v,e = map(int,input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF]*(v+1)

for i in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))

    while q:
        dist,now = heapq.heappop(q)
        if dist > distance[now]:
            continue

        for node in graph[now]:
            cost = dist + node[1]
            if cost >= distance[node[0]]:
                continue
            distance[node[0]] = cost
            heapq.heappush(q,(cost,node[0]))

dijkstra(start)

for i in range(v):
    if distance[i+1] == INF:
        print("INF")
    else:
        print(distance[i+1])