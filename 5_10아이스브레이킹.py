n, m = map(int, input().split())
map_info = []
for _ in range(n):
    map_info.append(list(map(int, input())))

def dfs(x, y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if map_info[x][y] == 0:
        map_info[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
print(dfs(1,1))

# 3 3
# 001
# 110
# 010
# 답 3

# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000000011000
# 11111111100011
# 11100011111111
# 11100011111111
# 답 8