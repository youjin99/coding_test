###2022/02/05###
import sys 

def input():
    return sys.stdin.readline()

n = int(input())
array = list(map(int,input().split()))

m = int(input())
x = list(map(int,input().split()))

for i in x: 
    if i in array:
        print(1) #array안에 있으면 1 출력
    else: 
        print(0) #없으면 0 출력 

