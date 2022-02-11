###2022/02/11###
import sys 

def input():
    return sys.stdin.readline()

n = int(input())
array = list(map(int,input().split()))

temp  = [0]
for i in array: 
    if i in temp: 
        continue
    if temp[-1] < i: 
        temp.append(i)
    else: 
        left = 0
        right = len(temp)
        while left <= right: 
            mid = (left+right) // 2
            if temp[mid] < i:
                left = mid+1 
            else: 
                right = mid 
        temp[right] = i 

print(len(temp)-1)