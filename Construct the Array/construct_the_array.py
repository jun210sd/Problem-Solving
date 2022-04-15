

# 1 -> 2 -> 1 -> 2
# 1 -> 2 -> 1 -> 3

# 1 -> 2 -> 3 -> 1
# 1 -> 2 -> 3 -> 2

# 1 -> 3 -> 1 -> 3
# 1 -> 3 -> 1 -> 2

# 1 -> 3 -> 2 -> 1
# 1 -> 3 -> 2 -> 3

# an = i번째 순서에서 x로 끝나는 경우의 수를 저장한 배열
# bn = i번째 순서에서 x로 끝나지 않는 경우의 수를 저장한 배열

# 먄약 x가 2인 경우:
# a[n] = [0, 1, 1, 3]
# b[n] = [1, 1, 3, 5]

def countArray(n, k, x):
    # Return the number of ways to fill in the array.    
    
    a = [0] * n
    b = [0] * n    
	
    a[0] = 1 if x==1 else 0
    b[0] = 0 if x==1 else 1
	
    mod = int(1e9 + 7)
	
    for i in range(1, n):
        # a는 이전 b의 경우의 수
        a[i] = b[i-1] % mod
		#  b는 이전에 x로 끝나는 경우 현재 x 를 제외한 나머지의 경우의 수 + x로 끝나지 않는 경우 x와 이전의 자신을 제외 한 경우의 수
        b[i] = (a[i-1] * (k-1) + b[i-1] * (k-2)) % mod

    return a[n-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = int(first_multiple_input[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()