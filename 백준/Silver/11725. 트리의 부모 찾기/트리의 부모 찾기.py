from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
parent = [-1]*(n+1)

for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    parent[start] = 1

    while q:
        value = q.popleft()

        for i in graph[value]:
            if visited[i] == 1:
                continue
            q.append(i)
            visited[i] = 1
            parent[i] = value

bfs(1)
for i in range(2,n+1):
    print(parent[i])