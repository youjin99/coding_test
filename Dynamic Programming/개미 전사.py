import sys 

def input():
    return sys.stdin.readline()

n = int(input())

array = list(map(int,input().split()))

#다이나믹 프로그래밍 
d = [0] * 100
d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(3, n): 
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[n-1])


"""입력 예시
4
1 3 1 5
출력 예시
8"""

#예시 답안 