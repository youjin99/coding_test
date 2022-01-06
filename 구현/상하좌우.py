###2022/01/06###
import sys 

def input():
    return sys.stdin.readline()

N = int(input())

count = list(map(str,input().split()))

#처음 좌표를 (1,1)로 설정 
x = 1 
y = 1

for j in count:
    if j == 'R': #R이면 오른쪽으로 한 칸 
        if 1 <= y+1 <= N: #1과 N사이에 있어야함 
            y += 1
    elif j == 'L':
        if 1<= y-1 <= N:
            y -= 1
    elif j == 'U':
        if 1 <= x-1 <= N:
            x -=1
    elif j == "D":
        if 1 <= x+1 <= N:
            x += 1
    
print(x,y)

#답안예시
n = int(input())
x,y = 1,1
plans = input().split()

#L, R, U, D에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

#이동 계획을 하나씩 확인
for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
    #공간을 벗어나는 경우 무시
    if nx < 1 or ny <1 or nx > n or ny>N:
        continue
    #이동 수행
    x,y = nx, ny

print(x,y)

"""입력
5
R R R U D D"""