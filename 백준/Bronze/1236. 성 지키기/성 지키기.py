import sys
input = sys.stdin.readline

n, m = map(int, input().split())
castle = [input().rstrip() for _ in range(n)]

empty_rows = sum(1 for i in range(n) if 'X' not in castle[i])
empty_cols = 0
for i in range(m):
    flag  = 0
    for j in range(n):
        if castle[j][i] == 'X':
            flag = 1
    if flag == 0:
        empty_cols += 1

print(max(empty_rows, empty_cols))