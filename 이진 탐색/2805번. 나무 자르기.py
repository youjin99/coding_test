###2022/02/08###
import sys 

def input():
    return sys.stdin.readline()

#나무의 수, 집으로 가져가려고 하는 나무의 길이
n, m = map(int,input().split())

#나무의 높이 
array = list(map(int,input().split()))

start = 0 #시작점
end = max(array) #끝점 

while start <= end: 
    answer = 0
    mid = (start+end) // 2
    for i in array: 
        temp = i - mid 
        if temp > 0: 
            answer += temp 
    if answer < m: 
        end = mid - 1
    else: 
        res = mid #만들 수 있는 나무의 최대 길이 
        start = mid + 1
print(res)
