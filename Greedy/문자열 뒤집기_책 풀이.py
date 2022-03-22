#문자열 s
s = input()

count0 = 0 #전부 0으로 바꾸는 경우
count1 = 1 #전부 1로 바꾸는 경우 

#첫 번째 원소에 대해서 처리 
if s[0] == '1':
    count0 += 1
else:
    count1 += 1

#두 번째 원소부터 모든 원소를 확인하며 
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        #다음 수에서 1로 바뀌는 경우 
        if s[i+1] == '1':
            count0 += 1
        else: #다음 수에서 0으로 바뀌는 경우
            count1 += 1

print(min(count0,count1))

"""입력예시
0001100
출력예시 
1
"""