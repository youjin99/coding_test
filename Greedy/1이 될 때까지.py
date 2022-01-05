###2022/01/05###
import sys

def input():
    return sys.stdin.readline()

N,K = map(int, input().split())

result = 0
while True:
    if N == 1: #N이 1이면 멈춤
        break
    elif N%K == 0: #N을 K로 나누었을 때 나머지가 0이면 N이 K로 나누어떨어짐
        N = N/K 
        result += 1
        if N == 1: 
            break
    else: #N이 K로 나누어 떨어지지 않으면
        N = N - 1 #N-1
        result += 1
        if N == 1:
            break

print(result)

#답안예시1
n, k = map(int, input().split())
result = 0

#N이 K 이상이라면 K로 계속 나누기
while n>=k:
    #N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    #k로 나누기 
    n //= K
    result += 1

#마지막으로 남은 수에 대하여 1씩 빼기
while n>1:
    n -= 1
    result += 1

print(result)

#답안예시2
n, k = map(int, input().split())
result = 0

while True:
    #(N==K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n//k) * K
    result += (n-target)
    n = target
    #N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    #K로 나누기
    result += 1
    n //= K

#마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)

"""입력1
25 5"""

"""입력2
17 4"""