def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        x = numbers[i]
        temp = 1
        while True:
            if x%2 == 0:
                if temp == 1:
                    answer.append(numbers[i]+temp)
                else:
                    answer.append(numbers[i]+temp-temp//2)
                break
            x = x//2
            temp *= 2

    return answer