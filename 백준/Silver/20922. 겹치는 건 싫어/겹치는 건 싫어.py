import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
sequence = list(map(int, input().split()))
element_count = defaultdict(int)

answer = 0
left, right = 0, 0
while left < n and right < n:
    if element_count[sequence[right]] < k:
        element_count[sequence[right]] += 1
        right += 1
        answer = max(answer, right - left)
    else:
        while element_count[sequence[right]] >= k:
            element_count[sequence[left]] -= 1
            left += 1

print(answer)


