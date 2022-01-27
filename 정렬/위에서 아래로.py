###2022/01/27###
import sys

def input():
    return sys.stdin.readline()

n = int(input())

#n개의 정수를 입력받아 리스트 만들기 
num = []

for i in range(n):
    x = int(input())
    num.append(x) 

num.sort() #정렬
num.reverse() #내림차순 

#내림차순으로 만든 리스트를 하나씩 출력하기 
for i in num:
    print(i,end=' ')

"""입력
3 
15
27
12"""
