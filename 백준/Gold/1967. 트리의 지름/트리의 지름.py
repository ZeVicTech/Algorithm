from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[]*(n+1) for i in range(n+1)]


for i in range(n-1):
    p,c,w = map(int,input().split())
    graph[p].append((c,w))
    graph[c].append((p,w))

def bfs(start):
    visited = [0]*(n+1)
    distance = [0]*(n+1)
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        node = q.popleft()
        for c,w in graph[node]:
            # 방문한 노드일 경우 건너뜀
            if visited[c] == 1:
                continue
            q.append(c)
            visited[c] = 1
            distance[c] = distance[node] + w

    return distance

distance = bfs(1)
node = distance.index(max(distance))
distance = bfs(node)

print(max(distance))