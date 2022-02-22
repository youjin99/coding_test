import sys 

def input():
    return sys.stdin.readline()

n, m = map(int,input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

d = [10001] * (m+1) #0~m원까지 각각의 금액에 대한 최소한의 화폐의 개수 저장 
d[0] = 0

for i in range(n): #각각의 화폐 단위 
    for j in range(coin[i],m+1): #각각의 금액
        if d[j-coin[i]] != 10001: #(i-k)원을 만드는 방법이 존재하는 경우 
            d[j] = min(d[j], d[j-coin[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

"""입력 예시
2 15
2
3
출력 예시
5
"""
"""입력 예시
3 4
3
5
7
출력 예시
-1
"""