###2022/01/18-실패###
import sys 
from collections import deque

def input():
    return sys.stdin.readline()

N = int(input())

#graph
graph = [[]*_ for _ in range(N)]

for i in range(N):
    g = input()
    for j in range(N):
        graph[i].append(int(g[j]))

count = 0
def dfs(x,y):
    global count
    if x <= -1 or y <= -1 or x >= N or y >= N:
        return False
    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False
   
result = 0
count = 0
num = []
for i in range(N):
    for j in range(N):
        if dfs(i,j) == True:
            num.append(count)
            result += 1 #처음 방문할때만 result += 1 
            count = 0

num.sort()
print(result, sep='\n')
for i in num:
    print(i, sep='\n')

