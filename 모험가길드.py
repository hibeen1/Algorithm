from coding import random_List
# 내 풀이
# n = int(input())
# arr = map(int, input().split())
n = 100000
arr = random_List(n, 1, n)
result = 0

arr = sorted(arr, reverse=True)
cnt = 0

while arr:
    # print(arr, cnt)
    temp = arr.pop()
    if temp == 1:
        # print(temp, "겟또!")
        result += 1
        continue
    else:
        if temp > len(arr) + 1 + cnt:
            break
        if temp <= temp:
            cnt += 1    
            if temp == cnt:
                # print(temp, "겟또!")
                result += 1
                cnt = 0
print(result)



# 책 풀이
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# result = 0  # 총 그룹의 수
# count = 0 # 현재 그룹에 포함된 모험가의 수

# for i in data:  # 공포도를 낮은 것부터 하나씩 확인하며
#     count += 1  # 현재 그룹에 해당 모험가를 포함시키기
#     if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 -> 그룹 결성
#         result += 1 # 총 그룹의 수 증가시키기
#         count = 0   # 현재 그룹에 포함된 모험가의 수 초기화

# print(result)   # 총 그룹의 수 출력
    

# 27
# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 6 6 6 6 6 6 7 7 7 7 7 7 
# 6

# 5
# 2 3 1 2 2
# 2

# 20
# 1 2 2 3 3 3 4 4 4 5 5 5 5 6 6 6 6 6 6 
# 5