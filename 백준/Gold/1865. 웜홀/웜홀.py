import sys
input = sys.stdin.readline
INF = int(1e9)

tc = int(input())

def bf(start):

    distance[start] = 0

    for i in range(n):
        for j in range(len(edges)):
            cur_node=edges[j][0]
            next_node=edges[j][1]
            edge_cost=edges[j][2]

            if distance[next_node] > distance[cur_node]+edge_cost:
                distance[next_node]=distance[cur_node]+edge_cost

                if i == n-1:
                    return 'YES'
                
    return 'NO'

for _ in range(tc):
    n,m,w = map(int,input().split())
    distance = [INF]*(n+1)
    edges = []
    for i in range(m):
        s,e,t = map(int,input().split())
        edges.append((s,e,t))
        edges.append((e,s,t))
    for i in range(w):
        s,e,t = map(int,input().split())
        edges.append((s,e,-t))

    print(bf(1))