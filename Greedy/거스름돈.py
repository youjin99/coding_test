###2022/01/03###
import sys

def input():
    return sys.stdin.readline()

N = int(input())

coin = [500,100,50,10] 
answer = 0 #거슬러 줘야 할 동전의 개수
for c in coin:
    while N // c != 0: #N : 거스름돈, 거스름돈을 각 동전으로 나눴을 때 몫이 존재하면 그 동전으로 거슬러 줄 수 있다고 판단
        N = N - c #거스름돈에서 그 동전만큼의 금액 차감
        answer += 1 #거슬러 줘야 할 동전의 개수 업데이트 
print(answer)

#답안 예시
n = 1260
count = 0

#큰 단위의 화폐부터 차례대로 확인
coin_types = [500,100,50,10]

for coin in coin_types:
    count += n // coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin #n업데이트 
    
print(n)