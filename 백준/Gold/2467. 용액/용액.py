import sys
input = sys.stdin.readline

n = int(input())
solution = list(map(int, input().split()))

left, right  = 0, n-1
value = abs(solution[left] + solution[right])
answer = [solution[left], solution[right]]

while left < right:
    now = solution[left] + solution[right]
    if value > abs(now):
        value = abs(now)
        answer = [solution[left], solution[right]]
        if value == 0:
            break
    
    if now < 0:
        left += 1
    else:
        right -= 1

print(*answer)
