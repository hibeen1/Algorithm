def my_code():
    n = int(input())
    numbers = []
    for i in range(n):
        numbers.append(int(input()))
    max_num = max(numbers)
    fibo = []
    if max_num == 0:
        fibo.append([0, [1, 0]])
    elif max_num == 1:
        fibo.append([0, [1, 0]])
        fibo.append([0, [0, 1]])
    else:
        fibo = [[0] for _ in range(max_num + 1)]
        fibo[0].append([1, 0])
        fibo[1].append([0, 1])
        fibo[1][0] = 1

    def fibonacci(n):
        if len(fibo[n]) > 1:
            return fibo[n]
        else:
            a, b = fibonacci(n-1), fibonacci(n-2)
            if len(fibo[n]) == 1:
                fibo[n].append([a[1][0] + b[1][0], a[1][1] + b[1][1]])
                fibo[n][0] = a[0] + b[0]
            return fibo[n]

    if max_num > 1:
        fibonacci(max_num)
    for i in numbers:
        print(fibo[i][1][0], fibo[i][1][1])



import sys
def best_code():
    T = int(input())
    dp = [[1,0], [0,1]]
    q = [int(sys.stdin.readline()) for _ in range(T)]

    for i in range(2,max(q)+1):
        dp.append([dp[i-2][0]+dp[i-1][0], dp[i-2][1]+dp[i-1][1]])
    for i in q:
        print(dp[i][0], dp[i][1])
