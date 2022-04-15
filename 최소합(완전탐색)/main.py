import sys
sys.stdin = open("sample_input.txt", "r")

def search(x, y, mat, buff, res, N):
    if x < 0 or y < 0 or x >= N or y >=N:
        return 1e19

    res = res + mat[y][x]

    if x == N-1 and y == N-1 :        
        return res    
    
    if buff[y][x] > res:
        buff[y][x] = res
        return min(search(x+1, y, mat, buff, res, N), search(x, y+1, mat, buff, res, N))
    else:
        return 1e19

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())

    buff = [[1e19] * N for i in range(N)]
    matrix = [ ]
    for i in range(N):
        matrix.append( list(map(int, input().split())) )         
    res = search(0, 0, matrix, buff, 0, N)
    print(res)