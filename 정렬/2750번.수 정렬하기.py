###2022/01/27###
import sys 

def input():
    return sys.stdin.readline()

n = int(input())  #정수의 개수 

array = []
for i in range(n):
    array.append(int(input()))

array.sort() #오름차순

for i in array:
    print(i)


