import sys
input = sys.stdin.readline

name = input().rstrip()
n = int(input())
teams = [input().rstrip() for _ in range(n)]
teams.sort()
scores = []

for i in range(n):
    L = name.count('L') + teams[i].count('L')
    O = name.count('O') + teams[i].count('O')
    V = name.count('V') + teams[i].count('V')
    E = name.count('E') + teams[i].count('E')
    scores.append(((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100)

print(teams[scores.index(max(scores))])
