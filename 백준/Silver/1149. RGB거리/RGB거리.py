n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

r = [0]*n
g = [0]*n
b = [0]*n

r[0],g[0],b[0]  = graph[0][0],graph[0][1],graph[0][2]

for i in range(1,n):
    r[i] = graph[i][0] + min(g[i-1],b[i-1])
    g[i] = graph[i][1] + min(r[i-1],b[i-1])
    b[i] = graph[i][2] + min(r[i-1],g[i-1])

print(min(r[n-1],g[n-1],b[n-1]))