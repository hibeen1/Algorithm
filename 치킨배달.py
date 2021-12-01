from itertools import combinations

n, m = map(int, input().split())
map_info = []
for _ in range(n):
    map_info.append(list(map(int, input().split())))

house_sets = []
chicken_sets = []

def chicken_abs(house, chicken):
    return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])


for i in range(n):
    for j in range(n):
        if map_info[i][j] == 1:
            house_sets.append((i, j))
        elif map_info[i][j] == 2:
            chicken_sets.append((i, j))

combination_of_chicken_sets = list(combinations(chicken_sets, m))
print(combination_of_chicken_sets)

result = [0 for _ in range(len(combination_of_chicken_sets))]
for i in range(len(combination_of_chicken_sets)):
    temp = 9999
    temp_result = 0
    for j in range(len(house_sets)):
        for k in range(m):
            temp = min(temp, chicken_abs(house_sets[j], combination_of_chicken_sets[i][k]))
        temp_result += temp
        temp = 9999
    result[i] += temp_result
print(min(result))