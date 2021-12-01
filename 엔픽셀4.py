from itertools import combinations

# 2 <= n <= 400

# 임의로 4개의 좌표를 뽑았을 때, 그 4개로 선을 각각 그어봐서(3), 중앙값이 서로 같고, 기울기의 곱이 -1이면 true.

# 기울기, 중점

def solution(n):
    graph = []
    for i in range(n):
        for j in range(n):
            graph.append((i, j))
    print("hello")
    arr = []
    print(len(graph))
    # for i in range(len(graph)):
    #     for j in range(i+1, len(graph)):
    #         dx = graph[i][0] - graph[j][0]
    #         dy = graph[i][1] - graph[j][1]
    #         mid_x = (graph[i][0] + graph[j][0]) / 2
    #         mid_y = (graph[i][1] + graph[j][1]) / 2
    #         if dy == 0:
    #             slope = 9999
    #         else:
    #             slope = dx / dy
    #         arr.append((slope, (mid_x, mid_y)))
    arr2 = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i][1] == arr[j][1]:
                arr2.append((arr[i][0], arr[j][0]))
    

solution(400)

                
from itertools import combinations



def solution(v):
    INF = int(1e9)
    answer = []
    arr = list(combinations(v, 2))
    # 01, 02, 12
    slopes = []
    for i in arr:
        dx = i[0][0] - i[1][0]
        dy = i[0][1] - i[1][1]
        if dx != 0:
            slope = dy / dx
        else:
            slope = INF
        slopes.append(slope)
    
    
    idx = []
    if INF in slopes:
        for i in range(len(slopes)):
            if slopes[i] == INF or slopes[i] == 0:
                idx.append(i)
    else:
        for i in range(1, len(slopes)):
            if slopes[i-1] * slopes[i] == -1:
                idx.append(i-1)
                idx.append(i)
                break
        if len(answer) == 0:
            idx.append(0)
            idx.append(2)
                
    if idx == [0, 1]:
        x = v[1][0] + v[2][0] - v[0][0]
        y = v[1][1] + v[2][1] - v[0][1]
    elif idx == [0, 2]:
        x = v[0][0] + v[2][0] - v[1][0]
        y = v[0][1] + v[2][1] - v[1][1]
    elif idx == [1, 2]:
        x = v[0][0] + v[1][0] - v[2][0]
        y = v[0][1] + v[1][1] - v[2][1]
    return [x, y]

