import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

q = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(a, b, visited, graph):
    q.append((a,b))
    visited[a][b] = 1
    union = [(a,b)]
    total = graph[a][b]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not(0 <= nx < n and 0 <= ny < n):
                continue
            if visited[nx][ny] == 1:
                continue
            if not(l <= abs(graph[x][y] - graph[nx][ny]) <= r):
                continue
            q.append((nx, ny))
            visited[nx][ny] = 1
            union.append((nx,ny))
            total += graph[nx][ny]

    return union, total//len(union)

day = 0
while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                continue
            cnt += 1
            union, population = bfs(i, j, visited, graph)
            for x,y in union:
                graph[x][y] = population
    if cnt == n*n:
        print(day)
        break
    day += 1