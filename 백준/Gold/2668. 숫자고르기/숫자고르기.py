import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
graph = [0 for _ in range(n + 1)]

for i in range(1, n+1):
    element = int(input())
    graph[i] = element

def dfs(start, now):
    visited[now] = True
    v = graph[now]
    if visited[v]:
        if v == start:
            answer.append(start)
    else:
        dfs(start, v)

answer = []
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    dfs(i, i)

answer.sort()
print(len(answer))
for item in answer:
    print(item)