import sys
import itertools
from pprint import pprint
input = sys.stdin.readline

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

def calculate(arr):
    dic = {}
    for item in arr:
        if item == 0:
            continue
        elif item in dic.keys():
            dic[item] += 1
        else:
            dic[item] = 1
    
    temp = list(dic.items())
    temp.sort(key = lambda x: (x[1],x[0]))
    temp = list(itertools.chain(*temp))
    arr = temp[:100]
    # print(arr)
    
    return len(arr), arr

cnt = 0
flag = 0
while True:

    if len(arr) > r-1 and len(arr[0]) > c-1 and arr[r-1][c-1] == k:
        print(cnt)
        break
    elif cnt > 100:
        print(-1)
        break

    cnt += 1
    # 열이 더 많을 때 전치
    if len(arr) < len(arr[0]):
        flag = 1
        arr = [list(row) for row in zip(*arr)]

    max_len = 0

    for i in range(len(arr)):
        arr_len, arr[i] = calculate(arr[i])
        max_len = max(arr_len, max_len)
    # pprint(arr)
    for i in range(len(arr)):
        for _ in range(max_len - len(arr[i])):
            arr[i].append(0)

    if flag == 1:
        flag = 0
        arr = [list(row) for row in zip(*arr)]

    # pprint(arr)
    