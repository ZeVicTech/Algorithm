import sys
from collections import deque
input = sys.stdin.readline

s = input().rstrip()

zero_count = s.count('0')//2
one_count = s.count('1')//2

temp = []
count = 0
for i in range(len(s)):
    if s[i] == '1' and count < one_count:
        count += 1
        continue
    temp.append(s[i])

answer = deque()
count = 0
for i in range(len(temp)-1, -1, -1):
    if temp[i] == '0' and count < zero_count:
        count += 1
        continue
    answer.appendleft(temp[i])

print("".join(answer))