###2022/02/09###
import sys 

def input():
    return sys.stdin.readline()

n, c = map(int,input().split())

array = [0] * 1000000001

min_ = 1000000001
max_ = 0
for i in range(n):
    num = int(input())
    array[num] += 1 
    if min_ > num: 
        min_ = num 
    if max_ < num:
        max_ = num 
        
temp = [min_,max_]

#왼쪽 부분 탐색 
def left(array, start, end): 
    while start <= end: 
        mid = (start+end) // 2
        if array[mid] == 1: 
            array[mid] = 0
            return mid 
        else:
            end = mid-1 

#오른쪽 부분 탐색 
def right(array, start, end): 
    while start <= end: 
        mid = (start+end) // 2
        if array[mid] == 1:
            array[mid] = 0 
            return mid
        else:
            start = start+1 

def binary_search(array, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == 1: 
            temp.append(mid)
            array[mid] = 0
            if len(temp) == c: 
                return temp  
        else:
            mid = right(array, mid+1, end) 
            temp.append(mid)
            if len(temp) == c: 
                return temp  
            else:
                mid = left(array,start,mid-1)
                temp.append(mid)
                if len(temp) == c: 
                    return temp 
start = 0
end = max_ 

temp = binary_search(array,start,end)
temp.sort(reverse=True)

min_ = 1000000000
for i in range(c-1): 
    if min_ > temp[i] - temp[i+1]:
        min_ = temp[i] - temp[i+1]

sys.stdout.write(str(min_))

