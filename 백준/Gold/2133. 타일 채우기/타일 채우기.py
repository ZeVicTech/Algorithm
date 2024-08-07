import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (31)
dp[2] = 3

for i in range(4, 31):
    if i%2 == 0:
        dp[i] = dp[i-2] * 3 + sum(dp[:i-3])* 2 + 2

print(dp[n])