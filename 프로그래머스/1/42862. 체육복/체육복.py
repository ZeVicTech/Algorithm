def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    student = [1 for _ in range(n)]
    
    for l in lost:
        student[l-1] -= 1
        
    for r in reserve:
        student[r-1] += 1
        
    for i in range(n):
        if student[i] == 2:
            if i - 1 >= 0 and student[i-1] == 0:
                student[i-1] += 1
                student[i] -= 1
            elif i + 1 <= n - 1 and student[i+1] == 0:
                student[i+1] += 1
                student[i] -= 1
            else:
                continue
        
    return n - student.count(0)