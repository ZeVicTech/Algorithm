import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dp = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        x,y,z = 0,0,0
        if i - 1 >= 0: # 위에서 오는 경우
            x = dp[i-1][j]
        if i - 1 >= 0 and j - 1 >= 0: # 대각선으로 오는 경우
            y = dp[i-1][j-1]
        if j - 1 >= 0: # 왼쪽에서 오는 경우
            z = dp[i][j-1]

        dp[i][j] += max(x,y,z)

print(dp[n-1][m-1])