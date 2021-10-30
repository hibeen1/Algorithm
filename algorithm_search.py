# 순차 탐색 O(N)
def sequential_search(target, array):
    for i in range(len(array)):
        if array[i] == target:
            return i+1
    return None

# 이진 탐색 O(logN). 단, 전제 조건이 있는데, 바로 데이터가 정렬되어 있는 상태에서만 유효하다는 것.
def binary_search_recursive(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search_recursive(array, target, start, mid-1)
    else:
        return binary_search_recursive(array, target, mid+1, end)

def binary_search_iterate(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


