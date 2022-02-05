import sys

def input():
    return sys.stdin.readline()

n, m = map(int,input().split())

array = list(map(int,input().split()))

start = 0 #시작점
end = max(array) #끝점 

while start <= end: 
    mid = (start+end) // 2
    length = 0
    for i in array:
        temp = i - mid #잘린 떡의 길이 
        if temp > 0:  
            length += temp 
    if length >= m : #손님이 원하는 떡의 길이와 같거나 길 때
        answer = mid #최대한 덜 잘랐을 때가 정답
        start = mid + 1 #오른쪽 탐색 
    else: #손님이 원하는 떡의 길이보다 짧을 때 
        end = mid - 1 #왼쪽 탐색 

print(answer)    


"""입력
4 6
19 15 10 17
출력
15"""