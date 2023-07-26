import sys
input = sys.stdin.readline

n = int(input())
maze = list(map(int,input().split()))
dp = [1000]*n
dp[0] = 0
for i in range(n):
    for j in range(i+1,i + maze[i] + 1):
        if j == n:
            break
        dp[j] = min(dp[j], dp[i]+1)

if dp[n-1] == 1000:
    print(-1)
else:
    print(dp[n-1])