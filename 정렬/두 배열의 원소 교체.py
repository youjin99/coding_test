###2022/01/27###
import sys

def input():
    return sys.stdin.readline()

n, k = map(int,input().split())

a = []
b = []

a_num = input().split()
b_num = input().split()

for i in range(n):
    a.append(int(a_num[i]))
    b.append(int(b_num[i]))

a.sort() #오름차순 
b.sort() 
b.reverse() #내림차순 

for i in range(k):
    if a[i] <= b[i]: 
        a[i], b[i] = b[i], a[i] #스와

print(sum(a))


"""입력
5 3
1 2 5 4 3
5 5 6 6 5

출력
26
"""