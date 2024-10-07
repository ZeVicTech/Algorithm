import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
t = 0
while True:
    t += 1
    n = int(input())
    if n == 0:
        break
    distance = [[INF]*n for _ in range(n)]
    graph = [list(map(int, input().split())) for _ in range(n)]

    distance[0][0] = graph[0][0]
    q = []
    heapq.heappush(q, (distance[0][0], (0,0)))

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    while q:
        dist, node = heapq.heappop(q)
        node_x, node_y = node

        if distance[node_x][node_y] < dist:
            continue

        for i in range(4):
            nx = node_x + dx[i]
            ny = node_y + dy[i]

            if not(0 <= nx <= n-1) or not(0 <= ny <= n-1):
                continue

            cost = graph[nx][ny]
            if dist + cost < distance[nx][ny]:
                heapq.heappush(q, (dist + cost, (nx, ny)))
                distance[nx][ny] = dist + cost
    
    print(f"Problem {t}: {distance[n-1][n-1]}")


