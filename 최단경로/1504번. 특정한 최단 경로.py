###2022/02/23###
import heapq
import sys 

input = sys.stdin.readline
INF = int(1e9)

#노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

#모든 간선 정보를 입력받기 
for _ in range(m): 
    a, b, c = map(int, input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q,(0,start))    
    distance[start] = 0
    while q: #큐가 비어있지 않다면 
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 처리된 적이 있는 노드라면 무시 
        if distance[now] < dist: 
            continue
        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 
            if cost < distance[i[0]]: 
                distance[i[0]] = cost 
                heapq.heappush(q, (cost, i[0]))

#거쳐야 하는 두 개의 정점 두 개 받기
v1, v2 = map(int, input().split())

#1번노드 -> v1 노드 -> v2 노드 -> 마지막노드 가는 최소 경로 
dijkstra(1) #1번 노드에서 v1노드로 가는 가장 짧은 길이  
dist_v1 = distance[v1]
distance = [INF] * (n+1) #왔던 길을 다시 갈 수 있으므로 거리 초기화 
dijkstra(v1) 
dist_v2 = distance[v2]
distance = [INF] * (n+1)
dijkstra(v2)
answer = dist_v1 + dist_v2 + distance[n]

#1번노드 -> v2 노드 -> v1 노드 -> 마지막노드로 가는 최소 경로 
distance = [INF] * (n+1)
dijkstra(1)
dist_v1 = distance[v2]
distance = [INF] * (n+1)
dijkstra(v2)
dist_v2 = distance[v1]
distance = [INF] * (n+1)
dijkstra(v1)
answer_2 = dist_v1 + dist_v2 + distance[n]


if answer >= INF or answer_2 >= INF: #길을 갈 수 없으면 -1 출력
    print(-1)
else: 
    print(min(answer,answer_2)) #경로가 있으면 v1->v2 , v2->v1중에 더 짧은 길 출력 

