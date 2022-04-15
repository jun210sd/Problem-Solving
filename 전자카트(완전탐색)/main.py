import sys

sys.stdin = open("sample_input.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def search(n, prev, cur, sum, matrix, visited):

    sum += matrix[prev][cur] 

    if n == 1:
        sum += matrix[cur][0] 
        return sum
    else:        
        

        min_val = 1e19
        for i in range(1, N):
            if (i != cur) and (i not in visited):                
                visited.append(cur)
                min_val = min(min_val, search(n-1, cur, i, sum, matrix, visited))
                visited.remove(cur)

        return min_val


for test_case in range(1, T + 1):
    N = int(input())

    matrix = []
    visited = []
    for i in range(N):
        lines = list(map(int, input().split()))
        matrix.append(lines)

    res = 1e19
    for i in range(1, N):
        res = min(res, search(N-1, 0, i, 0, matrix, visited))
    print(res)

    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
