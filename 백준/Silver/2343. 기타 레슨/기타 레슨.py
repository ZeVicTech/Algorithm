import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lectures = list(map(int, input().split()))

def divide_bluerays(standard):
    temp = 0
    count = 1
    for i in range(n):
        if temp + lectures[i] > standard:
            temp = lectures[i]
            count += 1
        else:
            temp += lectures[i]

    return count

left, right = max(lectures), sum(lectures)

while left <= right:
    mid = (left + right) // 2

    if divide_bluerays(mid) <= m:
        right = mid - 1
        result = mid
    else:
        left = mid + 1

print(result)

    
