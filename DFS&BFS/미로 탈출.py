###2022/01/14###
import sys
from collections import deque

def input():
    return sys.stdin.readline()

n, m = map(int,input().split())

miro = [[] * _ for _ in range(n)]
for i in range(n):
    x = input()
    for j in range(m):
        miro[i].append(int(x[j]))

#이동할 네 방향 정의(상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#BFS 소스코드 구현 
def bfs(x,y):
    #큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    #큐가 빌 때까지 반복
    while queue:
        x,y = queue.popleft()
        #현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로 찾기 공간을 벗어난 경우 무시 
            if nx < 0 or ny < 0 or nx >= n or ny >=m:
                continue
            #벽인 경우 무시
            if miro[nx][ny] == 0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx,ny))
    #가장 오른쪽 아래까지의 최단 거리 반환 
    return miro[n-1][m-1]
print(bfs(0,0))

"""입력
5 6 
101010
111111
000001
111111
111111"""