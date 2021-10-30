import time

# 내가 생각한 방법 :
#     6자리 고정 숫자를 만들어서.
#     일단 1씩 더하는데,
#     그걸 다시 문자열로 바궈서 3 있는 지 체크.

# 답지 방법 :


n = int(input())

start_time = time.time()

cnt = 0
for hour in range(n + 1):
    for minute in range(60):
        for second in range(60):
            if '3' in str(hour) + str(minute) + str(second):
                cnt += 1

print(cnt)

end_time = time.time()
print("실행 시간 : ", end_time-start_time)
