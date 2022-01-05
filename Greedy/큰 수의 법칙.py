###2022/01/03##
import sys

def input():
    return sys.stdin.readline()

N,M,K = input().split()
num = input().split()
n = []
for i in range(int(N)):
    n.append(int(num[i]))

#가장 큰 두 수만 필요하기 때문에 리스트에서 가장 큰 수, 그 다음으로 큰 수만 따로 빼기로 결정 
max1 = max(n) #가장 큰 수를 max1으로 설정
n.remove(max1) #가장 큰 수 리스트에서 제거
max2 = max(n) #그 다음 큰 수를 max2로 설정

sum_ = []
while len(sum_) < int(M): #M번 더하기 
    for k in range(int(K)): #최대 K번 반복해서 더할 수 있음
        if len(sum_) == int(M):
            break 
        sum_.append(max1) #K번동안 가장 큰 수 더하기 
    if len(sum_) == int(M):
        break
    sum_.append(max2) #K번이 끝나면 그 다음으로 큰 수 더하기

answer = sum(sum_) 
print(answer)

#답안 예시1
n,m,k = map(int, input().split())
data = list(map(int,input().split()))

data.sort() #입력받은 수들 정렬하기
first = data[n-1] #가장 큰 수
second = data[n-2] #두 번째로 큰 수 

result = 0

while True:
    for i in range(k): #가장 큰 수 k번 더하기
        if m == 0: #m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 #더할 때마다 1씩 빼기
    if m == 0: #m이 0이라면 반복문 탈출 
        break
    result += second #두 번째로 큰 수를 한 번 더하기
    m -= 1 #더할 때마다 1씩 빼기
print(result)

#답안예시2
n,m,k = map(int, input().split())
data = list(map(int,input().split()))

data.sort() #입력받은 수들 정렬하기
first = data[n-1] #가장 큰 수
second = data[n-2] #두 번째로 큰 수 

#가장 큰 수가 더해지는 횟수 계산
count = 0
count += int(int(m/(k+1)) * k)
count += m % (k+1)

result = 0
result += count * first #가장 큰 수 더하기
result += (m-count) * second #두 번째로 큰 수 더하기

print(result)

