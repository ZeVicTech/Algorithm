import sys
input = sys.stdin.readline

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def sqrt_matrix(num):

    # 재귀 종료조건
    if num == 1:
        return matrix
    
    remain = num % 2
    num = num//2
    temp = sqrt_matrix(num)
    result = mul_matrix(temp, temp)

    if remain == 0:
        return result
    else:
        return mul_matrix(result, matrix)

def mul_matrix(matrix_a, matrix_b):
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp = 0
            for k in range(n):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j] % 1000

    return result

result = sqrt_matrix(b)

for i in range(n):
    for j in range(n):
        print(result[i][j]%1000, end=' ')
    print()