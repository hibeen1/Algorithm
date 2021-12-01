key =[[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# # new_key = [[6,3,0], [7, 4, 1], [8, 5, 2]]

def rotate_90(key):
    # new_key =[[0] * len(key)] * len(key) # 얕은 복사
    new_key = [[0] * len(key) for _ in range(len(key))] # 깊은 복사
    num = len(key) - 1 # 2
    for i in range(num + 1):
        for j in range(num + 1):
            new_key[j][num-i] = key[i][j]
    return new_key


# def rotate_902(key):
#     num = len(key) # 3
#     new_key =[[0] * num for _ in range(num)]
#     for i in range(num):
#         for j in range(num):
#             new_key[j][num-1-i] = key[i][j]
#     return new_key
# print(rotate_902(key))

# def rotate_90(key):
#     num = len(key) # 3
#     new_key = [[0] * num for _ in range(num)] # 깊은 복사
#     for i in range(num):
#         for j in range(num):
#             new_key[j][num-1-i] = key[i][j]
#     return new_key

# def move_right(key):
#     num = len(key) # 3
#     new_key = [[0] * num for _ in range(num)]
#     for i in range(num):
#         for j in range(num):
#             if j == 0:
#                 new_key[i][j] = 0
#             else:
#                 new_key[i][j] = key[i][j-1]
#     return new_key

# def move_left(key):
#     num = len(key) # 3
#     new_key = [[0] * num for _ in range(num)]
#     for i in range(num):
#         for j in range(num):
#             if j == 2:
#                 new_key[i][j] = 0
#             else:
#                 new_key[i][j] = key[i][j+1]
#     return new_key

# def move_up(key):
#     num = len(key) # 3
#     new_key = [[0] * num for _ in range(num)]
#     for i in range(num):
#         for j in range(num):
#             if i == 2:
#                 new_key[i][j] = 0
#             else:
#                 new_key[i][j] = key[i+1][j]
#     return new_key

# def move_down(key):
#     num = len(key) # 3
#     new_key = [[0] * num for _ in range(num)]
#     for i in range(num):
#         for j in range(num):
#             if i == 0:
#                 new_key[i][j] = 0
#             else:
#                 new_key[i][j] = key[i-1][j]
#     return new_key

            
# print(move_left(key))
            
    
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
    
    for rotation in range(4):
        key = rotate_90(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key [i][j]
                if check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False