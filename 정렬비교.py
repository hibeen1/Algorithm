from random import randint
import time

# selection sort
array = []
for _ in  range(10000):
    array.append(randint(1, 100))

start_time = time.time()

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

end_time = time.time()
print("selection sort : ", end_time - start_time)


# 파이썬 기본 라이브러리 정렬 sort()
array = []
for _ in  range(10000):
    array.append(randint(1, 100))

start_time = time.time()

array.sort()

end_time = time.time()
print("sort() : ", end_time - start_time)


# 파이썬 기본 라이브러리 정렬 sorted()
array = []
for _ in  range(10000):
    array.append(randint(1, 100))

start_time = time.time()

sorted(array)

end_time = time.time()
print("sorted() : ", end_time - start_time)