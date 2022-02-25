###2022/02/25-실패###
import sys

def input():
    return sys.stdin.readline()

INF = int(1e9)

#N : 도시의 개수, M : 버스 노선의 개수 
n, m = map(int,input().split())

graph = []
distance = [INF] * (n+1)

for i in range(m):
    #A : 시작도시, B : 도착도시, C : 버스를 타고 이동하는데 걸리는 시간 
    a, b, c = map(int,input().split())
    graph.append((a,b,c))

#벨만포드 알고리즘
def bellman_ford(start):
    distance[start] = 0
    #n번 반복
    for i in range(1,n+1):
        #매 반복마다 모든 간선 확인
        for j in range(m):
            now, next, cost = graph[j][0], graph[j][1], graph[j][2]
            #현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[now] != INF and distance[next] > distance[now] + cost: 
                distance[next] = distance[now] + cost
                #n번째 반복에서도 값이 갱신된다면 음수 순환 존재  
                if i == n: 
                    return True
    return False

negative_cycle = bellman_ford(1)
if negative_cycle:
    print(-1)
else:
    for i in range(2,n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
