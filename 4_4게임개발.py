# 1. 왼 쪽 방향으로 일단 돈 다음, 안 가본 땅이면 한 칸 전진. 가 본 땅이거나 바다면 회전만 수행 후 반복.
# 2. 네 방향 다 돌았는데 전진할 수 없다면 방향 유지한 체 뒤로 한 칸 이동. 후 1번 반복.


# 정보 입력 받기
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
map_info = []
for _ in range(n):
    map_info.append(list(map(int, input().split())))

# 방문한 위치를 저장하기 위한 맵 생성
visited = [[0]*m for _ in range(n)]
# 현재 좌표 방문 처리
visited[x][y] = 1
# 북 동 남 서 이동시 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 왼쪽으로 도는 함수 구현
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


cnt = 1
# 회전한 횟수 카운트를 위한 변수
turn_cnt = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if visited[nx][ny] == 0 and map_info[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_cnt = 1
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_cnt += 1
    # 4번 돌아도 갈 데가 없으면 방향 유지한 체 뒤로 이동
    if turn_cnt == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동
        if map_info[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(cnt)

