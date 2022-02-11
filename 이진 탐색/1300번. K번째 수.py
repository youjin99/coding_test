###2022/02/10###
import sys 

def input():
    return sys.stdin.readline()

n = int(input())
k = int(input())

start = 1
end = n*n

while start <= end: 
    mid = (start+end) // 2
    #n*n 배열에서 mid보다 작은 수의 개수 찾기 
    temp = 0
    for i in range(1,n+1): 
        temp += min(n, mid//i)   
    if temp >= k:
        answer = mid  
        end = mid - 1
    elif temp < k: 
        start = mid + 1 

print(answer)



