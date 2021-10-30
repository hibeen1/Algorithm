import sys
from algorithm_search import binary_search_iterate, binary_search_recursive, sequential_search

n = int(sys.stdin.readline().rstrip())
n_array = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
m_array = list(map(int, sys.stdin.readline().rstrip().split()))

n_array.sort()
for i in m_array:
    result = sequential_search(i, n_array)
    # result = binary_search_iterate(n_array, i, 0, n-1)
    # result = binary_search_recursive(n_array, i, 0, n-1)
    if result != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')

