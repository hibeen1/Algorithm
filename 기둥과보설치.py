# n은 벽면의 크기
# build_frame = [가로좌표, 세로좌표, 기둥/보, 삭제/설치]
# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
# 출력 : [[가로좌표, 세로좌표, 기둥/보], ...]

def check(answer):
    # print(answer)
    for x, y, building in answer:
        if building == 0:
            if y == 0 or [x, y, 1] in answer or [x-1, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif building == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for i in range(len(build_frame)):
        # print(build_frame[i], " : ", answer)
        x, y = build_frame[i][0], build_frame[i][1]
        building = build_frame[i][2]
        delete_or_construct = build_frame[i][3]
        
        if delete_or_construct == 0:
            answer.remove([x, y, building])
            if not check(answer):
                answer.append([x, y, building])
                
        elif delete_or_construct == 1:
            answer.append([x, y, building])
            if not check(answer):
                answer.remove([x, y, building])
    answer.sort()
    return answer



# # 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
# def possible(answer):
#     for x, y, stuff in answer:
#         if stuff == 0: # 설치된 것이 '기둥'인 경우
#             # '바닥 위' 혹은 '보의 한쪽 끝 부분 위' 혹은 '다른 기둥 위'라면 정상
#             if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
#                 continue
#             return False # 아니라면 거짓(False) 반환
#         elif stuff == 1: # 설치된 것이 '보'인 경우
#             # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
#             if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
#                 continue
#             return False # 아니라면 거짓(False) 반환
#     return True

# def solution(n, build_frame):
#     answer = []
#     for frame in build_frame: # 작업(frame)의 개수는 최대 1,000개
#         x, y, stuff, operate = frame
#         if operate == 0: # 삭제하는 경우
#             answer.remove([x, y, stuff]) # 일단 삭제를 해본 뒤에
#             if not possible(answer): # 가능한 구조물인지 확인
#                 answer.append([x, y, stuff]) # 가능한 구조물이 아니라면 다시 설치
#         if operate == 1: # 설치하는 경우
#             answer.append([x, y, stuff]) # 일단 설치를 해본 뒤에
#             if not possible(answer): # 가능한 구조물인지 확인
#                 answer.remove([x, y, stuff]) # 가능한 구조물이 아니라면 다시 제거
#     return sorted(answer) # 정렬된 결과를 반환

print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))