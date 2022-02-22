import sys
import heapq

def input():
    return sys.stdin.readline()

INF = int(1e9)
#도시의 개수, 통로의 개수, 메세지를 보내고자 하는 도시 입력받기
n, m, c = map(int,input().split())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    x,y,z = map(int,input().split())
    #X에서 Y로 이어지는 통로, 전달되는 시간 Z
    graph[x].append((y,z))

def dijkstra(start): 
    q = []
    #출발 지점 걸리는 시간을 0으로 설정
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
dijkstra(c)
count = 0 #메시지를 받게 되는 도시의 개수 
max_ = 0 #도시들이 모두 메시지를 받는 데까지 걸리는 시간 
for i in range(2,n+1): 
    if distance[i] != INF: 
        count += 1
        if max_ < distance[i]:
            max_ = distance[i]
print(count, max_)

"""입력 예시
3 2 1
1 2 4
1 3 2"""
