import time
import random
import sys

sys.setrecursionlimit(10**9)

def random_List(size):
    result = []

    for v in range(size):
        result.append(random.randint(0,size))

    return result

n = 20000000
cards = random_List(n)
# cards = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


# 전통적인 선택정렬 O(N^2)
def selection_sort(cards):
    for i in range(len(cards)):
        for j in range(i+1, len(cards)):
            if cards[i] > cards[j]:
                cards[i], cards[j] = cards[j], cards[i]

# 파이썬 내장함수를 사용한 향상된 선택정렬 O(N^2) because min(n) -> O(N)
def selection_sort2(cards):
    for i in range(len(cards)):
        min_index = cards.index(min(cards[i:]))
        cards[i], cards[min_index] = cards[min_index], cards[i]


# 삽입정렬 O(N^2) -> 이미 데이터가 정렬되어 있는 경우 빠르게 작동
def insertion_sort(cards):
    for i in range(1, len(cards)):
        for j in range(i, 0, -1):
            if cards[j] < cards[j-1]:
                cards[j], cards[j-1] = cards[j-1], cards[j]
            else:
                break


# 퀵 정렬 평균 O(NlogN) 최악 O(N^2) -> 데이터가 이미 정렬이 되어 있는 경우
def quick_sort(cards, start, end):
    if start >= end:    # 원소가 1개인 경우 종료
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:    
        while left <= end and cards[left] <= cards[pivot]:  # 피벗보다 큰 데이터를 찾을 때까지 반복
            left += 1
        while right > start and cards[right] >= cards[pivot]:   # 피벗보다 작은 데이터를 찾을 때까지 반복
            right -= 1
        if left > right:    # 엇갈렸다면 작은 데이터와 피벗을 교체
            cards[right], cards[pivot] = cards[pivot], cards[right]
        else:   # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            cards[left], cards[right] = cards[right], cards[left]
    quick_sort(cards, start, right-1)   # 분할 이후 왼쪽과 오른쪽 부분에서 각각 정렬 재귀 수행
    quick_sort(cards, right+1, end)


def quick_sort2(cards):
    if len(cards) <= 1:
        return cards
    
    pivot = cards[0]
    tail = cards[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

# 계수 정렬. 일반적으로 max와 min의 차이가 백만을 넘지 않을 때 효과적. O(N+max)
def count_sort(cards):
    cnt = [0] * (max(cards) + 1)

    for i in range(len(cards)):
        cnt[cards[i]] += 1
    
    # del cards[:]
    for i in range(len(cnt)):
        for j in range(cnt[i]):
            cards.append(i)
    



# cards1 = cards
# a = time.time()
# selection_sort(cards1)
# b = time.time()
# print(b-a)


# cards2 = cards
# a = time.time()
# selection_sort2(cards2)
# b = time.time()
# print(b-a)


# cards3 = cards
# a = time.time()
# insertion_sort(cards3)
# b = time.time()
# print(b-a)

# cards4 = cards
# a = time.time()
# quick_sort(cards4, 0, len(cards4)-1)
# b = time.time()
# print(b-a)

# cards5 = cards
# a = time.time()
# quick_sort2(cards5)
# b = time.time()
# print(b-a)


# cards6 = cards
# a = time.time()
# count_sort(cards6)
# b = time.time()
# print(b-a)

# cards7 = cards
# a = time.time()
# cards7 = sorted(cards7)
# b = time.time()
# print(b-a)

# cards8 = cards
# a = time.time()
# cards8.sort()
# b = time.time()
# print(b-a)
