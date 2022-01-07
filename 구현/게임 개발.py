###2022/01/07###
import sys 

def input():
    return sys.stdin.readline()

N, M = map(int, input().split())

x,y,d = map(int,input().split())

#맵 위치마다 바다인지 육지인지 설정 
map_ = [] 
for i in range(N):
    map_.append(list(map(int,input().split())))

#맵의 위치를 설정 
map_path = [] 
for i in range(N):
    for j in range(M):
        map_path.append((i,j))

direction = [0,1,2,3] #북동남서
step = [(-1,0),(0,1),(1,0),(0,-1)] #방향마다 왼쪽으로 갈 때 계산 설정
back = [(1,0),(0,-1),(-1,0),(0,1)] #네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우, 바라보는 방향을 유지한 채 한 칸 뒤로 가는 경우 
already = [(x,y)] #이미 가본 길 

start_x, start_y = x,y #시작 지점 설정 
result = 1 #방문한 칸의 수 
count = 0 #가본 칸이거나 바다 일 때 1씩 증가 

while count != 4:
    for k in direction:
        if k == d and d == 0: #방향이 북쪽일 때 
            start_x,start_y = x+step[-1][0], y+step[-1][1] #start_x, start_y를 업데이트
            if map_[start_x][start_y] == 1: #가려는 칸이 바다인 경우 
                d = direction[-1] #방향 회전
                start_x, start_y = x,y #start_x,start_y 초기화
                count += 1 
                if count == 4: #모든 방향이 갈 수 없는 경우 
                    back_x, back_y = x+back[0][0], y+back[0][1] 
                    if map_[back_x][back_y] == 1: #되돌아 가려는 칸이 바다일때
                        break  #멈춤 
                    else: #바다가 아니라면
                        start_x, start_y = back_x, back_y #한 칸 뒤로 가기 
                        d = direction[0] #방향은 그대로 
            elif map_[start_x][start_y] == 0 and (start_x,start_y) not in already: #육지이고 가보지 않은 칸일 때 
                already.append((start_x,start_y)) #이미 가본 길에 추가 
                result += 1 #가본 칸 +1 
                count = 0 #count 초기화 
                x,y = start_x, start_y #x,y 업데이트 
            elif map_[start_x][start_y] == 0 and (start_x,start_y) in already: #육지이지만 이미 갔던 길일 때
                start_x, start_y = x,y #start_x, start_y 초기화
                d = direction[-1] #방향 회전 
                count += 1
                if count == 4: 
                    back_x, back_y = x+back[0][0], y+back[0][1]
                    if map_[back_x][back_y] == 1:
                        break  
                    else:
                        start_x, start_y = back_x, back_y 
                        d = direction[0]

        elif k == d and d != 0: 
            start_x, start_y = x+step[d-1][0], y+step[d-1][1]
            if map_[start_x][start_y] == 1: 
                d = direction[d-1]
                start_x, start_y = x,y
                count += 1
                if count == 4: 
                    back_x, back_y = x+back[d+1][0], y+back[d+1][1]
                    if map_[back_x][back_y] == 1:
                        break  
                    else:
                        start_x, start_y = back_x, back_y 
                        d = direction[d+1]
            elif map_[start_x][start_y] == 0 and (start_x,start_y) not in already:
                already.append((start_x,start_y))
                result += 1
                count = 0
                x,y = start_x, start_y
            elif map_[start_x][start_y] == 0 and (start_x,start_y) in already:
                start_x, start_y = x,y
                d = direction[d-1]
                count += 1
                if count == 4: 
                    back_x, back_y = x+back[d+1][0], y+back[d+1][1]
                    if map_[back_x][back_y] == 1:
                        break  
                    else:
                        start_x, start_y = back_x, back_y 
                        d = direction[d+1]
                        

print(result)

#답안 예시 
n, m = map(int, input().split())

#방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0]*m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y좌표, 방향 입력받기
x, y, direction = map(int,input().split())
d[x][y] = 1 #현재 좌표 방문 처리 

#전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

#북, 동, 남, 서 방향 정의
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#왼쪽으로 회전
def turn_left():
    global direction 
    direction  -= 1
    if direction == -1:
        direction = 3

#시뮬레이션 시작
count = 1
turn_time = 0
while True:
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]        
    ny = y + dy[direction]
    #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue 
    #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    #네 방향 모두 갈 수 없는 경우
    if turn_time == 4: 
        nx = x - dx[direction]
        ny = y - dx[direction]
        #뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        #뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)



"""입력
4 4 
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
출력 
3"""

"""5 5 
1 1 0
1 1 1 1 1
1 0 0 1 1
1 0 0 0 1
1 0 1 1 1 
1 1 1 1 1"""