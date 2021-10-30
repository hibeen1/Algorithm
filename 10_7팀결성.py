import sys
import time
import random


# a번 학생의 있는 팀 찾기
def find_team(a):
  # 루트 노드가 아니면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if team[a] != a:
        team[a] = find_team(team[a])
    return team[a]

# a와 b의 팀 합치기


def union_team(a, b):
    a = find_team(a)
    b = find_team(b)
    if a > b:
        team[a] = b
    else:
        team[b] = a


n, m = map(int, input().split())

team = [0] * (n + 1)
# 처음에는 서로 다른 팀으로 구분되어 총 N + 1개 팀이 존재한다.
start = time.time()
for i in range(n + 1):
    team[i] = i

for _ in range(m):
    # op, a, b = map(int, input().split())
    op = random.randint(0,1)
    a = random.randint(1, n)
    b = random.randint(1, n)
    

  # '팀 합치기' 연산
    if op == 0:
        union_team(a, b)
  # '같은 팀 여부 확인' 연산
    elif op == 1:
        if find_team(a) == find_team(b):
            print("YES")
        else:
            print("NO")
end = time.time()
print(end-start)




# def union(arr, a, b):
#     if is_union(arr, a, b):
#         return
#     else:
#         arr.append((a, b))

# def is_union(arr, a, b):
#     if ((a, b) or (b, a)) in arr:
#         return True
#     else:
#         return False

# input = sys.stdin.readline


# n, m = map(int, input().split())
# temp = []
# result = []

# start = time.time()
# for _ in range(m):
#     # calc, a, b = map(int, input().split())
#     calc = random.randint(0,1)
#     a = random.randint(1, n)
#     b = random.randint(1, n)
#     if calc == 0:
#         union(temp, a, b)
#     elif calc == 1:
#         if is_union(temp, a, b):
#             result.append("YES")
#         else:
#             result.append("NO")
# for i in result:
#     print(i)
# end = time.time()
# print(end-start)


# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1

# No
# NO
# YES
