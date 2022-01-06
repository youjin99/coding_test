###2022/01/06###
import sys

def input():
    return sys.stdin.readline()

x = ['a','b','c','d','e','f','g','h']
y = [1,2,3,4,5,6,7,8]

n = input()

row = n[1] #열
col = n[0] #행

for i in range(len(x)): #알파벳을 숫자로 변환
    if col == x[i]:
        col = y[i] 

#가능한 이동의 조합
dr = [2,2,-2,-2,1,1,-1,-1]
dc = [1,-1,1,-1,2,-2,2,-2]

count = 0
for j in range(len(dr)):
    r,c = 0,0
    r = int(row) + dr[j]
    c = dc[j] + int(col)
    #나이트는 정원의 밖으로 나갈 수 없다.
    if (1<=r<=8) & (1<=c<=8):
        count += 1

print(count)

#답안 예시
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

#나이트가 이동할 수 있는 8가지 방향 정의 
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

#8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result= 0
for step in steps:
    #이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    #해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8:
        result += 1
        
print(result)

"""입력 
a1
출력
2"""

"""입력
c2
출력
6"""