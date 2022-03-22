import sys 

def input():
    return sys.stdin.readline()

#N : 모험가의 수 
n = int(input())

#모험가의 공포도 받기 
people = list(map(int,input().split()))

#정렬 
people.sort()

count = 0 #그룹 개수  
while people: #사람이 없을 때 까지
    m = people.pop() #가장 큰 공포도 
    for i in range(m): #가장 큰 공포도만큼 사람 넣기 
        if len(people) !=0: #사람이 남아있다면
            people.pop() #그룹n에 넣기 
        else: #사람이 부족하다면
            break #멈춤 
    count += 1 #한 그룹이 완성되면 +1 


print(count)

"""입력예시
5 
2 3 1 2 2
출력예시
2
"""