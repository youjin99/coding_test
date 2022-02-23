###2022/02/23###
import sys 
import heapq 

def input():
    return sys.stdin.readline()

INF = int(1e9) #무한 
#정점과 간선의 개수 받기 
n, e = map(int,input().split())
#시작 번호
k = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1) #무한으로 거리 초기화

for i in range(e):
    u,v,w = map(int,input().split())
    #u에서 v로 가는데 w만큼의 시간이 걸린다. 
    graph[u].append((v,w))

def dijkstra(start): 
    q = []
    distance[start] = 0
    heapq.heappush(q,(0, start))
    while q: 
        dist, now = heapq.heappop(q)
        if distance[now] < dist: 
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(k)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])