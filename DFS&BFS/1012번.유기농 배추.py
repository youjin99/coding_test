###2022/01/19###
import sys
sys.setrecursionlimit(10**5) #런타임에러 방지 
def input():
    return sys.stdin.readline()

T = int(input()) 

#DFS 
def dfs(x,y):
    if x < 0 or y < 0 or x >= m or y >= n:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False 
            
temp = []
res = []
for i in range(T):
    m, n, k = map(int,input().split())

    for j in range(k):
        temp.append(list(map(int,input().split())))
    
    #mXn 크기로 그래프 생성하고 0으로 채움 
    graph = [[]*_ for _ in range(n)]
    for x in range(m):
        for y in range(n):
            graph[y].append(0)
    
    #배추흰지렁이가 있는 곳 1로 변경 
    for _ in range(len(temp)):
        x = temp[_][0]
        y = temp[_][1]
        graph[y][x] = 1

    r = 0
    for y in range(n):
        for x in range(m):
            if dfs(x,y) == True:
                r += 1 

    print(r)
    graph = []
    temp = []
    