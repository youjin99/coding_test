###2022/01/17###
import sys

def input():
    return sys.stdin.readline()

n = int(input())
m = int(input())

graph = [[]*_ for _ in range(n+1)]
temp = []

for j in range(m):
    num = list(map(int,input().split()))
    temp.append(num)

for i in range(len(temp)):
    num = temp[i][0]
    num2 = temp[i][1]
    graph[num].append(temp[i][1])
    graph[num2].append(temp[i][0])

from collections import deque

visited = [False] * (n+1)

def BFS(graph, start,visited):
    res = 0
    queue = deque([start])
    visited[start] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                res += 1
    print(res)

BFS(graph,1,visited)