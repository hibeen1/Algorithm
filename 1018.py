# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#     # graph.append(list(input().split()))
#     graph.append(input())

# def flip_flop(a):
#     if a == 'W':
#         return 'B'
#     else:
#         return 'W'

# result = int(1e9)

# pp = 0

# for x in range(n-7):
#     for y in range(m-7):
#         temp = graph[x][y]
#         for _ in range(2):
#             cnt = 0
#             pp += 1
#             for dx in range(8):
#                 for dy in range(8):
#                     temp = flip_flop(temp)
#                     if graph[x+dx][y+dy] == temp:
#                         pass
#                     else:
#                         cnt += 1
#                     if dy == 7:
#                         temp = flip_flop(temp)

#             temp = flip_flop(graph[x][y])
#             result = min(result, cnt)

# print(result)        


# # 9 23
# # BBBBBBBBBBBBBBBBBBBBBBB
# # BBBBBBBBBBBBBBBBBBBBBBB
# # BBBBBBBBBBBBBBBBBBBBBBB
# # BBBBBBBBBBBBBBBBBBBBBBB
# # BBBBBBBBBBBBBBBBBBBBBBB
# # BBBBBBBBBBBBBBBBBBBBBBB
# # BBBBBBBBBBBBBBBBBBBBBBB
# # BBBBBBBBBBBBBBBBBBBBBBB
# # BBBBBBBBBBBBBBBBBBBBBBW


chess = [['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB'], ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']]
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(input())
result = int(1e9)

for x in range(n-7):
    for y in range(m-7):
        for k in range(2):
            cnt = 0
            for i in range(8):
                for j in range(8):
                    if graph[x+i][y+j] == chess[k][i][j]:
                        continue
                    else:
                        cnt += 1
            result = min(result, cnt)
print(result)

