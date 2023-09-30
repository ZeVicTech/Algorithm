import heapq

def dijkstra(start, graph, dp):
    heap = []
    heapq.heappush(heap,(0,start))
    dp[start] = 0

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dp[node]:
            continue
        for item in graph[node]:
            if item[1] + cost < dp[item[0]]:
                dp[item[0]] = item[1] + cost
                heapq.heappush(heap,(dp[item[0]],item[0]))
    return dp



n,m,x = map(int,input().split())
INF = int(1e9)
graph = [[] for _ in range(m+1)]
dp = [INF] * (n+1)
distance = [0]*(n+1)

for _ in range(m):
    a,b,t = map(int,input().split())
    graph[a].append((b,t)) # 도착마을과 비용 순


for i in range(1,n+1):
    result = dijkstra(i,[item[:] for item in graph],dp[:])
    if i == x:
        for j in range(1,n+1):
            distance[j] += result[j]
    else:
        distance[i] += result[x]
print(max(distance[1:]))