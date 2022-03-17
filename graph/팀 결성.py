import sys

def input():
    return sys.stdin.readline()

#특정 원소가 속한 집합을 찾기 
def find_parent(parent, x):
    #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출 
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

#N : 노드의 개수, M : 입력으로 주어지는 연산의 개수 
n, m = map(int,input().split())
parent = [0] * (n+1) #부모 테이블 초기화 

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i 

for i in range(m): 
    #0 : 팀 합치기 연산 
    #a, b : a번 학생이 속한 팀과 b번 학생이 속한 팀을 합친다. 
    #1 : 같은 팀 여부 확인 연산 
    #a, b : a번 학생과 b번 학생이 같은 팀에 속해 있는지를 확인하는 연산
    t, a, b = map(int,input().split())
    if t == 0: 
        union_parent(parent, a, b)
    elif t == 1: 
        if parent[a] == parent[b]:
            print("YES")
        else: 
            print("NO")

"""입력 예시
7 8 
0 1 3 
1 1 7 
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
출력 예시
NO
NO
YES
"""