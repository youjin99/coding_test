###2022/01/20###
import sys
from collections import deque

def input():
    return sys.stdin.readline()

m, n = map(int,input().split())

graph = [[]*_ for _ in range(n)]
temp_ = deque()

for i in range(n):
    x = input().split()
    for j in range(m):
        graph[i].append(int(x[j]))
        if int(x[j]) == 1:
            temp_.append([i,j])

dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 0
def bfs(temp_):
    global count
    queue = deque()
    for i in range(len(temp_)):
        x,y = temp_.popleft()
        queue.append([x,y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >=n or ny >=m:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0: 
                queue.append([nx,ny])
                count += 1
                graph[nx][ny] = graph[x][y] + 1
      
    return graph 

graph = bfs(temp_)

max_ = 0
min_ = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            min_ = -1
        elif max_ < graph[i][j]:
            max_ = graph[i][j]

if min_ != 0:
    print(min_)
else:
    print(max_-1)
