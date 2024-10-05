import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

visited = [0] * 100001

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        node = q.popleft()
        if node-1 >= 0:
            if visited[node-1] == 0 or visited[node-1] > visited[node] + 1:
                q.append(node-1)
                visited[node-1] = visited[node] + 1

        if node+1 <= 100000:
            if visited[node+1] == 0 or visited[node+1] > visited[node] + 1:
                q.append(node+1)
                visited[node+1] = visited[node] + 1

        if 2*node <= 100000:
            if visited[2*node] == 0 or visited[2*node] > visited[node]:
                q.append(2*node)
                visited[2*node] = visited[node]

bfs(n)
print(visited[k]-1)

