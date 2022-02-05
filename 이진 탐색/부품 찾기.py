import sys

def input(): 
    return sys.stdin.readline()

#매장에 있는 부품 개수 
n = int(input()) 
#매장에 있는 부품 번호 
item = list(map(int,input().split()))

#손님이 요청한 부품 개수 
m = int(input())
#손님이 요청한 부품 번호 
want = list(map(int,input().split()))

#이진 탐색 
def binary_search(item,target,start,end):
    while start <= end: 
        mid = (start+end) // 2
        if item[mid] == target: 
            return mid
        elif item[mid] > target: 
            end = mid - 1
        else: 
            start = mid + 1
    return None 

for i in want:
    result = binary_search(item, i, 0, n-1)
    if result == None: 
        print("no",end=' ')
    else:
        print("yes",end=' ')
        
"""입력
5
8 3 7 9 2
3 
5 7 9
출력
no yes yes"""