###2022/01/17###
import sys

def input():
    return sys.stdin.readline()

n,m,v = map(int, input().split())

graph = [[]*_ for _ in range(n+1)]
temp = []

for i in range(m):
    x = list(map(int,input().split()))
    temp.append(x)
for j in range(len(temp)):
    num = temp[j][0]
    num2 = temp[j][1]
    graph[num].append(temp[j][1])
    graph[num2].append(temp[j][0])

for i in range(len(graph)):
    graph[i].sort()

visited = [False] * (n+1)

#DFS 
def DFS(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for z in graph[v]:
        if visited[z] == False:
            DFS(graph, z, visited)
DFS(graph, v, visited)
#BFS
from collections import deque

visited = [False] * (n+1)

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
print(sep='\n')
BFS(graph,v,visited)