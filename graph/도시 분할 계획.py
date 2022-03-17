import sys

def input():
    return sys.stdin.readline()

def find_parent(parent,x):
    if parent[x] != x: 
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else: 
        parent[a] = b

#N : 집의 개수, M : 길의 개수 
n, m = map(int, input().split())
parent = [0] * (n+1) #부모 테이블 초기화 

#모든 간선을 담을 리스트와 최종 비용을 담을 변수 
edges = []
result = 0

#부모 테이블상에서, 부모 자기 자신으로 초기화 
for i in range(n+1):
    parent[i] = i

#모든 간선에 대한 정보 입력받기 
for i in range(m):
    #A번 집과 B번 집을 연결하는 유지비가 C이다. 
    a, b, c = map(int, input().split())
    #비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정  
    edges.append((c, a, b))

#간선을 비용순으로 정렬
edges.sort()
last = 0 #최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선 

#간선을 하나씩 확인하며
for edge in edges: 
    cost, a, b = edge
    #사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost 
        last = cost  

print(result - last)

"""입력예시
7 12 
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
출력예시 
8
"""