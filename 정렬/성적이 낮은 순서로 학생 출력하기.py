###2022/01/27###
import sys 

def input():
    return sys.stdin.readline()

#학생 수
n = int(input())

student = [] 

def setting(data): 
    return data[1] 

for i in range(n):
    x,y = map(str, input().split())
    student.append((x,int(y))) #[(이름,점수)]

result = sorted(student, key=setting) #점수를 기준으로 오름차순 

for i in range(len(result)):
    print(result[i][0],end=' ') #이름만 출력하기 


"""입력
2
홍길동 95
이순신 77

출력
이순신 홍길동 
"""
