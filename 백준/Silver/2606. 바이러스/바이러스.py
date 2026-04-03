import sys
from collections import deque
sys.stdin.readline

n = int(input())
pair = int(input())

network = [[] for _ in range(n+1)]

for _ in range(pair):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

def bfs(start):
    global visited
    q = deque()
    q.append(start)
    visitied[start] = 1
    cnt = 0

    while q:
        node = q.popleft()
        for new in network[node]:
            if visitied[new]:
                continue
            q.append(new)
            visitied[new] = 1
            cnt += 1

    return cnt

visitied = [0 for _ in range(n+1)]
print(bfs(1))
