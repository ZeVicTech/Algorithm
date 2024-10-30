import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

def prim(start):
    visited[start] = 1
    q = graph[start][:]
    heapq.heapify(q)

    total_distance = 0
    max_distance = 0
    while q:
        now_cost, now_node = heapq.heappop(q)
        if visited[now_node] == 1:
            continue

        visited[now_node] = 1
        total_distance += now_cost
        max_distance = max(max_distance, now_cost)
        
        for edge in graph[now_node]:
            new_cost, new_node = edge
            if visited[new_node] == 1:
                continue
            heapq.heappush(q, edge)

    return total_distance - max_distance

result = prim(1)

print(result)