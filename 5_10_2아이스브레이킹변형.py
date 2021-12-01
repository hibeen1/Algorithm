n = int(input())
graph = []
copy_graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

temp = 0
arr = []

def dfs(x, y):
    if x<0 or x>=n or y<0 or y>=n:
        return 0
    if graph[x][y] == 1:
        graph[x][y] = 0
        global temp
        temp += 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return 1
    return 0

result = 0
arr = []
for x in range(n):
    for y in range(n):
        if dfs(x,y) != 0:
            result += 1
            arr.append(temp)
            temp = 0            

print(result)
print(arr)

# 6
# 011000
# 011011
# 000011
# 000011
# 110010
# 111000
