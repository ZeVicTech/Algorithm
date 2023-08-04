import sys
input = sys.stdin.readline

n = int(input())
schedule = [0] # 0번째 인덱스에 더미값 주입
dp = [0]*(n+1) # dp[i]는 i일 다음날 얻게되는 최대 금액

for _ in range(n):
    t,p = map(int,input().split())
    schedule.append((t,p))

for i in range(1,n+1):
    t,p = schedule[i][0],schedule[i][1]
    dp[i] = max(dp[i],dp[i-1])
    dead_line = i+t-1 # i일에 시작한 상담이 끝나는 날
    if dead_line <= n:
        dp[dead_line] = max(dp[i-1]+p,dp[dead_line])

print(dp[n])
