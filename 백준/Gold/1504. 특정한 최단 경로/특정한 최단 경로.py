import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,e = map(int,input().split())

graph = [[] for _ in range(n+1)]

for i in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2 = map(int,input().split())

def dijkstra(start,end):
    # start 정점에대한 초기 설정
    q = []
    distance = [INF]*(n+1)
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

    return distance[end]

route_1 = dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,n)
route_2 = dijkstra(1,v2)+dijkstra(v1,v2)+dijkstra(v1,n)


result = min(route_1, route_2)

print(result if result < INF else -1)