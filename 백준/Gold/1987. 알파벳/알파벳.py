import sys
input = sys.stdin.readline

def dfs(r, c, visited, cnt, board, R, C):
    result = cnt

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1 ,0]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 > nr or nr >= R or 0 > nc or nc >= C:
            continue

        bit = bits[nr][nc]
        if bit & visited:
            continue
        result = max(result ,dfs(nr, nc, bit | visited, cnt + 1, board, R, C))

    return result

if __name__ == "__main__":
    R, C = map(int, input().split())
    board = []

    for i in range(R):
        temp = input().rstrip()
        board.append(temp)
        
    bits = [[1 << (ord(board[i][j]) - ord('A')) for j in range(C)] for i in range(R)]
    visited = 1 << (ord(board[0][0]) - ord('A'))
    result = dfs(0, 0, visited, 1, board, R, C)

    print(result)
