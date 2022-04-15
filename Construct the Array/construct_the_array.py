def countArray(n, k, x):
    # Return the number of ways to fill in the array.
    
    # a = i번째 순서에서 x로 끝나는 경우의 수
    # b = i번째 순서에서 x로 끝나지 않는 경우의 수
    a = [0] * n
    b = [0] * n
    
    for i in range(1, n):
        a[i] = b[i-1] 
        #  b는 이전에 x로 끝나는 경우 현재 x 를 제외한 나머지의 경우의 수 + x로 끝나지 않는 경우 x와 이전의 자신을 제외 한 경우의 수
        b[i] = a[i-1] * (k-1) + b[i-1] * (k-2)

    return a[i]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = int(first_multiple_input[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()