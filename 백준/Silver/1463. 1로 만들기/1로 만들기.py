import sys
input = sys.stdin.readline

x = int(input())
dp = [0]*(x+1)

for i in range(1,x+1):

    if i == 1: # 1일경우에는 연산이 필요없음
        dp[i] = 0
        continue

    dp[i] = dp[i-1] + 1 #처음에는 1를 뺀경우를 할당

    # i가 3으로 나누어 떨어지면 나눈 몫을 인덱스로 가지는 dp테이블 값과 비교
    if i % 3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)

    # i가 2으로 나누어 떨어지면 나눈 몫을 인덱스로 가지는 dp테이블 값과 비교
    if i % 2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)

print(dp[x])