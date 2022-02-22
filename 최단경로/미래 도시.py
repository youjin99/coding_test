###2022/02/22###
import sys
import heapq

INF = int(1e9) #무한 
#회사의 개수, 경로의 개수
n, m = map(int,input().split()) 

graph = [[] for i in range(n+1)]
#거리 초기화
distance = [INF] * (n+1)

for i in range(m):
    a, b = map(int,input().split())
    #회사간의 이동은 양방향 이동이 가능하고 1만큼의 시간이 걸림 
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijkstra(start): 
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0 
    while q: 
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]: 
            cost = dist + i[1]
            if cost < distance[i[0]]: 
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

#X, K의 회사 번호 
x, k = map(int,input().split())

#A가 K번 회사까지 이동하는데 걸리는 최소 시간
dijkstra(1)
a = distance[k]
#A가 K번 회사에서 X번회사까지 이동하는데 걸리는 최소 시간 
dijkstra(k)
b = distance[x]
if a+b >= INF: 
    print(-1)
else:
    print(a+b)

"""입력예시1
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
출력 예시1
3"""

"""입력 예시2
4 2
1 3
2 4
3 4
출력 예시2
-1"""