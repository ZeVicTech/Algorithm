import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    day = int(input())
    stock = list(map(int, input().split()))
    high = 0
    total = 0
    for i in range(day-1,-1,-1):
        if high <= stock[i]:
            high = stock[i]
        else:
            total += high - stock[i]
    
    print(total)