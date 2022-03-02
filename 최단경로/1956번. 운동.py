#2022/03/01###
import sys 
import heapq 

def input():
    return sys.stdin.readline()

#V : 마을 개수, E : 도로의 개수 
v, e = map(int,input().split())
INF = int(1e9)
graph = [[INF]*(v+1) for i in range(v+1)]

for a in range(1,v+1):
    for b in range(1,v+1):
        if a == b:
            graph[a][b] = 0
            
cycle=[]
for i in range(e):
    #a번 마을에서 b번 마을로 가는 거리가 c 
    a, b, c = map(int, input().split())
    graph[a][b] =  c
    cycle.append((a,b))

#플로이드 워셜 알고리즘 
for k in range(1, v+1):
    for a in range(1, v+1):
        for b in range(1,v+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = INF
for i in range(1, v+1):
    result = min(result, graph[i][i])
    print(result, graph[i][i])