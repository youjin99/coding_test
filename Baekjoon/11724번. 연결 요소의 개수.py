###2022/03/17-실패###
import sys 

def input(): 
    return sys.stdin.readline()

#정점의 개수 N, 간선의 개수 M 
n, m = map(int,input().split())

graph = [[] for i in range(n+1)]

visited = [False] * (n+1)

for i in range(m): 
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, v, visited):
    visited[v] = True 
    for i in graph[v]: 
        if not visited[i]:
            dfs(graph,i,visited)
            return True 

count = 0

for i in range(1,n+1):  
    if not visited[i]:
        if dfs(graph, i, visited) == True: 
            count += 1

print(count)    
