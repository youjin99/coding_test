###2022/01/14###
import sys
from collections import deque

n, m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

#DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x,y):
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        #해당 노드 방문 처리
        graph[x][y] = 1
        #상,하,좌,우의 위치들도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

#모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)


"""입력 
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
출력
8"""

"""입력
4 5 
00110
00011
11111
00000
출력
3"""
