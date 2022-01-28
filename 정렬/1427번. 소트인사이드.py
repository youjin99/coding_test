###2022/01/28###
n = input()

array = []
for i in range(len(n)):
    print(n[i])
    array.append(int(n[i]))

array.sort(reverse=True)

for i in array:
    print(i,end="")