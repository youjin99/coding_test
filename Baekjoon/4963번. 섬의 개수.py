###2022/03/17###
import sys 

def input(): 
    return sys.stdin.readline()

while True: 
    #지도의 너비 w, 높이 h
    w,h = map(int, input().split())

    #w,h가 0,0이면 끝 
    if w == 0 and h == 0: 
        break 

    graph = []
    #지도에 대한 정보 받기 
    #1은 땅, 0은 바다
    for i in range(h):
        graph.append(list(map(int,input().split())))

    #DFS 
    def dfs(x,y): 
        if x<=-1 or y<=-1 or x>=h or y>=w: 
            return False 
        elif graph[x][y] == 1: 
            graph[x][y] = 0
            #상하좌우
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            #대각선 
            dfs(x+1,y+1)
            dfs(x-1,y+1)
            dfs(x+1,y-1)
            dfs(x-1,y-1)
            return True 
        return False 

    count = 0
    for i in range(w):
        for j in range(h):
            if dfs(j,i) == True: 
                count += 1
    print(count)