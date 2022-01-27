array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(0,i-1): #첫번째부터 i-1번째까지 탐색 
        if array[j] > array[i]:
            array[i], array[j] = array[j], array[i]

print(array)

array = [7,5,9,0,3,1,6,2,4,8]
for i in range(1,len(array)):
    for j in range(i,0,-1): #인덱스 i부터 1까지 감소하며 반복하는 문법 
        if array[j] < array[j-1]: #한칸씩 왼쪽으로 이동 
            array[j], array[j-1] = array[j-1], array[j]
        else: #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
print(array)