###2022/01/28###
import sys 

def input():
    return sys.stdin.readline()

n = int(input())

array = []
for i in range(n):
    x,y = map(int,input().split()) 
    array.append((x,y))

def sort_x(data):
    return data[0]

def sort_y(data):
    return data[1]

array.sort()

for i in range(len(array)):
    print(array[i][0],end=" ")
    print(array[i][1])

    