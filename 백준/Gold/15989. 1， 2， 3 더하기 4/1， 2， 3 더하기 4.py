# 다이나믹 프로그래밍인 것은 파악했지만, 점화식을 세우지는 못했다.
# 하나의 식으로만 솔루션을 도출하려고 했던 것이 문제였다.
# 좀 더 넓게 보자

import sys
input = sys.stdin.readline

t = int(input())
# 모든 정수가 1로 초기화 되는 경우
dp = [1]*(10001)
dp[1] = 1

for i in range(2,10001):
    dp[i] += dp[i-2]

for i in range(3, 10001):
    dp[i] += dp[i-3]

for _ in range(t):
    n = int(input())
    print(dp[n])