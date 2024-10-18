import sys
from collections import deque
input = sys.stdin.readline

s = input().rstrip()
m = int(input().rstrip())
l = len(s)

left_deque = deque(s)
right_deque = deque()

for _ in range(m):
    command = input().rstrip().split()
    if len(command) == 1:
        shortcut = command[0]
    else:
        shortcut, character = command

    if shortcut == 'L':
        if len(left_deque) == 0:
            continue
        tmp = left_deque.pop()
        right_deque.appendleft(tmp)
    elif shortcut == 'D':
        if len(right_deque) == 0:
            continue
        tmp = right_deque.popleft()
        left_deque.append(tmp)
    elif shortcut == 'B':
        if len(left_deque) == 0:
            continue
        left_deque.pop()
    else:
        left_deque.append(character)

print("".join(left_deque) + "".join(right_deque))