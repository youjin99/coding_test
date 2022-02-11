###2022/02/07###
import sys 

def input():
    return sys.stdin.readline()

#갖고있는 랜선의 개수, 필요한 랜선의 개수 
k, n = map(int,input().split()) 

#가지고 있는 각 랜선의 길이 저장 
array = []
for i in range(k):
    array.append(int(input()))

start = 0 #시작점
end = max(array) #끝점
res = 1 #mid = 0일 때 만들 수 있는 랜선의 최대 길이 

while start <= end:
    answer = 0
    mid = (start+end) // 2
    for i in array: 
        if mid != 0:
            temp = i // mid 
            answer += temp 
    if answer < n: 
        end = mid-1 
    elif answer >= n: 
        res = mid #만들 수 있는 랜선의 최대 길이 
        start = mid + 1 
print(res) 
