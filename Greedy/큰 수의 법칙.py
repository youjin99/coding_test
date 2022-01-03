###2022/01/03###
import sys

def input():
    return sys.stdin.readline()

N,M,K = input().split()
num = input().split()
n = []
for i in range(int(N)):
    n.append(int(num[i]))

max1 = max(n)
n.remove(max1)
max2 = max(n)

sum_ = []
while len(sum_) < int(M):
    for k in range(int(K)):
        sum_.append(max1)
    sum_.append(max2)

answer = sum(sum_)
print(answer)