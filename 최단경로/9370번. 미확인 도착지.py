###2022/02/24###
import sys 
import heapq

def input():
    return sys.stdin.readline()
INF = int(1e9) #무한
#테스트 케이스 수 
T = int(input())

def dijkstra(start): 
    q =[]
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

            
for i in range(T):
    #n : 교차로, m : 도로, t : 목적지 후보의 개수 
    n, m, t = map(int,input().split())
    #s : 예술가들의 출발지, g와h 교차로 사이에 있는 도로를 지나갔다. 
    s, g, h = map(int,input().split())
    
    graph = [[] for i in range(n+1)]
    distance = [INF] * (n+1)

    for i in range(m): 
        #a와 b사이에 길이 c의 양방향 도로가 있다. 
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))

    #목적지 후보들 
    temp = []
    for i in range(t): 
        end = int(input())
        #출발노드에서 다익스트라 실행 
        dijkstra(s)
        #출발노드 -> 끝노드
        dist_s_e = distance[end]
        #출발노드 -> g노드
        dist_s_g = distance[g]
        #출발노드 -> h노드 
        dist_s_h = distance[h]
        #거리 초기화 
        distance = [INF] * (n+1)
        #g노드에서 다익스트라 실행
        dijkstra(g)
        #g노드->h노드 / h노드->g노드 
        dist_g_h = distance[h]
        #g노드 -> end노드 
        dist_g_e = distance[end]
        #거리 초기화 
        distance = [INF] * (n+1)
        #h노드에서 다익스트라 실행
        dijkstra(h)
        #h노드 -> end노드
        dist_h_e = distance[end]
        #거리 초기화 
        distance = [INF] * (n+1)

        #출발 -> g -> h -> 끝
        dist_s_g_h_e = dist_s_g + dist_g_h + dist_h_e
        #출발 -> h -> g -> 끝
        dist_s_h_g_e = dist_s_h + dist_g_h + dist_g_e
        if dist_s_e >= dist_s_g_h_e or dist_s_e >= dist_s_h_g_e: 
            temp.append(end)

    temp.sort()
    for i in temp:
        print(i, end= " ")
    print()
    
"""
2
5 4 2
1 2 3
1 2 6
2 3 2
3 4 4
3 5 3
5
4
6 9 2
2 3 1
1 2 1
1 3 3
2 4 4
2 5 5
3 4 3
3 6 2
4 5 4
4 6 3
5 6 7
5
6
"""
