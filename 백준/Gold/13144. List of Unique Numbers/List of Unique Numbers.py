import sys
input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))

answer = 0
element_set = set()
left, right = 0, 0
while left < n and right < n:
    if not sequence[right] in element_set:
        element_set.add(sequence[right])
        right += 1
        answer += (right-left)
    else:
        element_set.remove(sequence[left])
        left += 1

print(answer)

