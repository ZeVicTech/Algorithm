def solution(book_time):
    for i in range(len(book_time)):
        for j in range(2):
            h, w = map(int, book_time[i][j].split(':'))
            if j == 0:
                book_time[i][j] = 60 * h + w
            else:
                book_time[i][j] = 60 * h + w + 10
            
    book_time.sort(key = lambda x: x[1])
    
    print(book_time)
    answer = 0
    for i in range(len(book_time)):
        count = 0
        for j in range(i, len(book_time)):
            if book_time[j][0] < book_time[i][1]:
                count += 1
        answer = max(answer, count)

    return answer