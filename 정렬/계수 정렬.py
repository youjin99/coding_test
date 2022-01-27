#모든 원소의 값이 0보다 크거나 같다고 가정 
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
#모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
sort = [0] * (max(array)+1)

for i in range(len(array)):
    n = array[i]
    count = sort[n]
    sort[n] = count + 1 #각 데이터에 해당하는 인덱스의 값 증가 

for i in range(len(sort)): #리스트에 기록된 정렬 정보 확인 
    for j in range(sort[i]):
        print(i, end=' ') #0 0 1 1 2 2 3 4 5 5 6 7 8 9 9 