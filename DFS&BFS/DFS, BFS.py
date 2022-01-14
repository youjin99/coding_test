stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()
print(stack)

from collections import deque

que = deque()
que.append(5)
que.append(2)
que.append(3)
que.append(7)
que.popleft()
que.append(1)
que.append(4)
que.popleft()
print(que)

def recursive_function(i):
    #100번째 출력했을 때 종료되도록 종료 조건 명시 
    if i == 100:
        return 
    print(i,'번째 재귀 함수에서',i+1,'번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i,'번째 재귀 함수를 종료합니다.')

recursive_function(1)

#팩토리얼
#반복적으로 구현한 n!
def factorial(n):
    result = 1
    #1부터 n까지의 수를 차례대로 곱하기 
    for i in range(1, n+1):
        result *= i
    return result 

print(factorial(4))

#재귀적으로 구현한 n!
def factorial2(n):
    #n이 1이하인 경우 1을 반환 
    if n <= 1:
        return 1 
    return n*factorial2(n-1)

print(factorial2(4))

#인접 행렬 
INF = 9999999999 #무한의 비용 선언

#2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]

print(graph) #[[0, 7, 5], [7, 0, 9999999999], [5, 9999999999, 0]]

#인접 리스트
#행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]
print(graph) #[[], [], []]

#노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

#노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0,7))

#노드 2에 연결된 노드 저보 저장(노드, 거리)
graph[2].append((0,5))

print(graph) #[[(1, 7), (2, 5)], [(0, 7)], [(0, 5)]]

#DFS예제 
#DFS 메서드 정의
def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True 
    print(v, end='')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문 
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

#정의된 DFS 함수 호출
dfs(graph, 1, visited) #12768345

#BFS 예제
from collections import deque

#BFS 메서드 정의
def bfs(graph, start, visited):
    #큐 구현을 위해 deque 라이브러리를 사용
    queue = deque([start])
    #현재 노드를 방문 처리 
    visited[start] = True
    #큐가 빌 때까지 반복
    while queue: 
        #큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end='')
        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입 
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph, 1,visited) #12387456