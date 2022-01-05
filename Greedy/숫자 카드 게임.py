###2022/01/05###

import sys

def input():
    return sys.stdin.readline()

N, M = map(int,input().split())

num = []
for i in range(N):
   n = input().split()
   num.append(n) #각 행마다 리스트로 묶어서 저장 

answer = 0 #가장 작은 수 설정
for j in range(N):
    min_ = int(min(num[j])) #각 행에서 가장 작은 수 찾기
    if answer < min_: #더 큰 숫자를 answer로 설정 
        answer = min_

print(answer)

#답안 예시1
n, m = map(int,input().split())

result = 0
#한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int,input().split()))
    #현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    #가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)

#답안 예시2
n, m = map(int,input().split())

result = 0
for i in range(n):
    data = list(map(int,input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)

"""입력1
3 3 
3 1 2
4 1 4
2 2 2"""

"""입력2
2 4 
7 3 1 8
3 3 3 4"""