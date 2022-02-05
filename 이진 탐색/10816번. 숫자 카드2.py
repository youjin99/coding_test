###2022/02/05-실패###
import sys 
from collections import Counter

def input():
    return sys.stdin.readline()

n = int(input())
card = list(map(int,input().split()))

m = int(input())
x = list(map(int,input().split()))

count = Counter(card) #Counter : 해당 원소들이 몇 번 등장했는지 세어 딕셔너리 형태로 반환 

for i in x: 
    if i in count:
        print(count[i], end = ' ')
    else: 
        print(0, end = " ")
