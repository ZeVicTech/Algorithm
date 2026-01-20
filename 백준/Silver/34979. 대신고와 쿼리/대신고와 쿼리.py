def execute_construction(school, floor, group):
    school[floor][group] += 1

    d_floor = [0, 1, 0, -1]
    d_group = [1, 0, -1, 0]

    for i in range(4):
        if 0 > floor + d_floor[i] or floor + d_floor[i] > 3:
            continue
        if 0 > group + d_group[i] or group + d_group[i] > n-1:
            continue
        school[floor + d_floor[i]][group+d_group[i]] += 1

n, q = map(int, input().split())

school = [list(0 for i in range(n)) for j in range(4)]

for _ in range(q):
    order = list(map(int, input().split()))

    if order[0] == 1:
        floor, group = order[1:]
        execute_construction(school, floor - 1, group - 1)
    else:
        floor = order[-1]
        max_displeasure = max(school[floor-1])
        print(school[floor-1].index(max_displeasure)+1)

max_displeasure = max(max(row) for row in school)
check = 0
for i in range(4):
    for j in range(n):
        if school[i][j] == max_displeasure:
            print(i+1, j+1)
            check = 1
            break
    if check == 1:
        break