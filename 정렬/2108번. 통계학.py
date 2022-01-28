###2022/01/28###
import sys 

def input():
    return sys.stdin.readline()

n = int(input())

array = []

for i in range(n):
    array.append(int(input()))

array.sort()

print(round(sum(array)/n)) #산술평균 
m = n//2
print(array[m]) #중앙값 
    
#최빈값 
length = max(array) - min(array)
#계수 정렬 
if min(array) > 0:
    num_list = [0] * (max(array) +1)
elif max(array) < 0:
    num_list = [0] * (abs(min(array)) +1)
else:
    num_list = [0] * (length+1)

for i in array:
    num_list[i] += 1
print(num_list)

x = max(num_list)
temp = []
for i in range(len(num_list)): 
    if num_list[i] == x: 
        if i > max(array):
            i -= len(num_list)
            temp.append(i)
        else:
            temp.append(i)
if len(temp) == 1:
    print(temp[0])
else:
    temp.sort()
    print(temp[1])

print(length) #범위

"""
6
1
1
3
8
-2
2"""
