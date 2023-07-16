def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        x = numbers[i]
        target = 1
        while True:
            if x%2 == 0:
                if target == 1:
                    answer.append(numbers[i]+target)
                else:
                    answer.append(numbers[i]+target-target//2)
                break
            x = x//2
            target *= 2

    return answer