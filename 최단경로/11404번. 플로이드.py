###2022/02/27###
import sys 
import heapq

def input():
    return sys.stdin.readline()

#n : 도시의 개수 
n = int(input())
#m : 버스의 개수
m = int(input())

INF = int(1e9)

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    #a : 출발 도시 , b : 도착 도시, c : 비용
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start): 
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q: 
        dist, now = heapq.heappop(q)
        if distance[now] < dist: 
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost 
                heapq.heappush(q,(cost,i[0]))

for i in range(1,n+1): #1번 도시부터 n번 도시까지 다익스트라 실행 
    dijkstra(i)
    for j in range(1,n+1): #1번 도시부터 n번 도시까지 비용 확인 후 출력 
        if distance[j] == INF:
            print(0, end = " ")
        else: 
            print(distance[j], end=" ")
    distance = [INF] * (n+1) #거리 초기화 
    print()